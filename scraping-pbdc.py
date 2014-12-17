import urllib
'''import requests'''
from bs4 import BeautifulSoup

'''r = request.get("www.princeton.edu/~pbdc/people.html")'''

f = urllib.urlopen("http://www.princeton.edu/~pbdc/people.html")

r = f.read() 

soup = BeautifulSoup(r)

print "People"
for row in soup.find_all("td"):
	print("%s\n" % row)