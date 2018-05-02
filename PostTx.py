#Post transactions on Testnet
from blockcypher import create_unsigned_tx
from blockcypher import broadcast_signed_transaction
from blockcypher import make_tx_signatures
from blockcypher import embed_data




string_to_post = "MyFirstOpReturnTransaction";
data_hex = string_to_post.encode("hex");
output_script = '6a13'+ data_hex;

inputs = [{'address':'mi1PUPDpwxHsmGhpTsy5LrsPuAkQMT9QLP'}, ];
outputs = [{'address': 'myAg6VTDJN4ktQ8F7xYLxZBTSGYuy8vVGV', 'value': 1},{'value':0, 'script_type':'null-data','data_string': 'My first op_return transactions', 'script': output_script},];
unsigned_tx = create_unsigned_tx(inputs=inputs, outputs=outputs, coin_symbol='btc-testnet',api_key = '9ec8d9d06347455b833d04031f7b4c9a');

#embed_data(to_embed='I am the walrus', api_key='07b8071917974a62aeafd77880afe93b', coin_symbol='btc-testnet',data_is_hex=False);
#print unsigned_tx;

privkey_list = ['93021c6bc9ee89c06d57931a99341df6cadadb9d0e82ac4acb205b03f0afc03d'];
pubkey_list = ['034cf1d96e5d632c64d987a5db49d1a0840c6fac7e138af2ce027ddee5bc787941'];
print len(privkey_list), len(pubkey_list), len(unsigned_tx['tosign'])
tx_signatures = make_tx_signatures(txs_to_sign=unsigned_tx['tosign'], privkey_list=privkey_list, pubkey_list=pubkey_list);


Tx = broadcast_signed_transaction(unsigned_tx=unsigned_tx, signatures=tx_signatures, pubkeys=pubkey_list,coin_symbol = 'btc-testnet',api_key = '9ec8d9d06347455b833d04031f7b4c9a');

print Tx['tx']['hash'];
#for key in Tx['tx']:
#	print key;



