from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
#from urllib.request import Request as request

import urllib.request
URL_NUMBER = 417585875
feedbackURL = 'https://www.dhgate.com/product/2017-classical-all-white-black-gray-low-high/'+ str(URL_NUMBER) +'.html'
google = 'https://www.dhgate.com/'
#try:

req = urllib.request.Request('https://www.dhgate.com/', headers={'User-Agent': 'Mozilla/5.0'})

print(uReq(req))
#with urllib.request.urlopen(req) as response:
 #  the_page = response.read()
#req = Request('https://www.dhgate.com/', headers={'User-Agent': 'Mozilla/5.0'})
#uClient = uReq(google)
#uClient = uReq(google, headers={'User-Agent': 'Mozilla/5.0'})       
#feedbackHTML = uClient.read
#print(uClient)
#uClient.close()
