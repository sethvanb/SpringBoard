import pybaseball as pybb
import pandas as pd
import os
import datetime as dt
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct']

# For all 30 MLB teams we will gather 10 years of records 2012-2021 and save them into a cvs for each team and one aggrgated one. 
years = [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
teamTags=['ARI', 'ATL', 'BAL', 'BOS', 'CHC', 'CHW', 'CIN', 'CLE', 'COL', 'DET', 'HOU', 'KCR', 'LAA', 'LAD', 'MIA', 'MIL', 'MIN', 'NYM', 'NYY', 'OAK', 'PHI', 'PIT', 'SDP', 'SEA', 'SFG', 'STL', 'TBR', 'TEX', 'TOR', 'WSN']

# years = [2021]
# teamTags=['SFG'] 

#Collect all the data frames for each team and each year and put them into one data frame
allFrames = []
for team in teamTags: 
    fileName = './individualTeams/' + team + '_data.csv'
    os.makedirs(os.path.dirname(fileName), exist_ok=True)
    teamFrames = []
    for year in years:
        data = pybb.schedule_and_record(year, team)
        #Drop columns that we cannot know before the game has occurred
        cleanedResult = data.drop(columns=['W/L', 'Inn', 'RA', 'Win', 'Loss', 'Save', 'Time', 'Attendance', 'cLI', 'Orig. Scheduled'])
        #Add wins and losses columns 
        cleanedResult["Wins"] = 1
        cleanedResult["Losses"] = 0
        cleanedResult["DoubleHeader"] = 0
        #Clean data to make sure all columns have usable data, change catergorcal and date elements into numerical inputs
        for i in range(len(cleanedResult)-1, -1, -1): 
            #Convert Date to number 
            d = cleanedResult.iat[i, 0]
            month = d[d.find(',')+2:d.find(',')+5]
            if d.find('(') == -1:
                day = d[d.find(',')+6:len(d)]
            else:
                day = d[d.find(',')+6:d.find('(')]
            date = dt.datetime(year, months.index(month)+1, int(day))
            cleanedResult.iat[i, 0] =  int(date.strftime("%Y%m%d")) #Date to number 
            cleanedResult.iat[i, 1] = teamTags.index(cleanedResult.iat[i, 1]) #Team to tag index
            cleanedResult.iat[i, 2] = 0 if cleanedResult.iat[i, 2] == 'Home' else 1 #Home/Away to bool
            cleanedResult.iat[i, 3] = teamTags.index(cleanedResult.iat[i, 3])  #Opponent to tag index
            # Change win-loss to win/loss ratio and add win and loss column
            wl = cleanedResult.iat[i, 5] 
            wins = float(wl[0:wl.find('-')])
            losses = float(wl[wl.find('-')+1:len(wl)])
            if losses != 0:
                cleanedResult.iat[i, 5] = wins/losses
            else:
                cleanedResult.iat[i, 5] = wins
            cleanedResult.iat[i, 10] = wins
            cleanedResult.iat[i, 11] = losses
            # Change games back tied to 0 and up to negative numbers
            if cleanedResult.iat[i, 7] == 'Tied':
                cleanedResult.iat[i, 7] = 0
            elif cleanedResult.iat[i, 7][0:2] == 'up':
                cleanedResult.iat[i, 7] = -1 * float(cleanedResult.iat[i, 7][3:len(cleanedResult.iat[i, 7])])
            cleanedResult.iat[i, 8] = 0 if cleanedResult.iat[i, 8] == 'D' else 1 #Day/Night to bool

        for i in range(len(cleanedResult)-1, -1, -1):  
            if i != 0 and cleanedResult.iat[i, 0] == cleanedResult.iat[i-1, 0]: # Add bool for double header
                cleanedResult.iat[i, 12] = 1
                cleanedResult.iat[i-1, 12] = 1
            if i != 0: # Shift all "in coming" stats down a column
                cleanedResult.iat[i, 5] = cleanedResult.iat[i-1, 5] # Shift win-loss ratio down a column
                cleanedResult.iat[i, 6] = cleanedResult.iat[i-1, 6] # Shift rank down a column
                cleanedResult.iat[i, 7] = cleanedResult.iat[i-1, 7] # Shift games back down a column
                cleanedResult.iat[i, 9] = cleanedResult.iat[i-1, 9] # Shift streak down a column
                cleanedResult.iat[i, 10] = cleanedResult.iat[i-1, 10] # Shift wins down a column
                cleanedResult.iat[i, 11] = cleanedResult.iat[i-1, 11] # Shift losses down a column
            else: #set first record to initial values
                cleanedResult.iat[i, 5] = 0
                cleanedResult.iat[i, 6] = 1
                cleanedResult.iat[i, 7] = 0
                cleanedResult.iat[i, 9] = 0
                cleanedResult.iat[i, 10] = 0
                cleanedResult.iat[i, 11] = 0

        teamFrames.append(cleanedResult)
    result = pd.concat(teamFrames)
    allFrames.append(result)
    result.to_csv(fileName)
    print(fileName) # To let user know which files are done
result = pd.concat(allFrames)
# Do we really wnat to do this?
#Go through and delete dulplicate games by keeping only home games
# cleanedResult = result[result['Home_Away'] == 0]
#Delete Home_Away column because we know team under Tm column is always Home
# refinedResult = cleanedResult.drop(columns=['Home_Away'])
# refinedResult.to_csv('allTeams_data.csv')
result.to_csv('allTeams_data.csv')