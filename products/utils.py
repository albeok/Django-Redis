from web3 import Web3
import os

def generic_info_dict(Lot):
    generic_info_dict = {
        "lot_code" : Lot.lot_code,
        "tracking_code" : Lot.tracking_code,
        "production_quantity" : str(Lot.production_quantity),
        "date_time_arrival" : str(Lot.date_time_arrival),
        "date_time_production" : str(Lot.date_time_production),
        "manufacturing_plant" : Lot.manufacturing_plant,
        "recipient" : Lot.recipient
        }
    return generic_info_dict

def send_transaction(message):
    # Create a new Ethereum transaction and send it on chain

    w3 = Web3(Web3.HTTPProvider('https://ropsten.infura.io/v3/14d63739bfa14c85b13dd1a8f37681e1'))
    address = '0x00891B1C6c959E953E02B79038BA985AF378f93F'
    private_key = '0x73e9350848f90d2f0e36f3fc6d5cad35e3891ba2541b70f8bdd339fcf4b2fc95'
    nonce = w3.eth.getTransactionCount(address)
    gas_price = w3.eth.gasPrice
    value = w3.toWei(0, 'ether')
    signed_tx = w3.eth.account.signTransaction(dict(
        nonce=nonce,
        gasPrice=gas_price,
        gas=100000,
        to='0x0000000000000000000000000000000000000000',
        value=value,
        data=message.encode('utf-8')
    ), private_key)

    tx = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    tx_id = w3.toHex(tx)
    return tx_id