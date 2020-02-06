from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import time
import sys
import copy
import json
import os
import pymongo
import datetime




## Things to find
product_id = 1
product_name = 1
category = 0
rating = 0
last_purchase_date = 0
last_page_reached = 0
num_transactions = 1
transaction_list = 0
date_scraped = 0  
topratedratedsellerboolean = 0
otherrating = 0
priceofitem = 0


#GLOBAL VARIABLES
URL_NUMBER = 32995023311
URL_NUMBER = 32995023387
EDGE_CASE_URL = 32995023387


def getRating():
    ratingIndex = feedbackSoup.find('<div class="star-view-big"><span style="')
    ratingString = feedbackSoup[ratingIndex+46:ratingIndex+50]
    print(ratingString)

def isPageEmpty():
    ratingIndex = feedbackSoup.find('<div class="star-view-big"><span style="')
    if(ratingIndex == -1):
        return -1
    else:
        return

def getNumOrders():
    numOrderIndex  = page_soup.find('tradeCount')
    endOderIndex = page_soup.find(',"tradeCountUnit":')
    numOrderString = page_soup[numOrderIndex+12:endOderIndex] 
    print(numOrderString)





for URL_NUMBER in range(URL_NUMBER, URL_NUMBER+1):
 
    ################################ Make feedback Soup ############################# START
    start_time = time.time()


    feedbackURL = 'https://feedback.aliexpress.com/display/productEvaluation.htm?productId='+ str(URL_NUMBER) +'&ownerMemberId=2&type=default&page=1'
    try:
        uClient = uReq(feedbackURL)
        feedbackHTML = uClient.read()
        uClient.close()
    except:
        print("this is not good")
        #continue

    feedbackSoup = str(soup(feedbackHTML, "html.parser"))

    #print("feedback page took: %s seconds ---" % (time.time() - start_time))
    ################################################################################# END


    pageCheck = isPageEmpty()
    if(pageCheck == -1):
        continue



    

    ################################ Make Regular Soup ############################# START
    start_time = time.time()


    url ='https://www.aliexpress.com/item/' + str(URL_NUMBER) +'.html'
    try:
        uClient = uReq(url)
        page_html = uClient.read()
        uClient.close()
    except:
        print("this is not good")
            #continue
       
    page_soup = str(soup(page_html, "html.parser"))

    #print("Regular page took: %s seconds ---" % (time.time() - start_time))
    ################################################################################# END

    
    #page_html =  makeSoup()


    ######## Find number of transactions ########
    #index  = page_soup.find('tradeCount')
    #print(page_soup.find('tradeCount'))
    #print(page_soup[index+12:index+17])
    #print(page_soup.find('item-not-found-image'))

    print("\n")

    ######### Find product number ###############
    #productNameIndex = page_soup.find('"subject":"')
    #print(page_soup[productNameIndex+11:index-3])

    #####################   ########################

    #####################   ########################

    #####################   ########################

    #####################   ########################

    #####################   ########################

    #####################   ########################

    #####################   ########################

    #####################   ########################

    #####################   ########################

    #####################   ########################

    #####################   ########################

    #####################   ########################

    #####################   ########################

    #####################   ########################

    #####################   ########################

    #####################   ########################


    #####################   ########################
    #####################   ########################

    ##################### Formatted output for testing  ########################
    print("Rating:")
    getRating()
    print("Item ID Number")
    print(URL_NUMBER)
    print("Total Number of orders made: ")
    getNumOrders()

    # Create URL
    # url = 'https://feedback.aliexpress.com/display/evaluationProductDetailAjaxService.htm?callback=jQuery&productId=' + str(4000591272216) + '&type=default&page=1'
    #url ='https://www.aliexpress.com/item/32995023311.html'

    # Make soup as a str so that it can easily be converted to json
    #supper = soup(page_html, "html.parser")

    #
    #print(url)


    #mydivs = supper.findAll("script", {"class": "product-reviewer"})
    #print(str(mydivs))
    #print(mydivs)

