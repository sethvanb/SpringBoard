# import pandas as pd
import numpy as np
import sys
import pybaseball as pybb
import datetime as dt
import googleapiclient.discovery
from google.api_core.client_options import ClientOptions
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct']

def inference():
  current_date = dt.date.today()

  # Get Away Teams Next Game Data
  data = pybb.schedule_and_record(current_date.year, sys.argv[1])
  nextHomeIndex = data[data.GB.isnull()].head(1).index[0] - 1

  data["Wins"] = 1
  data["Losses"] = 0
  data["DoubleHeader"] = 0
  data = data.assign(R1=data["R"])
  data["R1"] = data["R1"].shift(periods=1, fill_value=data["R"].mean())
  data["R3"] = np.nan
  for i in range(len(data)-1, -1, -1):
    if i >= 3:
        data.iat[i, 24] = (data.iat[i-1, 5] + data.iat[i-2, 5] + data.iat[i-3, 5])/3
    elif i == 2:
        data.iat[i, 24] = (data.iat[i-1, 5] + data.iat[i-2, 5])/2
    elif i == 1:
        data.iat[i, 24] = data.iat[i-1, 5]
    elif i == 0:
        data.iat[i, 24] = data["R3"].mean()

  data["R5"] = np.nan
  for i in range(len(data)-1, -1, -1):
    if i >= 5:
        data.iat[i, 25] = (data.iat[i-1, 5] + data.iat[i-2, 5] + data.iat[i-3, 5] + data.iat[i-4, 5] + data.iat[i-5, 5])/5
    elif i == 4:
        data.iat[i, 25] = (data.iat[i-1, 5] + data.iat[i-2, 5] + data.iat[i-3, 5] + data.iat[i-4, 5])/4
    elif i == 3:
        data.iat[i, 25] = (data.iat[i-1, 5] + data.iat[i-2, 5] + data.iat[i-3, 5])/3
    elif i == 2:
        data.iat[i, 25] = (data.iat[i-1, 5] + data.iat[i-2, 5])/2
    elif i == 1:
        data.iat[i, 25] = data.iat[i-1, 5]
    elif i == 0:
        data.iat[i, 25] = data["R5"].mean()

  data["R7"] = np.nan
  for i in range(len(data)-1, -1, -1):
    if i >= 7:
        data.iat[i, 26] = (data.iat[i-1, 5] + data.iat[i-2, 5] + data.iat[i-3, 5] + data.iat[i-4, 5] + data.iat[i-5, 5] + data.iat[i-6, 5] + data.iat[i-7, 5])/7
    elif i == 6:
        data.iat[i, 26] = (data.iat[i-1, 5] + data.iat[i-2, 5] + data.iat[i-3, 5] + data.iat[i-4, 5] + data.iat[i-5, 5] + data.iat[i-6, 5])/6
    elif i == 5:
        data.iat[i, 26] = (data.iat[i-1, 5] + data.iat[i-2, 5] + data.iat[i-3, 5] + data.iat[i-4, 5] + data.iat[i-5, 5])/5
    elif i == 4:
        data.iat[i, 26] = (data.iat[i-1, 5] + data.iat[i-2, 5] + data.iat[i-3, 5] + data.iat[i-4, 5])/4
    elif i == 3:
        data.iat[i, 26] = (data.iat[i-1, 5] + data.iat[i-2, 5] + data.iat[i-3, 5])/3
    elif i == 2:
        data.iat[i, 26] = (data.iat[i-1, 5] + data.iat[i-2, 5])/2
    elif i == 1:
        data.iat[i, 26] = data.iat[i-1, 5]
    elif i == 0:
        data.iat[i, 26] = data["R7"].mean()

  data["R10"] = np.nan
  for i in range(len(data)-1, -1, -1):
    if i >= 10:
        data.iat[i, 27] = (data.iat[i-1, 5] + data.iat[i-2, 5] + data.iat[i-3, 5] + data.iat[i-4, 5] + data.iat[i-5, 5] + data.iat[i-6, 5] + data.iat[i-7, 5] + data.iat[i-8, 5] + data.iat[i-9, 5] + data.iat[i-10, 5])/10
    elif i == 9:
        data.iat[i, 27] = (data.iat[i-1, 5] + data.iat[i-2, 5] + data.iat[i-3, 5] + data.iat[i-4, 5] + data.iat[i-5, 5] + data.iat[i-6, 5] + data.iat[i-7, 5] + data.iat[i-8, 5] + data.iat[i-9, 5])/9
    elif i == 8:
        data.iat[i, 27] = (data.iat[i-1, 5] + data.iat[i-2, 5] + data.iat[i-3, 5] + data.iat[i-4, 5] + data.iat[i-5, 5] + data.iat[i-6, 5] + data.iat[i-7, 5] + data.iat[i-8, 5])/8
    elif i == 7:
        data.iat[i, 27] = (data.iat[i-1, 5] + data.iat[i-2, 5] + data.iat[i-3, 5] + data.iat[i-4, 5] + data.iat[i-5, 5] + data.iat[i-6, 5] + data.iat[i-7, 5])/7
    elif i == 6:
        data.iat[i, 27] = (data.iat[i-1, 5] + data.iat[i-2, 5] + data.iat[i-3, 5] + data.iat[i-4, 5] + data.iat[i-5, 5] + data.iat[i-6, 5])/6
    elif i == 5:
        data.iat[i, 27] = (data.iat[i-1, 5] + data.iat[i-2, 5] + data.iat[i-3, 5] + data.iat[i-4, 5] + data.iat[i-5, 5])/5
    elif i == 4:
        data.iat[i, 27] = (data.iat[i-1, 5] + data.iat[i-2, 5] + data.iat[i-3, 5] + data.iat[i-4, 5])/4
    elif i == 3:
        data.iat[i, 27] = (data.iat[i-1, 5] + data.iat[i-2, 5] + data.iat[i-3, 5])/3
    elif i == 2:
        data.iat[i, 27] = (data.iat[i-1, 5] + data.iat[i-2, 5])/2
    elif i == 1:
        data.iat[i, 27] = data.iat[i-1, 5]
    elif i == 0:
        data.iat[i, 27] = data["R10"].mean()

  data = data.drop(columns=['R', 'Tm', 'Opp', 'W/L', 'Inn', 'RA', 'Win', 'Loss', 'Save', 'Time', 'Attendance', 'cLI', 'Orig. Scheduled', 'D/N', 'Streak', 'Rank', 'GB'])

  if data.iat[nextHomeIndex, 0] == data.iat[nextHomeIndex+1, 0] or data.iat[nextHomeIndex, 0] == data.iat[nextHomeIndex-1, 0]:
    data.iat[nextHomeIndex, 5] == 1
  d = data.iat[nextHomeIndex, 0]
  month = d[d.find(',')+2:d.find(',')+5]
  if d.find('(') == -1:
    day = d[d.find(',')+6:len(d)]
  else:
    day = d[d.find(',')+6:d.find('(')]
  date = dt.datetime(current_date.year, months.index(month)+1, int(day))
  data.iat[nextHomeIndex, 0] = int(date.strftime("%Y%m%d"))
  data.iat[nextHomeIndex, 1] = 0 if data.iat[nextHomeIndex, 1] == 'Home' else 1
  wl = data.iat[nextHomeIndex-1, 2] 
  wins = float(wl[0:wl.find('-')])
  losses = float(wl[wl.find('-')+1:len(wl)])
  if losses != 0:
    data.iat[nextHomeIndex, 2] = wins/losses
  else:
    data.iat[nextHomeIndex, 2] = wins
  data.iat[nextHomeIndex, 3] = wins
  data.iat[nextHomeIndex, 4] = losses

  teamTags = ['ARI', 'ATL', 'BAL', 'BOS', 'CHC', 'CHW', 'CIN', 'CLE', 'COL', 'DET', 'HOU', 'KCR', 'LAA', 'LAD', 'MIA', 'MIL', 'MIN', 'NYM', 'NYY', 'OAK', 'PHI', 'PIT', 'SDP', 'SEA', 'SFG', 'STL', 'TBR', 'TEX', 'TOR']
  oppTags = ['OPP_ARI', 'OPP_ATL', 'OPP_BAL', 'OPP_BOS', 'OPP_CHC', 'OPP_CHW', 'OPP_CIN', 'OPP_CLE', 'OPP_COL', 'OPP_DET', 'OPP_HOU', 'OPP_KCR', 'OPP_LAA', 'OPP_LAD', 'OPP_MIA', 'OPP_MIL', 'OPP_MIN', 'OPP_NYM', 'OPP_NYY', 'OPP_OAK', 'OPP_PHI', 'OPP_PIT', 'OPP_SDP', 'OPP_SEA', 'OPP_SFG', 'OPP_STL', 'OPP_TBR', 'OPP_TEX', 'OPP_TOR']

  for tag in teamTags:
    data[tag] = 0
  data._set_value(nextHomeIndex+1, sys.argv[1], 1)

  for tag in oppTags:
    data[tag] = 0
  data._set_value(nextHomeIndex+1, 'OPP_' + sys.argv[2], 1)

  # Get Away Teams Next Game Data
  data2 = pybb.schedule_and_record(current_date.year, sys.argv[2])
  nextAwayIndex = data2[data2.GB.isnull()].head(1).index[0] - 1

  data2["Wins"] = 1
  data2["Losses"] = 0
  data2["DoubleHeader"] = 0
  data2 = data2.assign(R1=data2["R"])
  data2["R1"] = data2["R1"].shift(periods=1, fill_value=data2["R"].mean())
  data2["R3"] = np.nan
  for i in range(len(data2)-1, -1, -1):
    if i >= 3:
        data2.iat[i, 24] = (data2.iat[i-1, 5] + data2.iat[i-2, 5] + data2.iat[i-3, 5])/3
    elif i == 2:
        data2.iat[i, 24] = (data2.iat[i-1, 5] + data2.iat[i-2, 5])/2
    elif i == 1:
        data2.iat[i, 24] = data2.iat[i-1, 5]
    elif i == 0:
        data2.iat[i, 24] = data2["R3"].mean()

  data2["R5"] = np.nan
  for i in range(len(data2)-1, -1, -1):
    if i >= 5:
        data2.iat[i, 25] = (data2.iat[i-1, 5] + data2.iat[i-2, 5] + data2.iat[i-3, 5] + data2.iat[i-4, 5] + data2.iat[i-5, 5])/5
    elif i == 4:
        data2.iat[i, 25] = (data2.iat[i-1, 5] + data2.iat[i-2, 5] + data2.iat[i-3, 5] + data2.iat[i-4, 5])/4
    elif i == 3:
        data2.iat[i, 25] = (data2.iat[i-1, 5] + data2.iat[i-2, 5] + data2.iat[i-3, 5])/3
    elif i == 2:
        data2.iat[i, 25] = (data2.iat[i-1, 5] + data2.iat[i-2, 5])/2
    elif i == 1:
        data2.iat[i, 25] = data2.iat[i-1, 5]
    elif i == 0:
        data2.iat[i, 25] = data2["R5"].mean()

  data2["R7"] = np.nan
  for i in range(len(data2)-1, -1, -1):
    if i >= 7:
        data2.iat[i, 26] = (data2.iat[i-1, 5] + data2.iat[i-2, 5] + data2.iat[i-3, 5] + data2.iat[i-4, 5] + data2.iat[i-5, 5] + data2.iat[i-6, 5] + data2.iat[i-7, 5])/7
    elif i == 6:
        data2.iat[i, 26] = (data2.iat[i-1, 5] + data2.iat[i-2, 5] + data2.iat[i-3, 5] + data2.iat[i-4, 5] + data2.iat[i-5, 5] + data2.iat[i-6, 5])/6
    elif i == 5:
        data2.iat[i, 26] = (data2.iat[i-1, 5] + data2.iat[i-2, 5] + data2.iat[i-3, 5] + data2.iat[i-4, 5] + data2.iat[i-5, 5])/5
    elif i == 4:
        data2.iat[i, 26] = (data2.iat[i-1, 5] + data2.iat[i-2, 5] + data2.iat[i-3, 5] + data2.iat[i-4, 5])/4
    elif i == 3:
        data2.iat[i, 26] = (data2.iat[i-1, 5] + data2.iat[i-2, 5] + data2.iat[i-3, 5])/3
    elif i == 2:
        data2.iat[i, 26] = (data2.iat[i-1, 5] + data2.iat[i-2, 5])/2
    elif i == 1:
        data2.iat[i, 26] = data2.iat[i-1, 5]
    elif i == 0:
        data2.iat[i, 26] = data2["R7"].mean()

  data2["R10"] = np.nan
  for i in range(len(data2)-1, -1, -1):
    if i >= 10:
        data2.iat[i, 27] = (data2.iat[i-1, 5] + data2.iat[i-2, 5] + data2.iat[i-3, 5] + data2.iat[i-4, 5] + data2.iat[i-5, 5] + data2.iat[i-6, 5] + data2.iat[i-7, 5] + data2.iat[i-8, 5] + data2.iat[i-9, 5] + data2.iat[i-10, 5])/10
    elif i == 9:
        data2.iat[i, 27] = (data2.iat[i-1, 5] + data2.iat[i-2, 5] + data2.iat[i-3, 5] + data2.iat[i-4, 5] + data2.iat[i-5, 5] + data2.iat[i-6, 5] + data2.iat[i-7, 5] + data2.iat[i-8, 5] + data2.iat[i-9, 5])/9
    elif i == 8:
        data2.iat[i, 27] = (data2.iat[i-1, 5] + data2.iat[i-2, 5] + data2.iat[i-3, 5] + data2.iat[i-4, 5] + data2.iat[i-5, 5] + data2.iat[i-6, 5] + data2.iat[i-7, 5] + data2.iat[i-8, 5])/8
    elif i == 7:
        data2.iat[i, 27] = (data2.iat[i-1, 5] + data2.iat[i-2, 5] + data2.iat[i-3, 5] + data2.iat[i-4, 5] + data2.iat[i-5, 5] + data2.iat[i-6, 5] + data2.iat[i-7, 5])/7
    elif i == 6:
        data2.iat[i, 27] = (data2.iat[i-1, 5] + data2.iat[i-2, 5] + data2.iat[i-3, 5] + data2.iat[i-4, 5] + data2.iat[i-5, 5] + data2.iat[i-6, 5])/6
    elif i == 5:
        data2.iat[i, 27] = (data2.iat[i-1, 5] + data2.iat[i-2, 5] + data2.iat[i-3, 5] + data2.iat[i-4, 5] + data2.iat[i-5, 5])/5
    elif i == 4:
        data2.iat[i, 27] = (data2.iat[i-1, 5] + data2.iat[i-2, 5] + data2.iat[i-3, 5] + data2.iat[i-4, 5])/4
    elif i == 3:
        data2.iat[i, 27] = (data2.iat[i-1, 5] + data2.iat[i-2, 5] + data2.iat[i-3, 5])/3
    elif i == 2:
        data2.iat[i, 27] = (data2.iat[i-1, 5] + data2.iat[i-2, 5])/2
    elif i == 1:
        data2.iat[i, 27] = data2.iat[i-1, 5]
    elif i == 0:
        data2.iat[i, 27] = data2["R10"].mean()

  data2 = data2.drop(columns=['R', 'Tm', 'Opp', 'W/L', 'Inn', 'RA', 'Win', 'Loss', 'Save', 'Time', 'Attendance', 'cLI', 'Orig. Scheduled', 'D/N', 'Streak', 'Rank', 'GB'])

  if data2.iat[nextAwayIndex, 0] == data2.iat[nextAwayIndex+1, 0] or data2.iat[nextAwayIndex, 0] == data2.iat[nextAwayIndex-1, 0]:
    data2.iat[nextAwayIndex, 5] == 1
  d = data2.iat[nextAwayIndex, 0]
  month = d[d.find(',')+2:d.find(',')+5]
  if d.find('(') == -1:
    day = d[d.find(',')+6:len(d)]
  else:
    day = d[d.find(',')+6:d.find('(')]
  date = dt.datetime(current_date.year, months.index(month)+1, int(day))
  data2.iat[nextAwayIndex, 0] = int(date.strftime("%Y%m%d"))
  data2.iat[nextAwayIndex, 1] = 0 if data2.iat[nextAwayIndex, 1] == 'Home' else 1
  wl = data2.iat[nextAwayIndex-1, 2] 
  wins = float(wl[0:wl.find('-')])
  losses = float(wl[wl.find('-')+1:len(wl)])
  if losses != 0:
    data2.iat[nextAwayIndex, 2] = wins/losses
  else:
    data2.iat[nextAwayIndex, 2] = wins
  data2.iat[nextAwayIndex, 3] = wins
  data2.iat[nextAwayIndex, 4] = losses

  teamTags = ['ARI', 'ATL', 'BAL', 'BOS', 'CHC', 'CHW', 'CIN', 'CLE', 'COL', 'DET', 'HOU', 'KCR', 'LAA', 'LAD', 'MIA', 'MIL', 'MIN', 'NYM', 'NYY', 'OAK', 'PHI', 'PIT', 'SDP', 'SEA', 'SFG', 'STL', 'TBR', 'TEX', 'TOR']
  oppTags = ['OPP_ARI', 'OPP_ATL', 'OPP_BAL', 'OPP_BOS', 'OPP_CHC', 'OPP_CHW', 'OPP_CIN', 'OPP_CLE', 'OPP_COL', 'OPP_DET', 'OPP_HOU', 'OPP_KCR', 'OPP_LAA', 'OPP_LAD', 'OPP_MIA', 'OPP_MIL', 'OPP_MIN', 'OPP_NYM', 'OPP_NYY', 'OPP_OAK', 'OPP_PHI', 'OPP_PIT', 'OPP_SDP', 'OPP_SEA', 'OPP_SFG', 'OPP_STL', 'OPP_TBR', 'OPP_TEX', 'OPP_TOR']

  for tag in teamTags:
    data2[tag] = 0
  data2._set_value(nextAwayIndex+1, sys.argv[2], 1)

  for tag in oppTags:
    data2[tag] = 0
  data2._set_value(nextAwayIndex+1, 'OPP_' + sys.argv[1], 1)

