import json
import urllib2

url = raw_input("Enter location: ")
info = urllib2.urlopen(url).read()
data = json.loads(info)
comments = data["comments"]

sum = 0
for i in range(len(comments)):
	sum += int(comments[i]["count"])

print sum