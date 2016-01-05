import sys
import socket
import io
import SimpleHTTPServer
import SocketServer

list = []

list.append(1112)
i=1
while True:
	if i>5:
		i=0
		break
	else:
		list.append(list[i-1]+1)
		print list[i-1]
		i=i+1

class myHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
		
	def do_GET(self):
		global i
		self.send_response(303)
		new_path = 'http://127.0.0.1:%s/'% (list[i])
		print new_path	
		i = i+1
		if i>5:
			i=0
		self.send_header('Location', new_path)
		self.end_headers()

PORT = 1120
handler = SocketServer.TCPServer(("10.151.34.174", PORT), myHandler)
print "serving at port 1212"
handler.serve_forever()
