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

############################################
            #### PART B ####
############################################
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url2 = input("Enter URL: ")
theurl = urllib.request.urlopen(url2, context=ctx).read()
count = int(input("Enter count: "))
position = int(input("Enter position: ")) - 1
index = 1

print("Retrieving: " + str(url2))
while (index < count):
    s = BeautifulSoup(theurl, "html.parser")
    webhtml = s.find_all('a')[position].get('href')
    print("Retrieving: " + str(webhtml))
    theurl = urllib.request.urlopen(webhtml, context=ctx).read()
    index += 1

s2 = BeautifulSoup(theurl, "html.parser")
print("Retrieving: " + s2.find_all('a')[position].get('href'))
print(s2.find_all('a')[position].string)
