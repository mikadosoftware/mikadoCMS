#!/usr/bin/env python
#! -*- coding: utf-8 -*-

### Copyright Paul Brian 2013 

# This program is licensed, without  under the terms of the
# GNU General Public License version 2 (or later).  Please see
# LICENSE.txt for details

###

"""
:author:  paul@mikadosoftware.com <Paul Brian>

This is a initial attempt at extracting meaningful data from tender documents
on the web, for the OSSinGov Project.

1. We visit the tender portal site (usually run by due-north.com).
2. we login, and search for tenders listed as category SOftware or having software in the body
3. we download the html to local disk
4. we run this program over it, extracting the main points and storing
   in ... json?
5. We can then further categorise the data and try and get some meaning.

"""

from bs4 import BeautifulSoup as bsoup
import sys, os
import json

def simple_parse(souptxt):
    """
    
    given txt (from bsoup.get_text()), extract main contract points
    
    """

    pkts = {"contractid": ("Contract:", "Main Contract Detail"),
            "buyer":      ("Buyer:", "Title:"),
            "title":      ("Title:", "Category/Categories:"),
            "summary":    ("Summary:", "Contact:"),
            "startdate":  ("contract start date:", "Estimated contract end date:")
    }
    
    output = {}
    for pkt in pkts:
        stidx = souptxt.find(pkts[pkt][0])+len(pkts[pkt][0])
        endidx = souptxt.find(pkts[pkt][1])        
        slice_ = souptxt[stidx:endidx]
        output[pkt] = slice_.strip()

    return output

def traversedir(fldr):
    """
    """
    capture = []
    files = [f for f in os.listdir(fldr) if os.path.isfile(f)
                     and f.find(".html")>0]
    for f in files:
        
        html = open(f).read()
        souptxt = bsoup(html).get_text()
        o = simple_parse(souptxt)
        capture.append(o)
    return capture

if __name__ == '__main__':
    fldr = sys.argv[1:][0]
    capture = traversedir(fldr)
    fo = open("foo.json", "w")
    fo.write(json.dumps(capture, indent=4))
    fo.close()
    
    