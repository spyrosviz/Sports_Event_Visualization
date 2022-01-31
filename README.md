# Sports_Event_Analysis

## Aim of Project
This project aims in visualizing sport events in **football**, **basketball** and **tennis**

## Source of Data
* Data for football are open source data created by WyScout and Statsbomb.
* Data for basketball were found on [kaggle](https://www.kaggle.com/boonpalipatana/nba-playoff-shots-2018)
* Data for tennis were also found on [kaggle](https://www.kaggle.com/boonpalipatana/nba-playoff-shots-2018)

## Aknowledgements
* All contributors of mplsoccer library which is very useful for visualizing football events data
* Boon P for uploading NBA Playoff 2018 data on kaggle
* [Savvas Tjortjoglou](https://github.com/savvastj) and [hkair](https://github.com/hkair) for creating functions to draw beautiful visualizations of the basketball events on court
* Robert Seidl for creating and uploading Australian Open Final 2019 tennis data on kaggle

## Project Description
This project has 3 main parts where each part is about a different sport (football, basketball and tennis)
1. Football open source data created by WyScout were downloaded from Figshare. Germany vs Italy game with a specific id from wyscout, was selected as demo to visualize Italy's corners ball path, on football court. However coordinates data did not seem to be right even when trying to visualize different events like shots or passes. Thus Statsbomb python API was used to extract data from Belgium-England match in FIFA World Cup 2018. Belgium's player, Thomas Meunier was randomly selected to visualize his passes on football court in the second half of the game. This time ball coordinates data seemed plausible.
2. Basketball data were downloaded from kaggle. Giannis Antetokounmpo was selected to visualize his coordinates when shooting in target (points) and out of target (missed shots) in NBA Playoffs 2018.
3. Tennis data from Australian Open Final 2019 were also downloaded from kaggle. I wrote a function for creating a tennis pitch with dimension's in meters which was also the metric for coordinates data given. Nadal and Djokovic coordinate data were visualized when winning. An animation of a specific rally was created with player's coordinate. In addition a web app with Dash framework was created and deployed with pythonanywhere. In the app, the user can select and animate a specific rally of the Australian Open Final 2019 based on player's coordinates data. If you choose a specific rally and hit play but the dot does not move on the court, it means that this rally was ace and thus the dot shows the hitter's initial position when serving the ball. The web app can be found [here](https://spyrosviz.eu.pythonanywhere.com).
