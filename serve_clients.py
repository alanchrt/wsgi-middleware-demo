import logging
import time

from threading import Thread
from wsgiref.simple_server import make_server

from apps.client_button import application

log = logging.getLogger()


def run_server(port):
    """Serve the client app on the specified port."""
    print "Serving client on port {0}...".format(port)
    httpd = make_server('localhost', port, application)
    httpd.serve_forever()

# Run three different wsgi servers on different ports
for port in xrange(9000, 9002 + 1):
    server = Thread(target=run_server, args=[port])
    server.daemon = True
    server.start()
    time.sleep(0.5)

# Wait until we kill the server
while True:
    time.sleep(0.5)
