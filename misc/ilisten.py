#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class WebhookHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # Read the request body
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        # Parse JSON
        try:
            payload = json.loads(post_data.decode('utf-8'))
            print("\n=== Received Webhook ===")
            print(json.dumps(payload, indent=2))
            print("========================\n")
            
            # Send success response
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {"status": "received", "message": "Webhook processed successfully"}
            self.wfile.write(json.dumps(response).encode('utf-8'))
            
        except json.JSONDecodeError:
            self.send_response(400)
            self.end_headers()
            print("ERROR: Invalid JSON received")
    
    def log_message(self, format, *args):
        # Suppress default request logging (optional)
        pass

if __name__ == '__main__':
    server_address = ('0.0.0.0', 8080)  # Listen on all interfaces, port 8080
    httpd = HTTPServer(server_address, WebhookHandler)
    print("Webhook test server running on http://0.0.0.0:8080/v1/alert")
    print("Press Ctrl+C to stop\n")
    httpd.serve_forever()

