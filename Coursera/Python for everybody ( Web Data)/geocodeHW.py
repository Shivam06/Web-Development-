import urllib
import json


url = "http://python-data.dr-chuck.net/geojson?"
while True:
	address = raw_input("Enter Address :")
	url = url + urllib.urlencode({"sensor": "false", "address":address})
	print url
	info = urllib.urlopen(url).read()
	#print info
	try:
		data = json.loads(info)
	except:
		print "Address does not exist!"
		continue

	print data["results"][0]["place_id"]
	#print js
