from wsgiref.simple_server import make_server
from webserver import application

httpd = make_server('', 3000, application)
print('Server HTTP on port 3000...')

httpd.serve_forever()
