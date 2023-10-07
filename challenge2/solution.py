import requests
import json
import re
from web3 import Web3

ETHERSCAN_URL = "https://api.etherscan.io/api?module=proxy&action=eth_getTransactionReceipt&txhash="
TRANSFER_HASH = "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef"

# https://api.etherscan.io/api?module=proxy&action=eth_getTransactionReceipt&txhash=0x3fbb21da357fdd74a12319ee423b4f30829030ba53b1d8d9e005c0da138e2263

def print_transfers(transaction_hash: str):
    if not re.search(r'^0x([A-Fa-f0-9]{64})$', transaction_hash): 
        raise Exception('Invalid transaction hash')
    
    response = requests.get(f'{ETHERSCAN_URL}{transaction_hash}')
    if response.status_code != 200:
        raise Exception('Failed etherscan request')
    
    response_dict = response.json()
    logs = response_dict.get('result').get('logs')

    def filterTransferLogs(log): 
        topics = log.get('topics')
        if topics[0] != TRANSFER_HASH:
            return False
        return True

    def parseTransferLog(log):
        topics = log.get('topics')
        return {
            'from': Web3.to_checksum_address('0x' + topics[1][-40:]),
            'to': Web3.to_checksum_address('0x' + topics[2][-40:]),
            'amount': int(log.get('data'), base=16)
        }

    filtered_logs = filter(filterTransferLogs, logs)
    result = map(parseTransferLog, filtered_logs)
    return json.dumps(list(result))




if __name__ == '__main__':
   hash = input('Enter transaction hash: ')
   r = print_transfers(hash)
   print('r', r)