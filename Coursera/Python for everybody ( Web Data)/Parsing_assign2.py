import urllib
from BeautifulSoup import *

url = raw_input("Enter the url : ")
num = raw_input("Enter the number of link you want to parse. ")
count = raw_input("Enter how many times you want to crawl. ")
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

tags = soup("a")

for _ in range(int(count)):
    tag = tags[int(num) - 1]
    print tag.contents[0]
    url = tag.get("href",None)
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup("a")
    
