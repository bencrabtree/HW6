import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

##########################################
            #### PART A ####
##########################################

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()

soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
numbers = soup.find_all('span')

values = []
for tag in numbers:
    values.append(int(tag.string))
sumVal = sum(values)

print ("Count: " + str(len(values)))
print ("Sum: " + str(sumVal))
