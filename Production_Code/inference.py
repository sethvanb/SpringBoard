import pandas as pd
from sklearn.model_selection import train_test_split
from joblib import load

def inference():
  data = pd.read_csv('allTeams_data.csv')
  X = data.drop(columns=["R", "D/N", "Streak", "Rank", "GB"])
  model = load('Inference_model.joblib')
  print(model.predict(X.head(5)))

if __name__ == '__main__':
  inference()
