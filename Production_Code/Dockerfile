FROM jupyter/scipy-notebook

# install build utilities 
RUN pip install joblib

# Copy data
COPY allTeams_data.csv ./allTeams_data.csv

# Copy all the necessary files to the image (COPY <src> … <dest>)
COPY train.py ./train.py
COPY inference.py ./inference.py

# Run python scripts 
RUN python3 train.py