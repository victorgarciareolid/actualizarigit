import subprocess
import os
import http.server
import socketserver
#-
class MyHandler(http.server.BaseHTTPRequestHandler):
	def do_GET(self):
		subprocess.call(['git', 'pull'])
		self.send_response(100)

def httpd (handler_class = MyHandler, server_adress =('localhost', 8080)):
	srvr = http.server.HTTPServer(server_adress, handler_class)
	srvr.serve_forever()

if __name__ == "__main__":
	httpd()