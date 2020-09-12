import sys
import numpy as np
#importing required libraries
import pandas as pd
import os
import pathlib
print('This script downloads data from multiple online sources.' )

#create a directory to store data
if not os.path.exists('../data/raw_data'):
    pathlib.Path('../data/raw_data').mkdir(parents=True, exist_ok=True)


#dowloading data from an online resource.

#dowloading dataset1 
url="https://data.bloomington.in.gov/dataset/38827c26-b8c3-4c87-9a9e-acc52f9d6d10/resource/ba904e95-42d8-4015-8983-dc47eedef4fd/download/2015-bloomington-civil-city-anual-compensation.csv"
data_2015=pd.read_csv(url)
#save data as csv
data_2015.to_csv('../data/raw_data/data_2015.csv')

#dowloading dataset2 
url="https://data.bloomington.in.gov/dataset/38827c26-b8c3-4c87-9a9e-acc52f9d6d10/resource/77aad3c3-2980-4d2f-bb30-183d4488d7ca/download/bloomington-civil-city-2016.csv"
data_2016=pd.read_csv(url)
#save data as csv
data_2016.to_csv('../data/raw_data/data_2016.csv')

#dowloading dataset3
url="https://data.bloomington.in.gov/dataset/38827c26-b8c3-4c87-9a9e-acc52f9d6d10/resource/bb5d3551-91f7-4087-aa8a-0823791f4639/download/2017-bloomington-civil-city-annual-compensation.csv"
data_2017=pd.read_csv(url)
#save data as csv
data_2017.to_csv('../data/raw_data/data_2017.csv')

#dowloading dataset4 
url="https://data.bloomington.in.gov/dataset/38827c26-b8c3-4c87-9a9e-acc52f9d6d10/resource/54016e25-a8a6-4d97-9389-b18380578a4e/download/2018-bloomington-civil-city-projected-salaries.csv"
data_2018=pd.read_csv(url)
#save data as csv
data_2018.to_csv('../data/raw_data/data_2018.csv')

