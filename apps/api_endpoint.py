import json


def application(environ, start_response):
    """The web application."""
    # This is the content of the response
    response_body = json.dumps({
        'success': True
    })

    # Set up the response status and headers
    status = '200 OK'
    response_headers = [
        ('Content-Type', 'application/json'),
        ('Content-Length', str(len(response_body))),
    ]

    # Deliver the response back to the server
    start_response(status, response_headers)
    return [response_body]
