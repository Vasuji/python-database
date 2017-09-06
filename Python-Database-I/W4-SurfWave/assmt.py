# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
#from BeautifulSoup import*
from bs4 import BeautifulSoup

url = "http://python-data.dr-chuck.net/comments_42.html"
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)


tags = soup('a')
for tag in tags:
   # Look at the parts of a tag
   print 'TAG:',tag
   print 'URL:',tag.get('href', None)
   print 'Contents:',tag.contents[0]
   print 'Attrs:',tag.attrs
