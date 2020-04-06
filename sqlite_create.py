#Import Dependencies
import requests
import pprint
import json
from sqlalchemy import create_engine, Column, Integer, String, Date, Float, Numeric   
from sqlalchemy.ext.declarative import declarative_base

import datetime as dt
import time
Base = declarative_base()

# Define romantic_comedy table
class Romcom(Base):
    __tablename__ = 'romcom_main'
    __table_args__ = {'extend_existing': True} 
    id = Column(String, primary_key=True)
    title = Column(String)
    year = Column(Integer)
    rated = Column(String)
    released = Column(Date)
    runtime = Column(Integer)
    genre = Column(String)
    director = Column(String)
    writer = Column(String)
    actors = Column(String)
    plot = Column(String)
    language = Column(String)
    country = Column(String)
    awards = Column(String)
    poster = Column(String)
    ratings = Column(Float)
    metascore = Column(Integer)
    imdbrating = Column(Float)
    imdbvotes = Column(Integer)
    imdbid = Column(String)
    dvd = Column(Date)
    boxoffice = Column(Integer)
    production = Column(String)
    website = Column(String)

Base.metadata.tables

#Create SQLite Engine
engine = create_engine('sqlite:///romcom.sqlite')

# Create Table in DataBase
Base.metadata.create_all(engine)

#Open Session
from sqlalchemy.orm import Session
session = Session(engine)

#Get all the JSON Data from the romcom_api_urls.json file
with open('./resources/json/romcom_api_urls.json') as json_file:
    data = json.load(json_file)

#add data from json links to sql table
already_committed = {}
for link in data:
    committed = "No"
    response = requests.get(link)
    romcom = response.json()
    
    #Convert "N/A" to None
    #Movie Rating
    if romcom['Rated']=="N/A":
        rated_ = None
    else:
        rated_ = romcom['Rated']
    #Awards
    if romcom['Awards']=="N/A":
        oscar = None
    else:
        oscar = romcom['Awards']
    #Poster URL
    if romcom['Poster']=="N/A":
        poster_url = None
    else:
        poster_url = romcom['Poster']
    #Production Company
    if romcom['Production']=="N/A":
        studio = None
    else:
        studio = romcom['Poster']
    #Website
    if romcom['Website']=="N/A":
        web = None
    else:
        web = romcom['Poster']
        
    #Format Corrections to Keep Change Type
    #convert runtime to integer
    try:
        the_runtime = int(romcom['Runtime'][:-3])
    except (ValueError, TypeError):
        the_runtime = None
    #Format Date Object
    date_object = dt.datetime.strptime(romcom['Released'], "%d %b %Y") 
    #Since Rating is one of the following: empty list, a one key dictionary or a multikey dictionary
    #Rating represent Rotten Tomato Score since all other scores are present
    #replacing the items without scores with a null Value
    index = "none"
    if len(romcom['Ratings']) > 0:
        for x in range(len(romcom['Ratings'])):
            if romcom['Ratings'][x]['Source' ]== "Rotten Tomatoes":
                index = x
        if index != "none":
            rt_rating= float(romcom['Ratings'][index]['Value'][:-1])
        else:
            rt_rating= None
    else:
        rt_rating= None
    #convert metascore to integer
    try:
        meta = int(romcom['Metascore'])
    except (ValueError, TypeError):
        meta = None  
    #convert imdb rating to float
    try:
        imdb_rate = float(romcom['imdbRating'])
    except (ValueError, TypeError):
        imdb_rate = None 
    #convert metascore to integer
    try:
        imdb_vote = int(romcom['imdbVotes'].replace(",",""))*10
    except (ValueError, TypeError):
        imdb_vote = None  
    #DVD object to Date
    try:
        dvds = dt.datetime.strptime(romcom['DVD'], "%d %b %Y")
    except:
        dvds = None
    #BoxOffice to Integer
    try:
        money = int(romcom['BoxOffice'].replace("$","").replace(",",""))
    except (ValueError, TypeError):
        money = None 
        
    #make sure all is committed
    while committed == "No":
        #create row to commit
        romcom_item = Romcom(id= romcom['imdbID'],
                title= romcom['Title'],
                year= romcom['Year'],
                rated= rated_,
                released= date_object,
                runtime= the_runtime,
                genre= romcom['Genre'],
                director= romcom['Director'],
                writer= romcom['Writer'],
                actors= romcom['Actors'],
                plot= romcom['Plot'],
                language= romcom['Language'],
                country= romcom['Country'],
                awards= oscar,
                poster= poster_url,
                ratings= rt_rating,
                metascore= meta,
                imdbrating= imdb_rate,
                imdbvotes= imdb_vote,
                imdbid= romcom['imdbID'],
                dvd= dvds,
                boxoffice= money,
                production= studio,
                website= web)
        session.add(romcom_item)
        try:
            session.commit()
            committed = "Yes"
        except: 
            session.rollback()
            romcom_delete = session.query(Romcom).filter_by(id= romcom['imdbID']).delete()
            session.commit()

if(len(already_committed.keys())) == 0:
    print("All Keys Committed")
else:
    print(f"There are {len(already_committed.keys())} not committed keys.")

# query the database
engine.execute('SELECT * FROM romcom_main').fetchall()


#Print Confirmation
print("Part 2: sqlite all updated")


