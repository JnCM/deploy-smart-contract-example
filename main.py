import json
from environs import Env
from web3 import Web3

env = Env()
env_filename = '.env'
env.read_env(env_filename, recurse=False)

# Blockchain credentials
URL_PROVIDER = env.str("URL_PROVIDER")
ACC_PUBLIC_KEY = env.str("ACC_PUBLIC_KEY")
ACC_PRIVATE_KEY = env.str("ACC_PRIVATE_KEY")
# Contract data obtained by solidity compiler (solc)
CONTRACT_BYTECODE = env.str("CONTRACT_BYTECODE")
CONTRACT_ABI = json.loads(env.str("CONTRACT_ABI"))

# Functions definitions

def connect_blockchain():
    web3_cnn = Web3(Web3.HTTPProvider(URL_PROVIDER))
    if not web3_cnn.is_connected():
        print("=== Provider was not connected! ===")
        return None
    return web3_cnn

def deploy_contract(web3_cnn):
    # Submit contract in blockchain
    web3_cnn.eth.default_account = ACC_PUBLIC_KEY
    HelloWorld = web3_cnn.eth.contract(abi=CONTRACT_ABI, bytecode=CONTRACT_BYTECODE)
    tx_hash = HelloWorld.constructor().transact()
    tx_receipt = web3_cnn.eth.wait_for_transaction_receipt(tx_hash)
    contract_address = tx_receipt.contractAddress
    # Saving contract address in .env file
    env_file = open(env_filename, 'a', encoding='utf-8')
    env_file.write(f'CONTRACT_ADDRESS={str(contract_address)}\n')
    env_file.close()
    # Returning the contract in Blockchain
    return web3_cnn.eth.contract(address=contract_address, abi=CONTRACT_ABI)

def using_contract(web3_cnn, contract):
    print(contract.functions.greet().call())
    tx_hash = contract.functions.setGreeting('Olá, Mundo!').transact()
    tx_receipt = web3_cnn.eth.wait_for_transaction_receipt(tx_hash)
    print(contract.functions.greet().call())

# Calling the functions
if __name__ == "__main__":
    web3_cnn = connect_blockchain()
    contract = deploy_contract(web3_cnn)
    using_contract(web3_cnn, contract)
