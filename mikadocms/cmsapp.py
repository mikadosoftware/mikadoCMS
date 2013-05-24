from flask import Flask, make_response, request, abort
from webob import Request, Response
from flask import send_from_directory
import os
import pprint
from waitress import serve
import conf
from optparse import OptionParser
import logging
logging.basicConfig(level=logging.DEBUG)

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


    routing:
    every path is supplied to cms() function.
    This means that the blog must serve off a different port and
    be routed with a different 
    """
    app = Flask(name)
    app.config.update(confd, static_folder="foo")

    app.add_url_rule("/", view_func=index)
    app.add_url_rule("/assets/<path:filename>",
                     view_func=servestatic)#should use wsgi middleware or nginx
    app.add_url_rule("/<path:path>", view_func=cms)
#    app.add_url_rule("/blog/<path:path>", view_func=blog)    
    return app

def servestatic(filename):
    """
    """
    print "serving ", filename
    return send_from_directory(confd['cms']['static_path'],
                                       filename)

def getchunks(chunkdir):
    """
    given a dir where there are text files we want to use as
    chunks of HTML, return a dict with those txt files as strings
    """
    allchunks = {}
    files = [f for f in os.listdir(chunkdir)
             if os.path.splitext(f)[1] == '.tmpl']
    logging.debug(files)
    for f in files:
        key = f.split(".")[0] #foo.tmpl -> foo
        fpath = os.path.join(chunkdir, f)  #foo.tmpl -> /tmp/foo.tmpl
        allchunks[key] = open(fpath).read()
    return allchunks
    
    
def index():
    t = get_tmpl(tmpltype="index")
    return t % allchunks


    
def favicon():
    return send_from_directory(app.config['cms']['docroot'],
                              'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')

def get_tmpl(tmpltype="internal"):
    """
    return either internal or index page tmpl.
    """
    if tmpltype == "index":
        tmpl = "index.tmpl"
    elif tmpltype == "internal":
        tmpl = "internal.tmpl"
    else:
        abort(404)
    
    return open(os.path.join(app.config['cms']['tmplroot'], tmpl)).read()

    
def get_pagetxt(path_requested):
    """ """
    txt = open(path_requested).read()
    return txt

    


def cms(path):
    
    path_requested = os.path.join(app.config['cms']['docroot'], path) + ".htm"
    if path_requested.find("/.htm") != -1:
        #horrible hack
        path_requested = path_requested.replace("/.htm", "/index.htm")
        
    if not os.path.isfile(path_requested):
        print "aborting", path_requested
        abort(404)
        
    t = get_tmpl(tmpltype="internal")
    body = get_pagetxt(path_requested)
    allchunks.update( {"itemcontent": body})
    print allchunks.keys()
    print allchunks['header']
    return t % allchunks

  
def blog(path):
    return "helo" + str(path)

def parse_args():
    parser = OptionParser()
    parser.add_option("--config", dest="confpath",
                      help="path to ini file")
    (options, args) = parser.parse_args()
    return (options, args)    


if __name__ == "__main__":

    lgr = logging.getLogger("mikadoCMS")
    logging.basicConfig(level=logging.DEBUG)
    
    opts, args = parse_args()
    confd = conf.get_config(opts.confpath)
    lgr.debug(pprint.pformat(confd))

    ##chunks
    allchunks = getchunks(confd['cms']['chunkdir'])
    print allchunks.keys()
    
    app = make_app("mikado", confd)
    serve(app.wsgi_app,host="0.0.0.0",port=8000)            
    