import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.send('GET http://open.umich.edu/sites/default/files/8202/code/romeo.txt HTTP/1.0\n\n')

while True:
	data = mysock.recv(512)
	if ( len(data) < 1 ) :
		break
	print data;
	
mysock.close()		
