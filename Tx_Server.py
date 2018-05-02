#This defines the class and methods for the server to post the information on the Blockchain
from blockcypher import create_unsigned_tx
from blockcypher import broadcast_signed_transaction
from blockcypher import make_tx_signatures
from blockcypher import embed_data
from merkletools import MerkleTools
import hashlib
import socket




class Tx_Server:

	Filename = "";
	privkey = ['93021c6bc9ee89c06d57931a99341df6cadadb9d0e82ac4acb205b03f0afc03d'];
	pubkey = ['034cf1d96e5d632c64d987a5db49d1a0840c6fac7e138af2ce027ddee5bc787941'];
	Sender_addr = 'mi1PUPDpwxHsmGhpTsy5LrsPuAkQMT9QLP';
	Address = 'myAg6VTDJN4ktQ8F7xYLxZBTSGYuy8vVGV';
	MyToken = '07b8071917974a62aeafd77880afe93b';
	root = "";
	BTC_MT = MerkleTools(hash_type="SHA256");
	zonefile = [];
	Proof = [];
	Tx_hash = "";

	def __init__(self, zonefile):
		self.Filename = zonefile;


	def CreateMerkleTree(self):

		zonefile = [line.rstrip('\n') for line in open(self.Filename)];
		# you may also want to remove whitespace characters like `\n` at the end of each line
		#print(zonefile);
		
		self.BTC_MT.add_leaf(zonefile, True);

		self.BTC_MT.make_tree();
		self.root = self.BTC_MT.get_merkle_root();

		self.Post_MerkleRoot();

		for i in range(len(zonefile)):
			temp_proof = {};
			temp_proof['hostname'] = zonefile[i].split(" ", 1)[0];
			temp_proof['record'] = zonefile[i];
			temp_proof['proof'] = self.BTC_MT.get_proof(i);
			temp_proof['Tx_hash'] = self.Tx_hash;
			self.Proof.append(temp_proof);

		#print self.Proof;
		f = open('Proof', 'w');
		for x in self.Proof:
			f.write(str(x) + '\n');
		f.close();

		'''f=open('Proof','w');
		f.write(Proof_str);
		f.close();'''

		print hashlib.sha256(zonefile[1]).hexdigest();
		print self.BTC_MT.get_leaf(1);

	def get_root(self):
		return self.root;

	def Post_MerkleRoot(self):
		hex_to_post = self.root.encode("hex");
		output_script = '6a13' + hex_to_post;
		inputs = [{'address': self.Sender_addr}, ];
		outputs = [{'address': self.Address, 'value': 25},\
		{'value':0, 'script_type':'null-data',\
		'script': output_script},];

		unsigned_tx = create_unsigned_tx(inputs=inputs, outputs=outputs, coin_symbol='btc-testnet',\
			api_key = self.MyToken);


		tx_signatures = make_tx_signatures(txs_to_sign=unsigned_tx['tosign'], \
			privkey_list=self.privkey, pubkey_list=self.pubkey);

		Posted_Tx = broadcast_signed_transaction(unsigned_tx=unsigned_tx, signatures=tx_signatures, pubkeys=self.pubkey,\
			coin_symbol = 'btc-testnet',api_key = self.MyToken);

		self.Tx_hash = Posted_Tx['tx']['hash'];
		return self.Tx_hash;

	def Send_Nameserver(self, NS_address, port_num):
		s = socket.socket();
		s.bind(NS_address, port_num);
		s.listen(5);
		print 'Server Listrning...'

		while True:
			conn, addr = s.accept();    # Establish connection with client.
			print 'Got connection from', addr;
			print ('Server received', repr(data));

			filename = 'Proof';
			f = open(filename, 'rb');
			l = f.read(1024);
			while (l):
				conn.send(l)
				print('Sent', repr(l));
				l = f.read(1024);
			f.close();
    		print('Done sending')
    		conn.close()



















Server = Tx_Server('zonefile');
Server.CreateMerkleTree();

#print Server.Post_MerkleRoot();

#print (Server.root);











