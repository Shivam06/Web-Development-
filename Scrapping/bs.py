from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc,"html.parser")
print soup.prettify()  # To change it in clean HTML form
print soup.title.string # string return the text stored etween the tags- NavigableString
print soup.title.parent.name 
print soup.a        # Only gives one "a" tag. So use it if there is only one tag in DOC. Like head, title etc
print soup.a.string 
print soup.find_all("a") # Returns a list of all the required tags
print soup.find(id = "link3") # there is only one tag corresponding to a particular id. To find it.

for link in soup.find_all("a"):
	print link["href"]   # or print link.get("href")

print soup.get_text()  # return all the text of the page.


