test = {'status': '1',
 'message': 'OK',
  'result': [{'blockNumber': '6111934', 'timeStamp': '1617048483', 'hash': '0x3969d98d5fc68aff0eebaca57ba02a4af755354df2530bcf9004836a77f77dd7',
   'nonce': '91',
    'blockHash': '0xb6c41b0f2f1910637c76a2984cf26dcce633c8e26b49f8f3ed4ae809cadb25c2',
     'from': '0xb25122ab1e0e44d73b7c35e378201787bc9594ed',
      'contractAddress': '0x69af49e82ea59a97f3879547f67b913c216c3714',
       'to': '0xcc64ea842fcde4283cf239259f7462ef809c44fd',
        'value': '9400000', 'tokenName': 'UNITi', 'tokenSymbol': 'UNIT', 'tokenDecimal': '9', 'transactionIndex': '13', 'gas': '154734', 'gasPrice': '10000000000', 'gasUsed': '103156', 'cumulativeGasUsed': '2243418', 'input': 'deprecated', 'confirmations': '80877'}]}

print(test['result'][0]['blockNumber'])

whales = [{"0xcC64ea842FcDe4283CF239259f7462Ef809c44FD",5},
         {"0x7238B14Ed465991EecCB9346cf435eE047dea6eD",8}]

for whale in whales:
        print(whale)

