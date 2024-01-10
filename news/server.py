from http.server import SimpleHTTPRequestHandler, HTTPServer

# Define the port on which to run the server
PORT = 9000

class CustomHandler(SimpleHTTPRequestHandler):
    # Override the default do_GET method to serve files from the 'articles' folder
    def do_GET(self):
        # Set the path to the 'articles' directory
        self.directory = 'articles/'
        return SimpleHTTPRequestHandler.do_GET(self)

# Create an HTTP server with the custom handler
httpd = HTTPServer(('0.0.0.0', PORT), CustomHandler)

print(f"Server running on http://localhost:{PORT}")
# Start the server
httpd.serve_forever()
