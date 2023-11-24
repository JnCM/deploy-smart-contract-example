// SPDX-License-Identifier: GPL-3.0

pragma solidity 0.8.19;

contract HelloWorld {
    string public greeting;

    constructor() {
        greeting = 'Hello, World!';
    }

    function setGreeting(string memory _greeting) public {
        greeting = _greeting;
    }

    function greet() view public returns (string memory) {
        return greeting;
    }
}