from pprint import pprint
class HTTPRequest(object):
    '''Only parses wellformed HTTP1.1 requests (should be made by browsre anyway)'''
    def __init__(self, tcp_content):
        print(tcp_content)
        request, message = tcp_content.split(b'\r\n\r\n')
        request_parts = request.split(b'\r\n')
        request_line = request_parts[0]
        headers = request_parts[1:]
        self.parse_request_line(request_line)
        self.parse_headers(headers)
        self.host = self.headers[b'Host']
        self.url = self.host + self.path

    def parse_request_line(self, request_line):
        parts = request_line.split(b' ')
        self.method = parts[0]
        self.path = parts[1]
    
    def parse_headers(self, headers):
        self.headers = {}
        for header in headers:
            key, value = header.split(b': ')
            self.headers[key] = value