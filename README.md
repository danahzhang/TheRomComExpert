The Romcom Expert:
By Dana Zhang

To make everything work, just run the app.py file.
!!!!Pick to Run the Short Version!!!!!!

Introduction:

Being a cinephine, there is always an awkwardness when dicussing the neglected child of cinema, the romantic comedy. Once a staple of the movie industry, the romantic comedy is became a genre niche, almost treated as a guilty pleasure when discussed as cinema. While the superhero boom in the movie industry guarantees the survival of action movies, the romantic comedy seems to have lost its favor within the movie industry. 

As a proclaim lover of this now seeming niche genre, there is a sense that movies that I grew up loving are not loved. What worries me even more is Netflix. The recent boom of romantic comedy films have found its platform on streaming sites, such as Netflixs. While the continue existence of romantic comedies might be protected by the likes of Netflix, this does seem to send a signal that these movies are to be enjoyed alone. 

Movies are easily accessible online, but movies still get released in theaters. The theater lets movies be a communal experience. It made comic books mainstream. While movies like To All the Boys I Loved Before can still be a great hit, the fact that movies as such live only as an individual viewing experience shows a disconnect between mainstream and the target audience of the romantic comedy, females.

With this project, there are three rather general questions that are raise concerning the future of romantic comedy movies. 

1.Has there been a decline in romantic comedy films in the industry?
2.Are romantic comedy films profitable?
3.Do people enjoy such films?

Question one and two both relate to the supply side of the film industry. Are romantic comedy films being made? This first examines whether romantic comedy films are experiencing a setback or is my inital observation, the decline of the romantic comedy film industry, inaccurate. While the fluctuation of films release per year can represent a variety of factor regarding with the film industry at large, since films are first and foremost a generally large investment, the number of romantic comedies being produce can speak volumes about how the industry sees romantic comedies. 

Question two and three both relate to the demand side of the film industry. The profitablily allows movies of that similar type to continously be made. Adam Sandler movies and the Star Wars franchise are two examples of how influencial box office records are. People spend money on what they want to see. By observing the average profitability of romantic comedy films, it also can reveal whether the industry will continue to invest in such films. 

In this day and age, there are many ways to measure the success of money. While profits is the foremost measure to the industry, critics as driven another measure, prestige (or brand) of films. Movies like Parasite(2019) was able to become more mainstream not due to box office numbers but due to popularity, first among critics, then among moviegoers at large. People liking the film still allows such films to exist. Therefore, while scores and rating of movies are general not treated with much fanfare when discussing movies, it affect which movies are being seen to a certain extent.

Methology:

Data Front:

To explore these facets of the romantic comedy film industry, I have utilized OMDb API (http://www.omdbapi.com), a open movie database. This API provide a movie's data give the correct title or imdbID.

For the list of romantic comedies, I have originally and currently am using the Wikipedia List on romantic comedy films (https://en.wikipedia.org/wiki/List_of_romantic_comedy_films), which provides a somewhat comphrehensive list. I'm currently also trying to use an extremely large list (over 15000) from imdb but due to the size, the processing has been too slow to see if it's possible. (Efforts in json_create_long.py)

json_create.py

The list of movies and year of release is gathered from the wikipedia page and using the API, search through OMDb. If the movie exist, the url which contains the movie's data's JSON file is kept in a JSON file for record and a Javascript file for use. Wepscraping the titles from the film's offical wikipedia page is done for titles that don't match. 

sqlite_create.py

After the urls are all accounted for, the database is get create through Python as an SQLite database. Since the JSON file only contained strings, I converted the dates into dates, the floats into floats, and the "N/A" into None to assure usability. THere was also an object within the JSON which didn't stay consistent throughout. Rating contain zero to three depending on the film, which I made into the Rotten Tomatoes rating, since the other two items were accounted for.

I used the imdbID as the primary key since every imdbID is unique. It also allow the code to update the information if the imdbID is within the database already.

list_create.py
While using files created within the code is possible, I am unable to since "CORS request not HTTP" issue keeps popping up. I skirted around this issue through a few methods including created JS files with Python and using the API URL for accessing JSON data. I used Python to create these files. This allowed me to easily create the charts with Plot.ly.

app.py
For the RESTful API aspect, JSON data for a romantic comedy film can be search with imdbID or with the correct title.

Visual Front:

I used resources (https://bootswatch.com) to create my HTML files, and I used an open resource file for my CSS. While I added minute elements, the general formats were from that website. This allowed me to focus a bit more on fun elements for the website including a random poster generator for the front page (all.js and home.html) and the dataset viewing element for the data page (dataTable.js and data.html). 

The graphs were created with Plot.ly. I created three graphs:

1. Number of Films Per Year (resources/images/number_of_films.png)
2. Critical Acclaim Per Year (resources/images/critics.png)
3. Box Office Per Year (resources/images/box_office.png)

Observations (with the Wikipedia List):

1. Romantic Comedy Boom in the 2000s

According to the data, there is a boom in romantic comedy films in the 2000s. While this can mostly be explained by the fact that the Wikipedia list was gather during this era, but then there shouldn't be such a drop between the last two decades. There is clearly more romantic comedies release during the 2000s rather than the 2010s. The box office number also show the profitability of romantic comedies was higher during the 2000s. 

2. Drop in Quality and Profitability

While there are some winners, most romantic comedies did poorly at the box office. While the median seem to fluctuate around 50 million dollars which isn't great, especially since, while inflation is on the rise, not only the median box office numbers are decreasing, but there aren't any box office success stories. Without profits, there isn't any incentives for movie studios to make romantic comedies, which can explain the drop in romantic comedies films especially towards the late 2010s.

The critical acclaim to romantic comedy films also dropped through the years. While it must be pointed out that the films remember by a modern critic pool tend to be films that stand the test of time and therefore would score higher on average, if only focusing on the data between 1980s to now, which is a period of time that film critics do remember, there is overall a steady decline, especially during the heyday of the romantic comedies, 2000s. This might also explain the decline of romantic comedies. While during the decade of romantic comedy, profitability convinced studios to make more, but the quality didn't keep up with the production. Therefore, there is a more negative outlook on romantic comedies, averaging out to the high thirties by 2010. 

3. Qualilty and Netflix over Profitability

After 2010, there seems to be a rise again in the rating, but not in box office. This can be accounted for in two ways.  On average, the quality of romantic comedy films is higher. One theory why is due to the fact that fewer "critic unfriendly" romantic comedies are being made. If movie studios follow profit incentives when deciding to make more romantic comedies during the 2000s, they would have felt the lackluster box office numbers and be deincentived to make such romantic comedies. A romantic comedy film wasn't being made for solely profits. Therefore, there was not only less romantic comedy films, there was also less "half hazardly thrown together" romantic comedy films which would have improved the quality.

Further Goals:
After seeing the variety of different ways to explore the data and finding a bigger database, I would like to add factors like the films' country of origin to observe trend in different countries, language, and filter between box office numbers and critic ratings and vis versa. 
