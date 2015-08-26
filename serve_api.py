from wsgiref.simple_server import make_server

from apps.api_endpoint import application

# Run a wsgi server to serve the app
print "Serving api on port 8000..."
httpd = make_server('localhost', 8000, application)
httpd.serve_forever()
