import urllib
import os
from BeautifulSoup import *

url = raw_input("Enter the url you want too parse :")

html = urllib.urlopen(url)
soup = BeautifulSoup(html)
tags = soup('a')
#for tag in tags:
#    print tag.get('href',None)
print tags
