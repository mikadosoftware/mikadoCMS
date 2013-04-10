from flask import Flask, make_response, request, abort
from webob import Request, Response
from flask import send_from_directory
import os
import pprint

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
* see if I can link visitor_ud to landing page

useage:

* run this file (behind nginx etc)
* this will hopefully allow me to serve HTML fragments
  from doccache - these can be generated rst style from
  REST
* Then the rest of the page is built
* for now its not too much 


'''




def make_app(name, confd):
    """
    an attempt at an app_factory
    """
    open("/tmp/log", "a").write("APPFACTORYCALLED\n")
    app = Flask(name, static_folder=confd["DOCROOT"])
    app.config.update(confd)
    app.add_url_rule("/hello", view_func=hello)
    app.add_url_rule("/favicon", view_func=favicon)
    app.add_url_rule("/cms/<path>", view_func=cms)        
    
    return app
    

def hello():
    return "hello"


def favicon():
    return send_from_directory(app.config['DOCROOT'],
                              'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')

def get_tmpl():
    return open(os.path.join(app.config['TMPLROOT'], "index.tmpl")).read()

def get_pagetxt(path_requested):
    """ """
    txt = open(path_requested).read()
    return txt


def cms(path):
    path_requested = os.path.join(app.config['DOCROOT'], path) + ".htm"
    if not os.path.isfile(path_requested): abort(404)
    t = get_tmpl()
    body = get_pagetxt(path_requested)

    return t % {"body_filler": body}

from waitress import serve


if __name__ == "__main__":
    #sys.argv[1:][0]
    conf={"DOCROOT": '/usr/home/pbrian/src/public/mikadoCMS/mikadocms/docroot',
          "TMPLROOT": '/usr/home/pbrian/src/public/mikadoCMS/mikadocms/tmplroot',
    }
    
    app = make_app("mikado", conf)
    serve(app.wsgi_app,host="0.0.0.0",port=8000)            
    