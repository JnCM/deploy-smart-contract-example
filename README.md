# Implantação de um Contrato Inteligente na Blockchain - Exemplo com Web3 e Python

## Requisitos

Recomenda-se a criação de um ambiente virtual em Python para evitar erros de versões ao executar este projeto. Com o ambiente virtual criado e ativado, execute o seguinte comando para instalar as dependências necessárias:

```bash
pip install -r requirements.txt --no-cache-dir
```

Após a instalação das dependências do código, é necessário instalar o compilador da linguagem Solidity, caso não esteja instalado. Instruções de instalação podem ser obtidas [aqui](https://docs.soliditylang.org/en/latest/installing-solidity.html).

**OBS.:** Para instalação e uso do compilador recomendo o WSL (Windows Subsystem for Linux) caso o sistema operacional for Windows, pois o método de instalação será o mesmo para o Linux (mais simples e prático).

Com o compilador instalado, execute os seguintes comandos para compilar o contrato inteligente de exemplo, obter seu Bytecode e ABI, respectivamente.

```bash
solc HelloWorld.sol # Compila o contrato inteligente
solc HelloWorld.sol --bin # Retorna o bytecode no terminal
solc HelloWorld.sol --abi # Retorna o ABI no terminal
```

Após isso, guarde tanto o Bytecode quanto o ABI para serem utilizados nas variáveis de ambiente em seguida.

## Estrutura das variáveis de ambiente

As variáveis de ambiente são importantes, pois mascaram dados sensíveis ao invés de coloca-los diretamente no código. Crie um arquivo `.env` no mesmo local que o arquivo `main.py` e defina as seguintes variáveis:

```env
URL_PROVIDER= # URL de conexão RPC com a Blockchain
ACC_PUBLIC_KEY= # Chave pública da conta
ACC_PRIVATE_KEY= # Chave privada da conta (opcional para este exemplo)
CONTRACT_BYTECODE= # Bytecode do contrato inteligente compilado
CONTRACT_ABI= # ABI do contrato inteligente compilado
```

Exemplo das variáveis de ambiente preenchidas:

```env
URL_PROVIDER=http://127.0.0.1:7545 # Conexão padrão do Ganache
ACC_PUBLIC_KEY=0xE7E9B917D5ffaCF42Db48101Af52Af8619d32b78
ACC_PRIVATE_KEY=0xe8d04041532c27ba0e80a3e0f935e98458924283091b57965ed90806cbfee5cf
CONTRACT_BYTECODE=60806040523480156200001157600080fd5b50604...
CONTRACT_ABI=[{"inputs":[],"stateMutability":"nonpayable"...
```

## Execução

Para executar o código, basta executar o comando:

```bash
python main.py
```

Ao final da execução, será possível verificar que no arquivo `.env` foi gravado o endereço do contrato inteligente implantado na Blockchain. Além disso, no terminal será possível visualizar a saída esperada do teste de execução do mesmo:

```txt
Hello, World!
Olá, Mundo!
```

Caso esteja utilizando uma rede de teste como o Ganache, poderá visualizar o bloco de criação do contrato, assim como o bloco que grava a chamada do contrato para teste.
