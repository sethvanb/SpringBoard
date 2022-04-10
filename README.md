# SpringBoard Capstone Project

## Project Ideas
    - Sports Bets(Over/Under)
    - Mobile RangeFinder for Golf
    - Automatic Room Lights(Thermal Cameras)

## Project Description
The idea I settled on was a machine learning model to help people bet on sports. To do this the model will be trained on a teams previous schedule and the resulting score for each game. Then when a new season starts some one can use an api to input a specific game and it will return a predict score range for both teams playing. This will aid in betting when deciding what teams to bet on and weather they wany to take the spread or moneyline. 

## Datasets Explored
    - 1. https://www.balldontlie.io/#get-all-stats
    - 2. https://panz.io/mlbgame/#mlbgame.players
    - 3. https://www.baseball-reference.com/teams/SFG/2021-schedule-scores.shtml
        - https://github.com/jldbc/pybaseball

## Data Collection and Cleaning
I decided to go with a baseball dataset becuase the NBA season is ending and the MLB season is just about to start so it will be easier to test and get new data points. I settled on the Baseball Refrence website because it had more statistics about games and it was easy to download CSVs for each season. I created a python script that utilizes the [pybaseball API](https://github.com/jldbc/pybaseball) to gather game data on all 30 teams over the last 10 years (2012-2021). It drops all other columns except for game number of the season, date, team, home or away, opponent, runs scored, runs against, wins and losses, rank, games back, day or night, and streak. These are all values we can know before a game that can be processed to predict the runs scored and runs againts ranges. These data columns need to be cleaned and this is how I did it. For each team there is a CSV with the games for their 10 seasons. There is also one CSV for all the teams that has all of the games. This CSV had to be cleaned to take out duplicate games and this was done by only keeping teams home games. This means we can also remove the home or away column because we know that the team column contains the home team. 

### Useful columns
    - Game number of the season
    - Team
    - Home or Away
    - Opponent
    - Runs scored
    - Runs against
Data that needs cleaning:
    - Date (single number)
    - Day=0 or Night=1 game 
    - Double Header: no=0, yes=1
    - Streak coming in
    - Rank coming in  
    - GB coming in
    - Wins coming in
    - Losses coming in
    - Ratio of wins to losses coming in?