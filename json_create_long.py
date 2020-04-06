#Import Dependencies
import requests
import json
import pandas as pd
import numpy as np
from pprint import pprint
import random
from bs4 import BeautifulSoup
from urllib.request import urlopen
import unicodedata
import re

#Find the Number of Movies for the Range of Pages
#Since imdb allows 50 movies per page

#The IMDB main url
url="https://www.imdb.com/search/title/?title_type=movie&genres=comedy,romance&view=simple&sort=boxoffice_gross_us,desc&start=1&explore=title_type,genres&ref_=adv_nxt"

#Find the number of possible pages
soup = BeautifulSoup(urlopen(url), 'html.parser')
page_max = str(soup.find_all("div", "desc"))
page_max = page_max.split(" ")
imdb_range = []
the_max = 0
for part in page_max:
    try:
        if int(part.replace(",",""))>the_max:
            the_max = part
    except:
        pass
the_max = int(the_max.replace(",",""))
#There were more then 10000 movies but after 9999, the url format became unclear
#this is so all the movie ids are collected
if the_max//2 > 9999:
    for x in range(1,10001,50):
        imdb_range.append(x)
else:
    for x in range(1,(the_max//2//50*50+1),50):
        imdb_range.append(x)


#List of ImdbIDs of possible Romcoms
ids= []
page_url1 = f"https://www.imdb.com/search/title/?title_type=movie&genres=comedy,romance&view=simple&sort=alpha,asc&start={x}&explore=title_type,genres&ref_=adv_nxt"
page_url2 = f"https://www.imdb.com/search/title/?title_type=movie&genres=comedy,romance&sort=alpha,desc&start={x}&explore=title_type,genres&ref_=adv_nxt"
page_urls = [page_url1, page_url2]

for page_number in imdb_range:
    x = page_number
    page_url1 = f"https://www.imdb.com/search/title/?title_type=movie&genres=comedy,romance&view=simple&sort=alpha,asc&start={x}&explore=title_type,genres&ref_=adv_nxt"
    soup = BeautifulSoup(urlopen(page_url1), 'html.parser')
    imdb_ids = soup.find_all("img", "loadlate")
    for imdb_id in imdb_ids:
        imdb_id= str(imdb_id)
        imdb_id=imdb_id.split('data-tconst="')
        imdb_id=imdb_id[1]
        #To Check to see if the IDs repeat
        if imdb_id[:9] not in ids:
            ids.append(imdb_id[:9])
for page_number in imdb_range:
    x = page_number
    page_url2 = f"https://www.imdb.com/search/title/?title_type=movie&genres=comedy,romance&sort=alpha,desc&start={x}&explore=title_type,genres&ref_=adv_nxt"
    soup = BeautifulSoup(urlopen(page_url2), 'html.parser')
    imdb_ids = soup.find_all("img", "loadlate")
    for imdb_id in imdb_ids:
        imdb_id= str(imdb_id)
        imdb_id=imdb_id.split('data-tconst="')
        imdb_id=imdb_id[1]
        #To Check to see if the IDs repeat
        if imdb_id[:9] not in ids:
            ids.append(imdb_id[:9])

print(f"There are {len(ids)} movies in the list.") 



#API Setup
base_url = "http://www.omdbapi.com/"
id_url = "?i="
api_key = "&apikey=trilogy"

#Create a list for Json Url for each RomCom
romcom_api_urls = []
for row in range(len(ids)):
    response = base_url + id_url + ids[row] + api_key
    romcom_api_urls.append(response)


#Create Record
with open('./resources/json/romcom_api_urls.json', 'w') as outfile:
    json.dump(romcom_api_urls, outfile)

#Create Workable Json File for Javascript
with open('./templates/static/romcomApiUrl.js', 'w') as file:
    file.write("var random = {url: "+f'{romcom_api_urls}'+'};'.strip())

#Use Links to Get JSON Files for Each Movie
romcom_api =[]
unusable_links =[]
for link in romcom_api_urls:
    try:
        response = requests.get(link)
        romcom = response.json()
        try:
            if response.json()['Title'] != "A Title(Which Means It Has a Title)":
                romcom_api_urls.append(link)
        except KeyError:
            mistitled_movie_index.append(link)
    except:
        unusable_links.append(link)
#Create Record
movie_dictionary = {}
movie_dictionary['movies'] = romcom_api
with open('./resources/json/romcom_api.json', 'w') as outfile:
    json.dump(movie_dictionary, outfile)

#Create Workable Json File for Javascript
with open('./templates/static/romcomApi.js', 'w') as file:
    file.write("var all_movies = "+f'{romcom_api};'.strip())


#Print Confirmation
print("Part 1: json all updated")

