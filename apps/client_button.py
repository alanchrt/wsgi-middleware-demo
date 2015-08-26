def application(environ, start_response):
    """Serve the button HTML."""
    with open('apps/client_button.html') as f:
        response_body = f.read()
    status = '200 OK'
    response_headers = [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body))),
    ]
    start_response(status, response_headers)
    return [response_body]
