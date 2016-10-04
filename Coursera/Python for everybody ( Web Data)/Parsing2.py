import urllib
from BeautifulSoup import *

url = raw_input("Enter the url: ")
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

tags = soup("a")
for tag in tags:
    print tag
    print tag.contents
    print tag.attrs
