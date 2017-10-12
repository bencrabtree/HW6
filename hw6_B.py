import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

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
