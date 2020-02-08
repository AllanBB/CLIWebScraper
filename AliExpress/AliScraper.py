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
#URL_NUMBER = 32995028266
#URL_NUMBER = 32995023560
#URL_NUMBER = 32995023311
#URL_NUMBER = 32995023387
#EDGE_CASE_URL = 32995023387


lower_range = int(sys.argv[1])
upper_range = int(sys.argv[2])


def getRating():
    ratingIndex = feedbackSoup.find('<div class="star-view-big"><span style="')
    ratingString = feedbackSoup[ratingIndex+46:ratingIndex+50]
    return ratingString
    #print(ratingString)

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
    #print(page_soup )
    return numOrderString
    print(numOrderString)





for URL_NUMBER in range(lower_range, upper_range):
    
    print("Now going though product: " +str(URL_NUMBER))
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
    rating = getRating()
    print("Rating: " + rating)
    productNumber = URL_NUMBER
    print("Item ID Number: "+ str(productNumber))
    numOrders = getNumOrders()
    print("Total Number of orders made: " + numOrders)




     # Create dictionary
    dict_product_id_copy = copy.deepcopy(productNumber)
    #dict_product_name_copy = copy.deepcopy(get_product_name())
    #dict_category_list = copy.deepcopy(get_category())
    #dict_last_date_purchased = copy.deepcopy(date_list[-1])
    dict_rating = copy.deepcopy(rating)
    dict_date_scraped = datetime.datetime.today()
    #dict_last_page_reached = copy.deepcopy(current_page)
    dict_num_transactions_copy = copy.deepcopy(numOrders)
    #dict_date_list_copy = copy.deepcopy(date_list)
    temp_dictionary = {'product_id': dict_product_id_copy, 'rating': dict_rating, 'num_transactions': dict_num_transactions_copy, 'date_scraped': dict_date_scraped} 
#    temp_dictionary = {'product_id': dict_product_id_copy, 'product_name': dict_product_name_copy, 'category': dict_category_list, 
#    					'rating': dict_rating, 'last_purchase_date': dict_last_date_purchased, 'last_page_reached': dict_last_page_reached, 
 #   					'num_transactions': dict_num_transactions_copy, 'transaction_list': dict_date_list_copy, 'date_scraped': dict_date_scraped
#                      } 
    for i in temp_dictionary:
        print(temp_dictionary[i])
    client = pymongo.MongoClient(
        "mongodb://allan:Spring2019@firstcluster-shard-00-00-wy2qu.mongodb.net:27017,firstcluster-shard-00-01-wy2qu.mongodb.net:27017,firstcluster-shard-00-02-wy2qu.mongodb.net:27017/test?ssl=true&replicaSet=FirstCluster-shard-0&authSource=admin&retryWrites=true")
    db = client['test']
    collection_products = db['products']
    query = {'product_id': dict_product_id_copy}
    new_value = {"$set": temp_dictionary}

    if(collection_products.update_one(query, new_value, upsert=True)):
        print("update_one")
    client.close()
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

