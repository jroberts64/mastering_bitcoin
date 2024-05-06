from bitcoin.rpc import RawProxy, Proxy

print('starting')

p: Proxy = RawProxy(service_url='http://umbrel:cehXos-viphyk-5tohdo@umbrel.local:8332')

blockheight = 775072

blockhash = p.getblockhash(blockheight)

block = p.getblock(blockhash)

transactions = block['tx']
print('Num transactions = ', len(transactions))
block_value = 0

for txid in transactions:
    tx_value = 0
    raw_tx = p.getrawtransaction(txid)
    decode_tx = p.decoderawtransaction(raw_tx)
    for output in decode_tx['vout']:
        tx_value = tx_value + output['value']
    # print('tx_value = ', tx_value)

    block_value = block_value + tx_value

print('Total value in block: ', block_value)
