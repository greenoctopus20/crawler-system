from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import urlparse, parse_qs
from extractor import find_element_by_xpath, get_html_from_url, read_json_file

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        post_params = parse_qs(post_data.decode('utf-8'))
        
        if 'file_path' in post_params:
            file_path = post_params['file_path'][0]
            json_data = read_json_file(file_path)
            domain = json_data['domain']
            html = get_html_from_url(domain)
            
            response = ""
            for article in json_data['articles_XPath']:
                title = find_element_by_xpath(html, article['title'])
                body = find_element_by_xpath(html, article['body'])
                author = find_element_by_xpath(html, article['author'])
                date = find_element_by_xpath(html, article['Date'])

                if title and body:
                    formatted_article = f"Title: {title}\nAuthor: {author}\nDate: {date}\n\n{body}\n"
                    response += formatted_article

            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(response.encode('utf-8'))
        else:
            self.send_response(400)
            self.end_headers()

def run_server():
    port = 400
    server_address = ('', port)
    httpd = HTTPServer(server_address, RequestHandler)
    print(f"Listening on port {port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()
