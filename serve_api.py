from wsgiref.simple_server import make_server

from apps.api_endpoint import application
from middleware.cors_middleware import cors_middleware

# Run a wsgi server to serve the app
print "Serving api on port 8000..."
wrapped_application = cors_middleware(
    application, whitelist=['http://localhost:9000', 'http://localhost:9001'])
httpd = make_server('localhost', 8000, wrapped_application)
httpd.serve_forever()
