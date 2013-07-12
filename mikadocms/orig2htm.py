

### convert .rst files into htm partials and put in docroot (pre-seeding effectively)
### steal stuff from bookmaker

from bookmaker import lib
import os, sys


def contents(pageobj):
    """
    """
    cutpoint = pageobj.src.find("/orig/")
    relative_src_path = pageobj.src[cutpoint + len("/orig/"):]
    relative_tgt_path = relative_src_path.replace(".rst", ".htm")
    relative_uri = relative_src_path.replace(".rst", "")
    
    print "    from %s got %s" % (pageobj.src,
                              relative_uri)
    


    #get page title
    if pageobj.title == '':
        title = os.path.splitext(os.path.basename(pageobj.src))[0]
    else:
        title = pageobj.title


    ##
    fo = open(CONTENTSPATH, "a")
    fo.write("* `%s <%s>`_\n" % (title, relative_uri))
    fo.close()

             
def mvfile(srcpath, destdir):
    """
    """
    cutpoint = srcpath.find("/orig/")
    relative_path = srcpath[cutpoint + len("/orig/"):]
    destpath = os.path.join(destdir, relative_path).replace(".rst", ".htm")
    pageobj = lib.rst_to_page(srcpath)
    contents(pageobj)
    open(destpath, "w").write(pageobj.html_body.encode("utf8"))
    return destpath    
    
    
    
def walk_orig(rootpath):
    for root, dirs, files in os.walk(rootpath):
        for f in files:
            ##hacky equivalent to .rst$
            if f.find(".rst") == len(f)-4:
                print f, " -> "
                destpath = mvfile(os.path.join(root, f), DESTDIR)
                print "   ", destpath
            else:
                pass
    
if __name__ == '__main__':

    ## create package of constants to pass around.
    configpath = sys.argv[1:][0]
    import conf
    confd = conf.get_config(configpath)

    CONTENTSPATH = os.path.join(confd['cms']['rstroot'], "contents.rst")
    DESTDIR = confd['cms']['docroot']
    open(CONTENTSPATH,"w") #delete/
    lib.inject_config({}) ## dummy to handle deficiences in bookmkaer
    walk_orig(confd['cms']['rstroot'])
    mvfile(CONTENTSPATH, DESTDIR)