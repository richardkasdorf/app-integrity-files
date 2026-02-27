import os
from dotenv import load_dotenv
from web3 import Web3


load_dotenv()

RPC_URL = os.getenv("SEPOLIA_RPC_URL")
w3 = Web3(Web3.HTTPProvider(RPC_URL))



if not w3.is_connected():
    raise Exception("Falha na conexão com Sepolia!")
print("Conectado à Sepolia! Chain ID:", w3.eth.chain_id)

PRIVATE_KEY = os.getenv("PRIVATE_KEY")  
account = w3.eth.account.from_key(PRIVATE_KEY)
sender_address = account.address


CONTRACT_ADDRESS = "0x234531fd78aE649463c7e5d392F9d8658BEf95Ab" 
CONTRACT_ABI = [
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": True,
				"internalType": "address",
				"name": "user",
				"type": "address"
			},
			{
				"indexed": False,
				"internalType": "bytes32",
				"name": "hashValue",
				"type": "bytes32"
			},
			{
				"indexed": False,
				"internalType": "uint256",
				"name": "timestamp",
				"type": "uint256"
			}
		],
		"name": "HashStored",
		"type": "event"
	},
	{
		"inputs": [
			{
				"internalType": "bytes32",
				"name": "_hash",
				"type": "bytes32"
			}
		],
		"name": "storeHash",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_user",
				"type": "address"
			}
		],
		"name": "getHash",
		"outputs": [
			{
				"internalType": "bytes32",
				"name": "",
				"type": "bytes32"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"name": "storedHashes",
		"outputs": [
			{
				"internalType": "bytes32",
				"name": "",
				"type": "bytes32"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]


contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=CONTRACT_ABI)


file_hash = "0x977aa5ecd4e8af1049f8355b65e9fab2373afa803fd97399f462be7c5c381d54" 


nonce = w3.eth.get_transaction_count(sender_address)


tx = contract.functions.storeHash(file_hash).build_transaction({
    'from': sender_address,
    'nonce': nonce,
    'gas': 100000,                  
    'maxFeePerGas': w3.to_wei(50, 'gwei'),     
    'maxPriorityFeePerGas': w3.to_wei(2, 'gwei'),
    'chainId': 11155111             
})


signed_tx = w3.eth.account.sign_transaction(tx, private_key=PRIVATE_KEY)
tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)

print(f"Transação enviada! Hash: {tx_hash.hex()}")


receipt = w3.eth.wait_for_transaction_receipt(tx_hash, timeout=300)
if receipt.status == 1:
    print("Sucesso! Hash armazenado na blockchain.")
else:
    print("Falha na transação.")

