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
data['Tm'] = data['Tm'].map({1:'ARI', 2:'ATL', 3:'BAL', 4:'BOS', 5:'CHC', 6:'CHW', 7:'CIN', 8:'CLE', 9:'COL', 10:'DET', 11:'HOU', 12:'KCR', 13:'LAA', 14:'LAD', 15:'MIA', 16:'MIL', 17:'MIN', 18:'NYM', 19:'NYY', 20:'OAK', 21:'PHI', 22:'PIT', 23:'SDP', 24:'SEA', 25:'SFG', 26:'STL', 27:'TBR', 28:'TEX', 29:'TOR', 30:'WSN'})
data = pd.get_dummies(data, columns=['Tm'], prefix='', prefix_sep='')
data['Opp'] = data['Opp'].map({1:'OPP_ARI', 2:'OPP_ATL', 3:'OPP_BAL', 4:'OPP_BOS', 5:'OPP_CHC', 6:'OPP_CHW', 7:'OPP_CIN', 8:'OPP_CLE', 9:'OPP_COL', 10:'OPP_DET', 11:'OPP_HOU', 12:'OPP_KCR', 13:'OPP_LAA', 14:'OPP_LAD', 15:'OPP_MIA', 16:'OPP_MIL', 17:'OPP_MIN', 18:'OPP_NYM', 19:'OPP_NYY', 20:'OPP_OAK', 21:'OPP_PHI', 22:'OPP_PIT', 23:'OPP_SDP', 24:'OPP_SEA', 25:'OPP_SFG', 26:'OPP_STL', 27:'OPP_TBR', 28:'OPP_TEX', 29:'OPP_TOR', 30:'OPP_WSN'})
data = pd.get_dummies(data, columns=['Opp'], prefix='', prefix_sep='')

print(data['R'].value_counts())
print(data.shape[0])
print((data['R']==3).sum()/data.shape[0])

# data = data.drop(columns = ['Date'])
data.drop(columns=['Unnamed: 0']).to_csv('allTeams_data.csv')
print(data.drop(columns=['Unnamed: 0']))
# data.to_csv('allTeams_data.csv')
