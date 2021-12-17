# twitter-scraper



https://user-images.githubusercontent.com/32941163/139967497-12d29910-78ee-4b9f-8203-96bc2b553662.mp4


## Features

This application allows you to view the last hundred tweets posted by a given search criteria (keyword, username, location, hashtag)


## Technologies Used
- SQLite
- tweepy 
- PyQt5
- Sys
- Os

## How to use
pip install -r requirements.txt  
python .\src\gui.py

## Limitations
Though functionality is complete, location has been a difficult filter criteria to implement due to the tweepy API not working for other geo-locations aside from the examples they list from their website. Additionally, the way that the code is currently implemented, a back button is able to be made functional but will not create a new instance of a search screen due to the values of the page not being updated. Unfortunately it will just show the previous search results. 

## Revised Limitations
In order to stay consistent with the flow of the application, the location filter has been removed due to the difficulty of use for the user. The user would have to search up the numerical coordinates of a certain city in order for it to work and I ideally wanted this application to work without any difficulty to the user. Additionally, in order to combat my problem with the back button, the application instead will ask to "search again: in which it reloads the program and restarts it from scratch. In order to combat this ongoing cycle, the user can click the exit button to stop the program.

## Mindset while creating this project
Originally I had planned to create a search engine based application which would index a database of stored tweets in order to search from it. However, in order to save enough tweets to make a worthwhile database, the twitter scraper file would have to run for hours and would eventually hit a streaming limit preset by the Twitter API. From my initial implementation, I had designed the scraper class to return a dataframe object from the pandas library so that I could get around using SQL databases. However, when reading from the data and storing it into the PyQt5 tablewidget, it had problems retreiving the values. Due to this, I decided it was better to research how to use SQLite since I did not have a server to host PostgreSQL (Amazon AWS is an option but I preferred to get practice with SQLite before moving onto it). In switching my implementation, I realized that having a class for the Scraper was useless because it no longer returns a value but rather creates a db file for my gui.py file to retrieve data from. Was not worth the extra time changing the code so I left the Scraper class as is.
