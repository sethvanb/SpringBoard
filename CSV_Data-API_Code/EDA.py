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

data = pd.read_csv('allTeams_data.csv')

# #Basic data information
# print(data.info())
# print(data.head())
# print("-----MIN-----")
# print(data.min())
# print("-----MAX-----")
# print(data.max())

# #Plotting data and looking for Outliers in R, W-L, GB, Streak, Wins, Losses
# #Histograms
# fig, axes = plt.subplots(3, 2)
# data["R"].plot(kind='hist',
#         alpha=0.7,
#         bins=30,
#         title='Runs',
#         rot=45,
#         grid=True,
#         figsize=(12,8),
#         fontsize=15, 
#         color=['#A0E8AF', '#FFCF56'],
#         ax=axes[0,0])
# data["W-L"].plot(kind='hist',
#         alpha=0.7,
#         bins=50,
#         title='Win to Loss Ratio',
#         rot=45,
#         grid=True,
#         figsize=(12,8),
#         fontsize=15, 
#         color=['#A0E8AF', '#FFCF56'],
#         ax=axes[0,1])
# data["GB"].plot(kind='hist',
#         alpha=0.7,
#         bins=70,
#         title='Games Back',
#         rot=45,
#         grid=True,
#         figsize=(12,8),
#         fontsize=15, 
#         color=['#A0E8AF', '#FFCF56'],
#         ax=axes[1,0])
# data["Streak"].plot(kind='hist',
#         alpha=0.7,
#         bins=42,
#         title='Streak',
#         rot=45,
#         grid=True,
#         figsize=(12,8),
#         fontsize=15, 
#         color=['#A0E8AF', '#FFCF56'],
#         ax=axes[1,1])
# data["Wins"].plot(kind='hist',
#         alpha=0.7,
#         bins=108,
#         title='Wins',
#         rot=45,
#         grid=True,
#         figsize=(12,8),
#         fontsize=15, 
#         color=['#A0E8AF', '#FFCF56'],
#         ax=axes[2,0])
# data["Losses"].plot(kind='hist',
#         alpha=0.7,
#         bins=116,
#         title='Losses',
#         rot=45,
#         grid=True,
#         figsize=(12,8),
#         fontsize=15, 
#         color=['#A0E8AF', '#FFCF56'],
#         ax=axes[2,1])
# plt.show()

# r_out = detect_outliers(data["R"])
# print(r_out)
# wl_out = detect_outliers(data["W-L"])
# print(wl_out)
# gb_out = detect_outliers(data["GB"])
# print(gb_out)
# streak_out = detect_outliers(data["Streak"])
# print(streak_out)
# w_out = detect_outliers(data["Wins"])
# print(w_out)
# l_out = detect_outliers(data["Losses"])
# print(l_out)

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



