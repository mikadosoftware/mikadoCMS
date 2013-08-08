from flask import Flask, make_response, request, abort
from webob import Request, Response
from flask import send_from_directory
import os
import pprint
from waitress import serve
import conf
from optparse import OptionParser
import logging
from bookmaker import lib

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




WHy so much HTML in the scafoolding
- I am using bootstrap - so we need to use HTML scaffolding.
This is fine, and the chunks approach means I can compose a HTML page fairly well, and as
I get to know more bootstrap, the chunks will get finer grained, heading towards a DSL
to describe a template.  That might be a bit advanced but there is no reason this CMS cannot
sensibly support a numerous templated styles plus simple ReSt based content.

Notes on mixins in Less
http://ruby.bvision.com/blog/please-stop-embedding-bootstrap-classes-in-your-html
or copy compress.rb idea
http://www.sitepoint.com/css-frameworks-semantic-class-names/



allchunks is magically in global...
I dont like this - it needs to be in wsgi flow.
'''

import contents_maker

class CMSError(Exception):
    pass

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
    return app

def servestatic(filename):
    """
    """
    lgr.info("serving %s" % filename)
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
        allchunks[key] = open(fpath).read().decode('utf-8')
    ##header needs the title and meta details of a page formatted in
    return allchunks
    
def index():
    return cms("/")


    
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

    
def get_page_from_rst(srcText):
    """
    from a rest file generate a bookmaker pageobj
    """
    lgr.debug("Converting a text string %s" % srcText[:10])
    pageobj = lib.rst_to_page(srcText)
    return pageobj
    
def read_srcfile(path_requested):
    """
    """
    if not os.path.isfile(path_requested):
        lgr.error("aborting %s" % path_requested)
        abort(404)
    else:
        rst_txt = unicode(open(path_requested).read(),'utf8')
        ### lib deamnds all text as unicode
    return rst_txt

def cms(path):
    """
    This is essentially a URL route dispatcher, that is not designed like one...

    I am special casing a lot of things...
    
    """
    lgr.info("Entered CMS with path %s" % path)
    
    if path.strip() == '/':
        t = get_tmpl(tmpltype="index")
        path_requested = os.path.join(confd['cms']['rstroot'], "index.rst")
        lgr.info("looking for %s after %s" % (path_requested,
                                              confd['cms']['rstroot']))
        rst_txt = read_srcfile(path_requested)
        
    elif path.strip() == 'contents':
        ###
        lgr.debug("Called for /contents")
        t = get_tmpl(tmpltype="internal")
        rst_txt = contents_maker.gather_contents_as_rst(confd['cms']['rstroot'])
        
    elif path.strip()[-1:] == "/":
        ##directory
        t = get_tmpl(tmpltype="internal")
        #horrible hack - if path ends in / then get the index of the dir...
        path_requested = os.path.join(confd['cms']['rstroot'],
                                      path, "index.rst")
        lgr.info("Ended in slash looking for %s after %s" % (
                                              path_requested,
                                              confd['cms']['rstroot']))
        rst_txt = read_srcfile(path_requested)
    else:
        t = get_tmpl(tmpltype="internal")
        path_requested = os.path.join(confd['cms']['rstroot'],
                                      path + ".rst")
        lgr.info("looking for %s after %s" % (path_requested,
                                              confd['cms']['rstroot']))
        rst_txt = read_srcfile(path_requested)
        
        
    ##chunks
    allchunks = getchunks(confd['cms']['chunkdir'])
    ### at this point we know if its an internal page,
    ### we know the path_requested, we know the various chunks that
    ### will make the final page
        
    pg = get_page_from_rst(rst_txt)
    ## OK - now the page info is in allchunks, we can write the page
    ## info into the title field in header.
    ## I should avoid the obj->dict issue by using jinja2
    allchunks['header'] = allchunks['header'] % {"page_title": pg.title,
                                                 "page_subtitle": pg.subtitle}
    allchunks["page_html_body"] = pg.html_body
    return t % allchunks


def parse_args():
    parser = OptionParser()
    parser.add_option("--config", dest="confpath",
                      help="path to ini file")
    (options, args) = parser.parse_args()
    return (options, args)    


if __name__ == "__main__":


    ## only confd is allowed to be global to the module,
    ## everything else gets passed around.
    
    lgr = logging.getLogger("mikadoCMS")
    logging.basicConfig(level=logging.DEBUG, file="./mikado.log")
    lib.inject_config({}) ## dummy to handle deficiences in bookmkaer
    
    opts, args = parse_args()
    confd = conf.get_config(opts.confpath)

    app = make_app("mikadocms", confd)
    serve(app.wsgi_app,host="0.0.0.0",port=int(confd['cms']['port']))            
    