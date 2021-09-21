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

## Revised Limitations
In order to stay consistent with the flow of the application, the location filter has been removed due to the difficulty of use for the user. The user would have to search up the numerical coordinates of a certain city in order for it to work and I ideally wanted this application to work without any difficulty to the user. Additionally, in order to combat my problem with the back button, the application instead will ask to "search again: in which it reloads the program and restarts it from scratch. In order to combat this ongoing cycle, the user can click the exit button to stop the program.
