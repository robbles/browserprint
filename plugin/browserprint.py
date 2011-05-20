import vim
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import webbrowser
from cgi import escape as escape_html
import re

head_template = """
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=%(encoding)s">
</head>
<body>
<pre style="font-family: %(font_name)s; font-size: %(font_size)spx">
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

def get_font():
    """ 
    Return a tuple of (font name, font size) falling back to default of
    ('monospace', 12) if necessary.
    """
    font = vim.eval('&gfn')
    if re.match('.*:h\d+$', font):
        return re.match('(.*):h(\d+)$', font).groups()
    elif re.match('.* \d+$', font):
        return re.match('(.*) (\d+)$', font).groups()
    else:
        return (font, '12') if font else ('monospace', '12')


def load_html(generator):
    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            font_name, font_size = get_font()
            self.wfile.write(head_template % {
                'encoding': vim.eval('&encoding'),
                'font_name': font_name,
                'font_size': font_size
            })
            self.wfile.writelines(generator)
            self.wfile.write(tail_template)

    server = HTTPServer(('127.0.0.1', 0), RequestHandler)
    webbrowser.open_new('http://127.0.0.1:%d' % server.server_port)
    server.handle_request()

def load_buffer(buf):
    load_html((escape_html(line) + eol for line in buf))

