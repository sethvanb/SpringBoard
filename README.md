# SpringBoard Capstone Project

## Project Description
This proejcts main goal is to predcit an mlb teams runs for their next game using a Machine Learning algorithm. To achieve this I gathered a lot of data on every mlb teams records for the last 20 years. Then I tested various machine learning algorithms with this data and settled on a Random Forest model to predict the runs of an mlb teams next game. I exported this model as a .joblib file and then deployed it on Google Cloud Platforms Storage Cloud and set up an API through their AI PLatform. I then created a web application that uses React/Node.js/Python to request my API and give run prediction for both teams of a dialy match up. The folder /Explortaion_Datasets has python scripts and datasets that I was exploring in the beginning ofn the project. The folder /Docs outlines planning for the project and the folder /Research has research on other project that were similar to this one. The folder /Data_Gathering_and_Analysis has scrpits for gathering data on each mlb team's records and for analyzing/refining the data. The folder /Training_and_Model_Testing has the python notebooks used to train and test various model to compare thier results. The folder /Prduction Code has the python script to train the Machine Learning model and a submodle of a web app that can request prections from the model if its deployed. To deploy the machine learing model follow the instructions below. To deploy the companion web appliction follow the instructions that are in the submodule under Production_Code/mlb-run-predictor or at [this repository](https://github.com/sethvanb/mlb-run-predictor). This applictaion is currently deploye don Google Cloud platform and can be accessed using the Heroku deployment linked below. 

[Heroku Deployment](https://mlb-run-predictor.herokuapp.com/)

## Machine Learning Model Deployment
* To deploy a Machine Learning Model to Google Cloud Platform, start by cloning this repository
* (Optional) You can run `python3 Data_Gathering_and_Analysis/ModifiedDataGather.py` and `python3 Data_Gathering_and_Analysis/EDA.py` to upadte, analyze, and refine the team data set
    * You can then copy this data into the Production_Code file and replace the current data set in there
    * To train a new model with this data, delete/rename the 'model.joblib' file and  run  `python3 Production_Code/train.py`
    * You can also chabnge the type or model and it parameters in Production_Code/train.py
* Deploy the 'model.joblib' file from the Production_Code folder, using the instruction in [this video](https://www.youtube.com/watch?v=q8u4irnpfzE)
* Now you can access the model and test it on the console like video deomonstrated or you can write a python script using the code given on the Google Cloud Platform console when you click on the button "Sample Prediction Request" or you can deploy this web app that is in the  submodule under Production_Code/mlb-run-predictor or at [this repository](https://github.com/sethvanb/mlb-run-predictor). 

## Project Docs
Documents for the Spring Board Capstone Project are under the /Docs/ folder. These give insight into the background planning for the applictaion. 
