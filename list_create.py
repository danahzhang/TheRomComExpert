import sqlite3
import os
import csv
from sqlite3 import Error
import pandas as pd
#Create the Dataset to JS files as Arrays
#Create Pandas DataFrame

#Connect to Database
conn=sqlite3.connect('Romcom.sqlite')

#Create Dataframe
df = pd.read_sql_query("SELECT * FROM romcom_main", conn)
df2 = df.copy()


#Create Master List
year_list = []
y_list = []
yall_list = []

#Create YearList and Movie per Year List
movie_years = df2.groupby(['year'])['id'].count()
year_list = movie_years.index.tolist()
movie_amount= movie_years.tolist()
y_list.append(movie_amount)

#Create Box Office, Rotton Tomatoes, Imdb, and Metascore Lists
money = df2.groupby(['year'])['boxoffice'].mean()
money_amount= money.tolist()
money_all = df2.groupby(['year'])['boxoffice'].apply(list)
money_all = money_all.tolist()
y_list.append(money_amount)
yall_list.append(money_all)

rotten = df2.groupby(['year'])['ratings'].mean()
rotten_amount= rotten.tolist()
rotten_all = df2.groupby(['year'])['ratings'].apply(list)
rotten_all = rotten_all.tolist()
y_list.append(rotten_amount)
yall_list.append(rotten_all)

#To make rating out of 100 instead of 10
df2['imdbrating']=df2['imdbrating']*10
imdb = df2.groupby(['year'])['imdbrating'].mean()
imdb_amount= imdb.tolist()
imdb_all = df2.groupby(['year'])['imdbrating'].apply(list)
imdb_all = imdb_all.tolist()
y_list.append(imdb_amount)
yall_list.append(imdb_all)

meta = df2.groupby(['year'])['metascore'].mean()
meta_amount= meta.tolist()
meta_all = df2.groupby(['year'])['metascore'].apply(list)
meta_all = meta_all.tolist()
y_list.append(meta_amount)
yall_list.append(meta_all)


#Create a Workable File for Javascript
with open('./templates/static/lists.js', 'w') as file:
    file.write("var nan = null; var year_list = "+f'{year_list};' + "var y_list = "+f'{y_list};'+ "var yall_list = "+f'{yall_list};')


#Print Confirmation
print("Part 3: list all updated")

