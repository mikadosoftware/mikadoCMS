

### convert .rst files into htm partials and put in docroot (pre-seeding effectively)
### steal stuff from bookmaker

from bookmaker import lib
import os, sys

def mvfile(srcpath, destdir):
    """
    """
    cutpoint = srcpath.find("/orig/")
    relative_path = srcpath[cutpoint + len("/orig/"):]
    destpath = os.path.join(destdir, relative_path).replace(".rst", ".htm")
    pageob = lib.rst_to_page(srcpath)
    open(destpath, "w").write(pageob.html_body.encode("utf8"))
    return destpath    
    
    
    
def walk_orig(rootpath):
    for root, dirs, files in os.walk(rootpath):
        for f in files:
            ##hacky equivalent to .rst$
            if f.find(".rst") == len(f)-4:
                print f, " -> ", 
                destpath = mvfile(os.path.join(root, f), DESTDIR)
                print destpath
            else:
                pass
    
if __name__ == '__main__':
    configpath = sys.argv[1:][0]
    import conf
    confd = conf.get_config(configpath)
    DESTDIR = confd['cms']['docroot']
    lib.inject_config({}) ## dummy to handle deficiences in bookmkaer
    walk_orig(confd['cms']['rstroot'])