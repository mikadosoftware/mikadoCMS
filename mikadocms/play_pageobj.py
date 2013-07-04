from bookmaker import lib
import conf
from optparse import OptionParser
import logging
import os
import pprint

class myError(Exception):
    pass
    
#########

def main(confd):
    """
    """
    srcpath = os.path.join(confd['cms']['rstroot'], "orig", "about.rst")
    pageob = lib.rst_to_page(srcpath)
    return pageob

#########

def parse_args():
    parser = OptionParser()
    parser.add_option("--config", dest="confpath",
                      help="path to ini file")
    (options, args) = parser.parse_args()
    return (options, args)
    
if __name__ == '__main__':
    
    logging.basicConfig(level=logging.DEBUG)
    lgr = logging.getLogger(__name__)
    
    opts, args = parse_args()
    confd = conf.get_config(opts.confpath)
    lgr.debug(pprint.pformat(confd))
    try:
        pageob = main(confd)
    except Exception, e:
        print "We can trap a lot up here"
        raise e