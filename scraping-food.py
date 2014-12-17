import urllib
from bs4 import BeautifulSoup

https://campusdining.princeton.edu/dining/_Foodpro/nutframe.asp?sName=Princeton+University+Campus+Dining&locationNum=02&locationName=Butler+%26+Wilson+Colleges&naFlag=1

 urllib.urlencode({'locationNum':'02', 'locationName': "Butler & Wilson Colleges"})
collegenums = {'02'}
colleges = {"Butler & Wilson Colleges"}