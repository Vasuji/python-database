import urllib 
#from BeautifulSoup import *
from bs4 import BeautifulSoup

url = "http://www.dr-chuck.com/"
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
tags = soup('a')
for tag in tags:
   # Look at the parts of a tag
   print 'TAG:',tag
   #print 'URL:',tag.get('href', None)
   #print 'Contents:',tag.contents[0]
   #print 'Attrs:',tag.attrs