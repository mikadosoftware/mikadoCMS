from webob import Request, Response


def simpleapp(environ, start_response):
    """ """
    status = "200 OK"
    response_headers = [('Content-type', 'text/plain'),
                        ('X-gruffalo', 'There is no such thing as a gruffalo')]
    start_response(status, response_headers)
    return ["A mouse took a stroll.",]


def mainfactory(conf, **settings):
    print settings
    return simpleapp



def getmemiddleware(config, **settings):
#factory
    def factory(app):
        return Upperware(app)
    return factory

class Upperware:
    """A generally safe way to buffer /handle middleware in wsgi - we
    yield the data returned, but nest it in output() that
    way problsmshwon in
    http://jimmyg.org/blog/2009/using-yield-statements-in-wsgi-middleware-can-be-very-harmful.html   are not found
    """

    def __init__(self, app):
        self.wrapped_app = app


    def __call__(self, environ, start_response):
        req = Request(environ)
        rsp = req.get_response(self.wrapped_app)
        try:
            del rsp.headers["Cache-Control"]
        except:
            pass

        rsp.headers.add("Cache-Control",
                        "public, max-age=-1, no-cache, must-revalidate, post-check=0, pre-check=0")

        return rsp(environ, start_response)
