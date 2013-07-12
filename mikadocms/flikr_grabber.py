#!/usr/bin/env python
#! -*- coding: utf-8 -*-

### Copyright Paul Brian 2013 

# This program is licensed, without  under the terms of the
# GNU General Public License version 2 (or later).  Please see
# LICENSE.txt for details

###

"""
:author:  paul@mikadosoftware.com <Paul Brian>

Flikr.com provides a useful outlet for using photographs on
a website with minimal cost, and importantly, fuss.

1.  visit http://www.flickr.com/search/advanced/
    Search for a photo (by tag / text) but click "creative commons"
    and "commercial" use.

2. Find the right photo URL

3. run ``python flickr_grabber.py <URL>``

4. I will grab the page and make a best guess as to the original photo
   URL

5. 



"""

import requests
from bs4 import BeautifulSoup
import sys
from bookmaker import lib
import conf
from optparse import OptionParser
import logging
import webbrowser
import urllib
import os

class myError(Exception):
    pass
    
#########

            



PHOTO_STORE = "./photos"
testurl = "http://www.flickr.com/photos/comedynose/4230176889/"

def extract_photo_url(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    likelicandidate = soup.find(property='og:image')
      
    resultstr = """
    From page %s

    We have likely candidate of

    %s

    or these:

    """

    resultstr = resultstr % (url, str(likelicandidate))

    for imgtag in soup.find_all("img"):
        resultstr += str(imgtag)

    return (likelicandidate, resultstr)
        

def get_photo(url):
    """
    """
    tgt = os.path.join(PHOTO_STORE, os.path.basename(url))
    urllib.urlretrieve(url, tgt)

    
    
    
#########

def parse_args():
    parser = OptionParser()
    parser.add_option("--config", dest="confpath",
                      help="path to ini file")
    parser.add_option("--flikrpage", dest="flikrpage",
                      help="url to embedded photo")
    parser.add_option("--flikrphoto", dest="flikrphoto",
                      help="url to stadnalone photo (mutually xlusive with glikrpage")
    

    (options, args) = parser.parse_args()
    return (options, args)

def main(opts, args):
    """
    """
    if opts.confpath:
        confd = conf.get_config(opts.confpath)
        lgr.debug(pprint.pformat(confd))
    else:
        confd = {}

    if opts.flikrpage:
        likelicandidate, resultstr = extract_photo_url(opts.flikrpage)
        print likelicandidate
        print resultstr
        
    if opts.flikrphoto:
        get_photo(opts.flikrphoto)
    
if __name__ == '__main__':
    
    logging.basicConfig(level=logging.DEBUG)
    opts, args = parse_args()
        
    try:
        main(opts, args)
    except Exception, e:
        print "We can trap a lot up here"
        raise e
