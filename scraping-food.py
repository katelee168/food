import urllib
from bs4 import BeautifulSoup

base = "https://campusdining.princeton.edu/dining/_Foodpro/menuSamp.asp?%s"

dhall = {'rocky': 0, 'mathey': 0, 'butler': 1, 'wilson': 1, 'forbes': 2, 'grad': 3, 'cjl': 4, 'woodywoo': 5, 'whitman': 6, 'witherspoon': 7, 'viv': 8, 'green': 9, 'grill': 10, 'chem': 11, 'baked': 12, 'breakfast': 13, 'frist': 14, 'salad': 15}

params = ["locationNum=01&locationName=Rockefeller+%26+Mathey+Colleges&naFlag=1", "locationNum=02&locationName=Butler+%26+Wilson+Colleges&naFlag=1", "locationNum=03&locationName=Forbes+College&naFlag=1", "locationNum=04&locationName=Graduate+College+&naFlag=1", "locationNum=05&locationName=Center+for+Jewish+Life&naFlag=1", "locationNum=07&locationName=Woodrow+Wilson+Cafe&naFlag=1", "locationNum=08&locationName=Whitman+College&naFlag=1", "locationNum=15&locationName=Frist+Gallery&naFlag=1", "locationNum=16&locationName=Witherspoon%27s&naFlag=1", "locationNum=17&locationName=Cafe+Vivian&naFlag=1", "locationNum=19&locationName=Chancellor+Green+Cafe&naFlag=1", "locationNum=21&locationName=Every+Day+Grill&naFlag=1", "locationNum=23&locationName=Chemistry+CaFe&naFlag=1", "locationNum=30&locationName=Baked+Goods+%26+Frozen+Treats&naFlag=1", "locationNum=06&locationName=Breakfast+%26+Brunch&naFlag=1", "locationNum=35&locationName=Frist+Favorites&naFlag=1", "locationNum=40&locationName=Salad+Selections&naFlag=1"]

college = raw_input("What college would you like to look up the menue for? ")

f = urllib.urlopen(base % params[dhall[college]])

html = f.read()
soup = BeautifulSoup(html)
print soup.prettify()
for category in soup.find_all("div", {'class':'menusampcats'}):
	print category
	for food in category.find_all("a", {"name": "Recipe_Desc"}):
		print "\t%s" % food