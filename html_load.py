from bs4 import BeautifulSoup
from urllib2 import urlopen


import re

my_address = "http://insiderbranding.com"
html_page = urlopen(my_address)
html_text = html_page.read()
soup = BeautifulSoup(html_text, "html.parser") #second param tells which parser to use
#scrape all images

images= []
images= soup.find_all("img")
for img in images:
    print img['src']
