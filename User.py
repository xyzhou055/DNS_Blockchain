#This is the implementation of the user who will fetch the transaction from 
#the blockchain and check the proof from the nameserver.
from blockcypher import get_transaction_details
import bisect
from merkletools import MerkleTools
import socket
import ast
import hashlib

class DNS_User:

	zonefile=[];
	NS_addr='';
	port_num=0;
	root = '';

	def __init__(self, addr, num):
		self.NS_addr = addr;
		self.port_num = num;

	def DNS_Request(self, hostname):
		s = socket.socket();
		s.connect((self.NS_addr, self.port_num));
		s.send(hostname);

		print 'receiving data...'
		data = s.recv(1024)

		if not data:
			print 'No zonefile found!'
			return False;

		self.zonefile = ast.literal_eval(data); 
		print self.zonefile;
		s.close();
		return True;


	def __Fetch_Merkle_root(self):
		if not self.zonefile:
			print 'No transaction found!'
			return False;

		Tx_hash = self.zonefile['Tx_hash']
		Tx = get_transaction_details(Tx_hash, coin_symbol='btc-testnet');
		for item in Tx['outputs']:
			for key in item:
				if(key == 'data_string'):
					#bisect.insort_left(self.Tx_list, (Tx['block_height'], item[key]));
					self.root = item[key];
					print self.root;
					return True;

		return False;

	def verify(self):
		if not self.zonefile:
			return False;
		self.__Fetch_Merkle_root();
		DNS_record = self.zonefile['record'];
		target_hash = hashlib.sha256(DNS_record).hexdigest();
		mt = MerkleTools();
		return mt.validate_proof(self.zonefile['proof'], target_hash, self.root);
			



User1 = DNS_User('127.0.0.1', 5554);
User1.DNS_Request('google.com');
print User1.verify();
#User1.Fetch_Merkle_root('8da43ffbca738ac4d2fec0d45f9f5db06c1bc3a49b3ef0dcd48bff0a4d7589a8');
#User1.Fetch_Merkle_root('28a92bed93e18a5cedaee24f515ef38b800805d1b20d2d2342215cbb22370393');
#User1.Fetch_Merkle_root('4e22d952f2461823111d18eaf70e8b4928c0a9615bf326509c2983d0619a1fb7');
#print User1.get_root_list();
