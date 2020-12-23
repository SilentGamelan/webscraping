from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

from bs4 import BeautifulSoup

def loadUrl(url): 
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    except URLError as e:
        print(e)
        return None

    try:
     bs = BeautifulSoup(html, 'html.parser')
     body = bs.body
    except AttributeError as e:
        print(e)
        print('No body found')
        return None

    return bs



bs = loadUrl('http://pythonscraping.com/pages/pagex.html')

if(bs):
    print('Success')
else:
    print('Failure')


bs = loadUrl('http://pythonscraping.com/pages/page1.html')
if(bs):
    print('Success')
else:
    print('Failure')


