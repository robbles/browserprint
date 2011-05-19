import vim
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import webbrowser

head_template = """
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=%(encoding)s">
</head>
<body>
<pre style="font-family: %(font)s">
"""

tail_template = """
</pre>
</body>
</html>
"""

ff = vim.eval('&ff').split(',')[0]
eol = {
    'unix': '\n',
    'dos':'\r\n',
    'mac':'\r'
}[ff]

def load_html(generator):
    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.wfile.write(head_template % {
                'encoding': vim.eval('&encoding'),
                'font': vim.eval('&gfn').split(':')[0]
            })
            self.wfile.writelines(generator)
            self.wfile.write(tail_template)

    server = HTTPServer(('127.0.0.1', 0), RequestHandler)
    webbrowser.open_new('http://127.0.0.1:%d' % server.server_port)
    server.handle_request()

def load_buffer(buf):
    load_html((line + eol for line in buf))

