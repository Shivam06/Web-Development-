import xml.etree.ElementTree as ET
import urllib

url = raw_input("Enter the URL : ")
xml_string = urllib.urlopen(url).read()

tree = ET.fromstring(xml_string)
lst = tree.findall('.//count')

sum = 0
for item in lst:
    sum+= int(item.text)

print sum