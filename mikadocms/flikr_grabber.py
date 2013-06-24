import requests
from bs4 import BeautifulSoup
import sys

def main(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    likelicandidate = soup.find(property='og:image')
      
    resultstr = """
    From page %s

    We have likely candidate of

    %s

    or these:

    """

    print resultstr  % (url, str(likelicandidate))

    for imgtag in soup.find_all("img"):
        print imgtag #imgtag['src']

    return likelicandidate
        
if __name__ == '__main__':
    url = sys.argv[1:][0]
    testurl = "http://www.flickr.com/photos/comedynose/4230176889/"
    li = main(url)
    