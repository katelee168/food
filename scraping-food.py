import urllib
from bs4 import BeautifulSoup

base = "https://campusdining.princeton.edu/dining/_Foodpro/nutframe.asp?sName=Princeton+University+Campus+Dining&%s" 

params = {"locationNum=01&locationName=Rockefeller+%26+Mathey+Colleges&naFlag=1", "locationNum=02&locationName=Butler+%26+Wilson+Colleges&naFlag=1", "locationNum=03&locationName=Forbes+College&naFlag=1", "locationNum=04&locationName=Graduate+College+&naFlag=1", "locationNum=05&locationName=Center+for+Jewish+Life&naFlag=1", "locationNum=07&locationName=Woodrow+Wilson+Cafe&naFlag=1", "locationNum=08&locationName=Whitman+College&naFlag=1", "locationNum=15&locationName=Frist+Gallery&naFlag=1", "locationNum=16&locationName=Witherspoon%27s&naFlag=1", "locationNum=17&locationName=Cafe+Vivian&naFlag=1", "locationNum=19&locationName=Chancellor+Green+Cafe&naFlag=1", "locationNum=21&locationName=Every+Day+Grill&naFlag=1", "locationNum=23&locationName=Chemistry+CaFe&naFlag=1", "locationNum=30&locationName=Baked+Goods+%26+Frozen+Treats&naFlag=1", "locationNum=06&locationName=Breakfast+%26+Brunch&naFlag=1", "locationNum=35&locationName=Frist+Favorites&naFlag=1", "locationNum=40&locationName=Salad+Selections&naFlag=1"}

college = raw_input("What college would you like to look up the menue for?")
f = urllib.urlopen(base % params[college])

html = f.read()
soup = BeautifulSoup(html)

for category in soup.find_all("div", {"class":"menusampcats"})
	print category
	for food in category.find_all("a", {"name": "Recipe_Desc"})
	print "\t%s" % food