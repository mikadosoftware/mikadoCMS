from flask import Flask, make_response, request, abort
from webob import Request, Response
from flask import send_from_directory
import os
import pprint

app = Flask("mikadocms", static_folder="docroot")
THISDIR = os.path.abspath(os.path.dirname(__file__))
DOCROOT = os.path.join(THISDIR, 'docroot')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(DOCROOT,
                              'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')
'''
This is supposed to be the heart of CMS
maybe I want my own route mapper???
Maybe I just want to grab the requested path and return a
text file found at that <docroot>/path/requested
yes

Then we build up the response from there.
Roughly speaking the response body is built by the web app
The headers are province of the wsgi middleware.
This is not a hard and fast rule.



Basics so far:
We have static files served out of docroot
We have all other routes being intercepted and served by :function:`cms`

This looks for a ".htm" (!) file in the docroot (could be anywhere)
the htm is located at requested url location

    example.com/path/foo

    will look for ~/docroot/path/foo.htm

THis is then put into the hero unit via string fomratting.

Next steps:

* gunicorn and nginix
* deployment scripts
* produce material via rst into the .htm file
* adjust the bootstrap html to suit
* launch

* google anlytics
* ability to store cookies and give each browser a unique uuid
* see if I can link visitor_uuid to landing page


'''

def get_tmpl():
    return open(os.path.join(THISDIR, "index.tmpl")).read()

def get_pagetxt(path_requested):
    """ """
    txt = open(path_requested).read()
    return txt

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def cms(path):
    path_requested = os.path.join(DOCROOT, path) + ".htm"
    if not os.path.isfile(path_requested): abort(404)
    t = get_tmpl()
    body = get_pagetxt(path_requested)

    return t % {"body_filler": body}

#app.wsgi_app = Upperware(app.wsgi_app)

#app = Upperware(_app)
## basically we do nothing expect assume /static is served


if __name__ == "__main__":
    app.run(debug=True, port=5001)
