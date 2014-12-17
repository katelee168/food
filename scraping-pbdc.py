import requests
from bs4 import BeautifulSoup

r = request.get("www.princeton.edu/~pbdc/people.html")

soup = BeautifulSoup(r)

print "People"
for row in soup.find_all("td"):
	print("%s\n" % row)