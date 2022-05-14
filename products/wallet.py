from web3 import Web3

w3 = Web3(Web3.HTTPProvider("https://ropsten.infura.io/v3/14d63739bfa14c85b13dd1a8f37681e1"))
account = w3.eth.account.create()
private_key = account.privateKey.hex()
address = account.address
print(f"address wallet:{address}\nkey wallet: {private_key}")
