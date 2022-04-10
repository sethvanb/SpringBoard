import pybaseball as pybb
import pandas as pd
import os
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# For all 30 MLB teams we will gather 10 years of records 2012-2021 and save them into a cvs for each team and one aggrgated one. 
years = [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
teamTags=['BAL', 'BOS', 'CHW', 'CLE', 'DET', 'HOU', 'KCR', 'LAA', 'MIN', 'NYY', 'OAK', 'SEA', 'TBR', 'TEX', 'TOR', 'ARI', 'ATL', 'CHC', 'CIN', 'COL', 'LAD', 'MIA', 'MIL', 'NYM', 'PHI', 'PIT', 'SDP', 'SFG', 'STL', 'WSN']

#Collect all the data frames for each team and each year and put them into one data frame
allFrames = []
for team in teamTags: 
    fileName = './individualTeams/' + team + '_data.csv'
    os.makedirs(os.path.dirname(fileName), exist_ok=True)
    teamFrames = []
    for year in years:
        data = pybb.schedule_and_record(year, team)
        teamFrames.append(data)
    result = pd.concat(teamFrames)
    #Drop columns that we cannot know before the game has occurred
    refinedResult = result.drop(columns=['W/L', 'Inn', 'Win', 'Loss', 'Save', 'Time', 'Attendance', 'cLI', 'Orig. Scheduled'])
    #Todo!!! clean data to make sure all columns have usable data
    cleanedResult = refinedResult
    allFrames.append(cleanedResult)
    cleanedResult.to_csv(fileName)
result = pd.concat(allFrames)
#Go through and delete dulplicate games by keeping only home games
cleanedResult = result[result['Home_Away'] == 'Home']
#Delete Home_Away column because we know team under Tm column is always Home
refinedResult = cleanedResult.drop(columns=['Home_Away'])
cleanedResult.to_csv('allTeams_data.csv')