# from xgboost import XGBRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import pandas as pd
from joblib import dump

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

def train():
  data = pd.read_csv('allTeams_data.csv')
  X = data.drop(columns=["R", "D/N", "Streak", "Rank", "GB"])
  Y = data["R"]
  X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3)

  model = RandomForestRegressor(n_estimators=130, 
                                    max_leaf_nodes=110, 
                                    min_samples_split=12)
  model.fit(X_train, y_train)
  dump(model, 'Inference_model.joblib')

if __name__ == '__main__':
  train()
