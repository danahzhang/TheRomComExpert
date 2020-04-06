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

#URL for List of Rom-Coms
url = "https://en.wikipedia.org/wiki/List_of_romantic_comedy_films"

#Finding all of the Tables within the List of Romantic Comedy Film Wikipedia URL
tables = pd.read_html(url)
number_of_tables = 0
for x in range(20):
    try:
        tables[x]
        number_of_tables += 1
    except IndexError:
        number_of_tables = number_of_tables

#Creating DataFrames with each Table and Connecting all the Tables
romcom_list = []
for x in range(number_of_tables-1):
     romcom_list.append(pd.DataFrame(tables[x]))
romcom_df = pd.concat(romcom_list, sort=False)
romcom_df.columns = ["Year","Title","Director","Country","Notes","Empty"]
romcom_df = romcom_df.filter(items=["Year","Title","Director","Country"])
romcom_df = romcom_df.set_index("Country")
romcom_df = romcom_df.filter(like='United States', axis=0)
romcom_df = romcom_df.reset_index()
romcom_df = romcom_df.filter(items=["Year","Title"])


#API Setup
base_url = "http://www.omdbapi.com/"
title_url = "?t="
year_url = "&y=" 
api_key = "&apikey=trilogy"

#Create a list for Json Url for each RomCom
#Test the Wikipedia Titles to Find Inaccurate Ones
#If Inaccurate, will not put in list, will fix later
romcom_api_urls = []
mistitled_movie_index =[]
for row in range(len(romcom_df.to_numpy())):
    try:
        title = romcom_df.to_numpy()[row][1]
        year = str(romcom_df.to_numpy()[row][0])
        response = requests.get(base_url + title_url + title + year_url + year + api_key)
        try:
            if response.json()['Title'] != "A Title(Which Means It Has a Title)":
                romcom_api_urls.append(response.url)
        except KeyError:
            mistitled_movie_index.append(row)
    except:
        pass

#Create a Dictionary for Movie Titles and Year for Mistitled
old_titles = romcom_df['Title'][mistitled_movie_index].tolist()
#Format(Fix Special Characters)
old_titles_titles = list(old_titles[i].encode("ascii", "replace").decode("utf-8") for i in range(len(old_titles)))
old_titles_years = romcom_df['Year'][mistitled_movie_index].tolist()
old_titles_dictionary = {old_titles_titles[i]: str(old_titles_years[i]) for i in range(len(old_titles))}

#Match the Correct Ends of the URL with Each Title
#first find all possible correct ends
new_title_urls_ends = []
soup = BeautifulSoup(urlopen(url), 'html.parser')
for link in soup.findAll('a'):
    new_title_urls_ends.append(str(link.get('href')))

#Reformat Titles to Match with Links Accurately
new_titles = []
unfound_titles = []
for title in old_titles_titles:
#Find the Correct URLs to each Movie 
#Match with URLs from the Wiki List HTML
    ends = []
    new_title = title.replace(" ","_")
    new_title = new_title.replace("?","%27")
    for end in new_title_urls_ends:
        if end.find(new_title) != -1:
            ends.append(end)
    if len(ends) == 1:
        new_title = ends[0]
    elif len(ends) > 1:
        for end in ends:
            if old_titles_dictionary[title] in end:
                new_title = end
    else:
        unfound_titles.append(title)
    new_url = "https://en.wikipedia.org" + new_title
    soup = BeautifulSoup(urlopen(new_url),'html.parser')
    new_titles.append(soup.find('th', class_='summary').text)

#Create a New Dictionary with Correct Titles and Year
new_titles_dictionary = {new_titles[i]: str(old_titles_years[i]) for i in range(len(new_titles))}

#Add Dictionary Back Into DataFrame to Update Dataframe
romcom_df.append(new_titles_dictionary, ignore_index=True)

#Add new titles' URLs into list
#Test Again to Double Check

mistitled_movie_index =[]
for row in range(len(new_titles_dictionary)):
    try:
        title = list(new_titles_dictionary)[row]
        year = new_titles_dictionary[list(new_titles_dictionary)[row]]
        response = requests.get(base_url + title_url + title + year_url + year + api_key)
        try:
            if response.json()['Title'] != "A Title(Which Means It Has a Title)":
                romcom_api_urls.append(response.url)
        except KeyError:
            mistitled_movie_index.append(row)
    except:
        pass
len(romcom_api_urls)


#Create Record
with open('./resources/json/romcom_api_urls.json', 'w') as outfile:
    json.dump(romcom_api_urls, outfile)

#Create Workable Json File for Javascript
with open('./templates/static/romcomApiUrl.js', 'w') as file:
    file.write("var random = {url: "+f'{romcom_api_urls}'+'};'.strip())

#Use Links to Get JSON Files for Each Movie
romcom_api =[]
for link in romcom_api_urls:
    response = requests.get(link)
    romcom = response.json()
    romcom_api.append(romcom)

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

