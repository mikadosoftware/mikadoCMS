from bookmaker import lib
import conf
from optparse import OptionParser
import logging
import os
import pprint


"""
usage: python -i play_pageobj.py --tgtpath=data/mikadosoftware.com/orig/services/index.rst

"""

class myError(Exception):
    pass
    
#########

def main(tgtpath):
    """
    """
    srcpath = tgtpath
    pageob = lib.rst_to_page(srcpath)
    return pageob

#########

def parse_args():
    parser = OptionParser()
    parser.add_option("--tgtpath", dest="tgtpath",
                      help="path to a rest file")
    (options, args) = parser.parse_args()
    return (options, args)
    
if __name__ == '__main__':
    
    logging.basicConfig(level=logging.DEBUG)
    lgr = logging.getLogger(__name__)
    
    opts, args = parse_args()
    try:
        pageob = main(opts.tgtpath)
    except Exception, e:
        print "We can trap a lot up here"
        raise e
