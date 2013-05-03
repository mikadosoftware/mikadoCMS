

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
    print destpath
    pageob = lib.rst_to_page(srcpath)
    open(destpath, "w").write(pageob.html_body)
    
    
    
def walk_orig(rootpath):
    for root, dirs, files in os.walk(rootpath):
        for f in files:
            if f.find(".rst") >0:
                print f, " to ", 
                mvfile(os.path.join(root, f), DESTDIR)
            else:
                pass
    
        


if __name__ == '__main__':
    rootpath = sys.argv[1:][0]
    DESTDIR =  sys.argv[1:][1]
    lib.inject_config({}) ## dummy to handle deficiences in bookmkaer
    walk_orig(rootpath)