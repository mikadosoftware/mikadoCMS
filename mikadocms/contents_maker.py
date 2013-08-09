

### convert .rst files into htm partials and put in docroot (pre-seeding effectively)
### steal stuff from bookmaker

from bookmaker import lib
import os, sys
import logging
lgr = logging.getLogger("mikadoCMS")

def contententry(pageobj):
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
    return "* `%s <%s>`_\n" % (title, relative_uri)
    
             
def gather_contents_as_rst(rootpath):
    contents = []
    for root, dirs, files in os.walk(rootpath):
        for f in files:
            ##hacky equivalent to .rst$
            if f.find(".rst") == len(f)-4:
                if f == "index.rst":continue
                srcpath = os.path.join(root, f)
                if not os.path.isfile(srcpath): continue ### emacs cruft often fails here. 
                lgr.debug("valid file: %s at srcpath %s" % (f,srcpath))
                pageobj = lib.file_to_page(srcpath)
                contents.append(contententry(pageobj))
            else:
                lgr.debug("invalid file %s" % f)
    return "\n".join(contents)
    
if __name__ == '__main__':

    ## create package of constants to pass around.
    origpath = sys.argv[1:][0]
    print walk_orig(origpath)
    