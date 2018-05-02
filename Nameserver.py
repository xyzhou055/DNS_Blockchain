#This class defines the nameserver which answer the DNS request from the client

import socket
import ast

class nameserver:

	def DNS_response(self):
		s = socket.socket();
		s.bind(('127.0.0.1', 5554));

		s.listen(5);
		print 'Server Listening...'

		while True:
			conn, addr = s.accept();
			print 'Got connection from', addr;
			data = conn.recv(1024);
			print('Server received', repr(data));
			for line in open('Proof'):
				if data in line:
					conn.send(line);
					break;
			

			print('Done sending')
			conn.close();


N = nameserver();
N.DNS_response();