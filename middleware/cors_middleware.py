def validate_origin(origin, whitelist):
    return origin and origin in whitelist


def cors_middleware(app):
    print "CORS middleware applied."

    whitelist = ['http://localhost:9000', 'http://localhost:9001']

    def cors_enabled_application(environ, start_response):

        origin = environ.get('HTTP_ORIGIN')

        def cors_allowed_response(status, response_headers, exc_info=None):
            """This wraps the start_response behavior to add some headers."""
            response_headers.extend([('Access-Control-Allow-Origin', origin)])
            return start_response(status, response_headers, exc_info)

        if validate_origin(origin, whitelist):
            return app(environ, cors_allowed_response)
        else:
            return app(environ, start_response)

    return cors_enabled_application
