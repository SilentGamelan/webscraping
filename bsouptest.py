from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page1.html')

# create the BeautifulSoup object and read the target into the object
# 
#bs = BeautifulSoup(html.read(), 'html.parser')

# NB - this will only return the first instance of an h1 element
#print(bs.h1)

# It's possible to access the file object directly without .read()
# I'm not sure if this makes any difference or why you'd do it
html = urlopen('http://www.pythonscraping.com/pages/page1.html')
bsfile = BeautifulSoup(html, 'html.parser')
print(bsfile.html)


# The bs object can be supplied different parsers after the text object to parse

# These require separate downloads, are slower, but are more capable
# with malformed HTML/XML files for instance
# bs = BeautifulSoul(html.read, 'lxmi')

# bs = BeautifulSoul(html.read, 'html5lib')
