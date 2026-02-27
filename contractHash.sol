// SPDX-License-Identifier: MIT
pragma solidity ^0.8.26;

contract contractHash {
    
    mapping(address => bytes32) public storedHashes;

    // Evento auditoria
    event HashStored(address indexed user, bytes32 hashValue, uint256 timestamp);

    // armazena hash
    function storeHash(bytes32 _hash) public {
        storedHashes[msg.sender] = _hash;
        emit HashStored(msg.sender, _hash, block.timestamp);
    }

    // Ler hash
    function getHash(address _user) public view returns (bytes32) {
        return storedHashes[_user];
    }
}



