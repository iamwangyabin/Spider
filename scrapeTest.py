from bs4 import BeautifulSoup
import urllib
html=urllib.urlopen("")
bsObj=BeautifulSoup(html.read())
print(bsObj.h1)