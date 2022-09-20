import pybaseball as pybb
import json
import datetime as dt
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct']

def dailyGames():
  teamTags=['ARI', 'ATL', 'BAL', 'BOS', 'CHC', 'CHW', 'CIN', 'CLE', 'COL', 'DET', 'HOU', 'KCR', 'LAA', 'LAD', 'MIA', 'MIL', 'MIN', 'NYM', 'NYY', 'OAK', 'PHI', 'PIT', 'SDP', 'SEA', 'SFG', 'STL', 'TBR', 'TEX', 'TOR', 'WSN']
  teamTagName={'ARI':'Diamondbacks', 'ATL':'Braves', 'BAL':'Orioles', 'BOS':'Red Sox', 'CHC':'Cubs', 'CHW':'White Sox', 'CIN':'Reds', 'CLE':'Gaurdians', 'COL':'Rockies', 'DET':'Tigers', 'HOU':'Astros', 'KCR':'Royals', 'LAA':'Angels', 'LAD':'Dodgers', 'MIA':'Marlins', 'MIL':'Brewers', 'MIN':'Twins', 'NYM':'Mets', 'NYY':'Yankees', 'OAK':'Athletics', 'PHI':'Phillies', 'PIT':'Pirates', 'SDP':'Padres', 'SEA':'Mariners', 'SFG':'Giants', 'STL':'Cardinals', 'TBR':'Rays', 'TEX':'Rangers', 'TOR':'Blue Jays', 'WSN':'Nationals'}
  current_date = dt.date.today()
  games = []
  for team in teamTags:
    data = pybb.schedule_and_record(current_date.year, team)
    nextGameIndex = data[data.GB.isnull()].head(1).index[0] - 1

    d = data.iat[nextGameIndex, 0]
    month = d[d.find(',')+2:d.find(',')+5]
    if d.find('(') == -1:
      day = d[d.find(',')+6:len(d)]
    else:
      day = d[d.find(',')+6:d.find('(')]
    date = dt.date(current_date.year, months.index(month)+1, int(day))

    if date == current_date and data.iloc[nextGameIndex, 2] == 'Home':
      home = data.iloc[nextGameIndex, 1]
      away = data.iloc[nextGameIndex, 3]
      games.insert(-1, {'value': home + '-' + away, 'text': teamTagName[home] + ' vs ' + teamTagName[away]})

  # games = {'results':[{'value': "SFG-LAD", 'text': "Giants vs Dodgers"}, {'value': "OAK-LAA", 'text': "A's vs Angels"}]}
  print({ 'results': games })

if __name__ == '__main__':
  dailyGames()
