import urllib

file = open("Profanity Checker Document.txt","r")
doc = file.read()
list =  doc.split() 
for element in list:
    if "true" in urllib.urlopen("http://www.wdylike.appspot.com/?q="+element).read():
        print str(element) + " is Curse Word. Kindly change it appropriately."
