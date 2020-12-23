# basicExceptions.py
# simple exception handling for page/server errors

from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

from bs4 import BeautifulSoup

try: 
    html = urlopen('http://www.pythonscraping.com/pages/page1.html')
except HTTPError as e:
    print(e)
    # insert handling code here: return null, etc
except URLError as e:
    print("Error: Server Not Found")
else:
    # continue processing on sucess
    print("Success")
    bs = BeautifulSoup(html.read(), 'html.parser')




# handling non-existing elements (e.g. tags)
# Although None objects will be assigned, this can lead to 
# Attribute errors

existingTag = bs.h1
print(existingTag)

try:
    nonExistingTag = bs.h2
except AttributeError as e:
    print('Tag not found')
else:
    if(nonExistingTag == None):
        print('Tag not found')
    else:
        print(nonExistingTag)




