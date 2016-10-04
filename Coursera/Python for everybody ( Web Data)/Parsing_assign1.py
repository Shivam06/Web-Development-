import urllib
from BeautifulSoup import *
import re

url = raw_input("Enter : ")
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
tags = soup("span")

sum = 0
sum2 = 0
print html
#for tag in tags:
#    sum += int(re.findall(">([0-9]*)<",str(tag))[0])
#    sum2 += int(tag.contents[0])
#print sum
print tags
