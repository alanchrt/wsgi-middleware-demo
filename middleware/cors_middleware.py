def cors_middleware(app):
    print "CORS middleware applied."

    def cors_enabled_application(environ, start_response):
        print "Do some stuff here."
        return app(environ, start_response)

    return cors_enabled_application
