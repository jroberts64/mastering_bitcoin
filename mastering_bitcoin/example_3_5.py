from bitcoin.rpc import RawProxy, Proxy
from env import ENV

env = ENV()

p: Proxy = RawProxy(service_url=env.service_url)

info = p.getblockchaininfo()

print(info)
print('--------------------------------------')
# Alice's transaction ID
txid = "466200308696215bbc949d5141a49a4138ecdfdfaa2a8029c1f9bcecd1f96177"

# Get raw transaction in hex
raw_tx = p.getrawtransaction(txid)

# Decode the raw transaction to JSON
decoded_tx = p.decoderawtransaction(raw_tx)

# Get outputs
for output in decoded_tx['vout']:
    print(output['scriptPubKey']['address'], output['value'])