#   print(data.iloc[nextHomeIndex]) 
#   print(data.iloc[nextAwayIndex]) 
#   instances = [[0.0, 20020401.0, 0.0, 0.0, 0.0, 0.0, 0.0, 5.055555555555555, 4.951345755693582, 4.944720496894409, 4.954362614611062, 4.953795721187026, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]
  instances = [np.insert(data.iloc[nextHomeIndex].values, 0, 0).astype(float).tolist(), np.insert(data2.iloc[nextAwayIndex].values, 0, 0).astype(float).tolist()]
  
  results = predict_json("spring-board-348123", "us-central1", "mlb_ml_model", instances, "V1")
  print(results[0])
  print(results[1])

def predict_json(project, region, model, instances, version=None):
    prefix = "{}-ml".format(region) if region else "ml"
    api_endpoint = "https://{}.googleapis.com".format(prefix)
    client_options = ClientOptions(api_endpoint=api_endpoint)
    service = googleapiclient.discovery.build(
        'ml', 'v1', client_options=client_options)
    name = 'projects/{}/models/{}'.format(project, model)

    if version is not None:
        name += '/versions/{}'.format(version)

    response = service.projects().predict(
        name=name,
        body={'instances': instances}
    ).execute()

    if 'error' in response:
        raise RuntimeError(response['error'])

    return response['predictions']

if __name__ == '__main__':
  inference()
