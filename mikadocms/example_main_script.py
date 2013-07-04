from bookmaker import lib
import conf
from optparse import OptionParser
import logging

class myError(Exception):
    pass
    
#########

def main():
    """
    """
    

#########

def parse_args():
    parser = OptionParser()
    parser.add_option("--config", dest="confpath",
                      help="path to ini file")
    (options, args) = parser.parse_args()
    return (options, args)
    
if __name__ == '__main__':
    
    logging.basicConfig(level=logging.DEBUG)
    opts, args = parse_args()
    confd = conf.get_config(opts.confpath)
    lgr.debug(pprint.pformat(confd))
    try:
        main()
    except Exception, e:
        print "We can trap a lot up here"
        raise e