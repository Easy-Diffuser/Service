import _socket
import os
import http.server
import socketserver
import uuid
import run
import json
import easy_diffuser


global model

class HTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
            
    def do_POST(self):
        content_len = int(self.headers.get('Content-Length'))
        post_body = self.rfile.read(content_len)
        
        body = post_body.decode('utf-8')
        option, image = body[:3], body[3:]
        model.run_link(image)
        if (option == "img"):
            model.img2img_(image)
        reply = {
            'pos' : model.pos.split(),
            'neg' : model.neg.split()
        }
        
        reply_body = json.dumps(reply)

        self.send_response(201, 'Created')
        self.end_headers()
        self.wfile.write(reply_body.encode('utf-8'))

    def do_GET(self):
        self.send_response(404, 'Not Found')
        self.end_headers()
        self.wfile.write(b'')
        
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        http.server.SimpleHTTPRequestHandler.end_headers(self)

if __name__ == '__main__':
    model=easy_diffuser.start()
    
    print("Server Run")
    PORT = 5998
    
    server = http.server.HTTPServer(('', PORT), HTTPRequestHandler)
    
    server.serve_forever()