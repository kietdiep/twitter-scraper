# twitter-scraper


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

## Possible fixes to Limitations
Will most likely remove location filter due to the fact that the Twitter API is the cause of the problem and will try to delete entries in the output table when clicking the back button to fill new values into table
