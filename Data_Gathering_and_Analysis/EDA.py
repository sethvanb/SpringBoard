import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn

def detect_outliers(data):
    outliers = []
    threshold = 3
    mean = np.mean(data)
    std = np.std(data)

    for i in data:
        z_score = (i - mean)/std
        if np.abs(z_score) > threshold:
            outliers.append(i)
    return outliers

def count_rows(rows):
    return len(rows)

# data = pd.read_csv('individualTeams/SFG_data.csv')
# data = data[0:500]
# seaborn.lineplot(data=data, x=list(range(len(data))), y="R")
# plt.show()

data = pd.read_csv('allTeams_data.csv')

# Standardize or Normalize  Wins, Losses, Runs?, W-L, GB, Streak, Rank

#Basic data information
print(data.info())
print(data.head())
print("-----MIN-----")
print(data.min())
print("-----MAX-----")
print(data.max())

print(data)

#Plotting data and looking for Outliers in R, W-L, GB, Streak, Wins, Losses
#Histograms
fig, axes = plt.subplots(3, 2)
data["R"].plot(kind='hist',
        alpha=0.7,
        bins=30,
        title='Runs',
        rot=45,
        grid=True,
        figsize=(12,8),
        fontsize=15, 
        color=['#A0E8AF', '#FFCF56'],
        ax=axes[0,0])
data["W-L"].plot(kind='hist',
        alpha=0.7,
        bins=50,
        title='Win to Loss Ratio',
        rot=45,
        grid=True,
        figsize=(12,8),
        fontsize=15, 
        color=['#A0E8AF', '#FFCF56'],
        ax=axes[0,1])
data["GB"].plot(kind='hist',
        alpha=0.7,
        bins=70,
        title='Games Back',
        rot=45,
        grid=True,
        figsize=(12,8),
        fontsize=15, 
        color=['#A0E8AF', '#FFCF56'],
        ax=axes[1,0])
data["Streak"].plot(kind='hist',
        alpha=0.7,
        bins=42,
        title='Streak',
        rot=45,
        grid=True,
        figsize=(12,8),
        fontsize=15, 
        color=['#A0E8AF', '#FFCF56'],
        ax=axes[1,1])
data["Wins"].plot(kind='hist',
        alpha=0.7,
        bins=108,
        title='Wins',
        rot=45,
        grid=True,
        figsize=(12,8),
        fontsize=15, 
        color=['#A0E8AF', '#FFCF56'],
        ax=axes[2,0])
data["Losses"].plot(kind='hist',
        alpha=0.7,
        bins=116,
        title='Losses',
        rot=45,
        grid=True,
        figsize=(12,8),
        fontsize=15, 
        color=['#A0E8AF', '#FFCF56'],
        ax=axes[2,1])
plt.show()

#Finding Outliers
r_out = detect_outliers(data["R"])
print(len(r_out))
wl_out = detect_outliers(data["W-L"])
print(len(wl_out))
gb_out = detect_outliers(data["GB"])
print(len(gb_out))
streak_out = detect_outliers(data["Streak"])
print(len(streak_out))
w_out = detect_outliers(data["Wins"])
print(len(w_out))
l_out = detect_outliers(data["Losses"])
print(len(l_out))

# Remove Outliers
data = data[~data['R'].isin(r_out)]
data = data[~data['W-L'].isin(wl_out)]
data = data[~data['GB'].isin(gb_out)]
data = data[~data['Streak'].isin(streak_out)]
data = data[~data['Wins'].isin(w_out)]
data = data[~data['Losses'].isin(l_out)]

#Plotting Scatter Plots
fig, axes = plt.subplots(3, 2)
seaborn.scatterplot(data=data, ax=axes[0,0], x="W-L", y="R")
seaborn.scatterplot(data=data, ax=axes[0,1], x="GB", y="R")
seaborn.scatterplot(data=data, ax=axes[1,0], x="Streak", y="R")
seaborn.scatterplot(data=data, ax=axes[2,0], x="Wins", y="R")
seaborn.scatterplot(data=data, ax=axes[2,1], x="Losses", y="R")
plt.show()

#Plotting Heat Maps
fig, axes = plt.subplots(3, 2)
runs_wl = data.groupby(["R", "W-L"]).apply(count_rows).unstack()
seaborn.heatmap(runs_wl, ax=axes[0,0])
runs_gb = data.groupby(["R", "GB"]).apply(count_rows).unstack()
seaborn.heatmap(runs_gb, ax=axes[0,1])
runs_streak = data.groupby(["R", "Streak"]).apply(count_rows).unstack()
seaborn.heatmap(runs_streak, ax=axes[1,0])
runs_wins = data.groupby(["R", "Wins"]).apply(count_rows).unstack()
seaborn.heatmap(runs_wins, ax=axes[2,0])
runs_losses = data.groupby(["R", "Losses"]).apply(count_rows).unstack()
seaborn.heatmap(runs_losses, ax=axes[2,1])
plt.show()

# One Hot Encode Tm and Opp
data['Tm'] = data['Tm'].map({0:'ARI', 1:'ATL', 2:'BAL', 3:'BOS', 4:'CHC', 5:'CHW', 6:'CIN', 7:'CLE', 8:'COL', 9:'DET', 10:'HOU', 11:'KCR', 12:'LAA', 13:'LAD', 14:'MIA', 15:'MIL', 16:'MIN', 17:'NYM', 18:'NYY', 19:'OAK', 20:'PHI', 21:'PIT', 22:'SDP', 23:'SEA', 24:'SFG', 25:'STL', 26:'TBR', 27:'TEX', 28:'TOR', 29:'WSN'})
data = pd.get_dummies(data, columns=['Tm'], prefix='', prefix_sep='')
data['Opp'] = data['Opp'].map({0:'OPP_ARI', 1:'OPP_ATL', 2:'OPP_BAL', 3:'OPP_BOS', 4:'OPP_CHC', 5:'OPP_CHW', 6:'OPP_CIN', 7:'OPP_CLE', 8:'OPP_COL', 9:'OPP_DET', 10:'OPP_HOU', 11:'OPP_KCR', 12:'OPP_LAA', 13:'OPP_LAD', 14:'OPP_MIA', 15:'OPP_MIL', 16:'OPP_MIN', 17:'OPP_NYM', 18:'OPP_NYY', 19:'OPP_OAK', 20:'OPP_PHI', 21:'OPP_PIT', 22:'OPP_SDP', 23:'OPP_SEA', 24:'OPP_SFG', 25:'OPP_STL', 26:'OPP_TBR', 27:'OPP_TEX', 28:'OPP_TOR', 29:'OPP_WSN'})
data = pd.get_dummies(data, columns=['Opp'], prefix='', prefix_sep='')

print(data['R'].value_counts())
print(data.shape[0])
print((data['R']==3).sum()/data.shape[0])

# data = data.drop(columns = ['Date'])
data.drop(columns=['Unnamed: 0']).to_csv('allTeams_data.csv')
print(data.drop(columns=['Unnamed: 0']))
# data.to_csv('allTeams_data.csv')
