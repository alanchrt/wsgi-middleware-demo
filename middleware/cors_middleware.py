def cors_middleware(app):
    print "CORS middleware applied."

    def cors_enabled_application(environ, start_response):

        def cors_allowed_response(status, response_headers, exc_info=None):
            """This wraps the start_response behavior to add some headers."""
            response_headers.extend([('Access-Control-Allow-Origin', '*')])
            return start_response(status, response_headers, exc_info)

        return app(environ, cors_allowed_response)

    return cors_enabled_application
