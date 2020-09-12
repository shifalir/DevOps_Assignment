#importing required libraries
import pandas as pd
import numpy as np
import shutil
import os
print('This script performs transformations on data.' )
#running data transformation steps
#reading each data set into a pandas dataframe
data_2015=pd.read_csv("../data/raw_data/data_2015.csv")
data_2016=pd.read_csv("../data/raw_data/data_2016.csv")
data_2017=pd.read_csv("../data/raw_data/data_2017.csv")
data_2018=pd.read_csv("../data/raw_data/data_2018.csv")

#function to do some data transformations in order to standardrize the data from different data sources.
def transformation(df):
#renaming columns to ensure all datsets have same column names
    df.rename(columns = {'first_name':'Employee','Name':'Employee','last, fist name':'Employee','Job Title/Duties':'Job_Title','Job Title':'Job_Title','job_title':'Job_Title','Compensation in 2015':'Total_Compensation','total_compensation':'Total_Compensation','Salary':'Total_Compensation','Projected 2018 Salary':'Total_Compensation'}, inplace = True)
#creating a list of columns to be removed- we dont need this for our analysis
    columns = ['Unnamed: 0','City','Textbox6','Textbox14']
#removing unwanted columns
    df.drop(axis=1, labels=[col for col in columns if col in df.columns], inplace=True)
#Our analysis focused on Information & Technology Service department
#creating list containging different names of Information & Technology Service department in datasets
    list=['ITS - Information & Technology Service','ITS']
##replacing data so that all datasets have the same name for the department
    for item in df['Department']:
        if item in list :
            df.loc[(df.Department==item),'Department'] = 'Information & Technology Service'
#removing $ and , column from Total_Compensation column
    df['Total_Compensation']=df.Total_Compensation.astype(str)
    df['Total_Compensation']=df['Total_Compensation'].str.replace('$','',regex=True).str.replace(',','',regex=True).astype(float)

# running transformation function for each dataset
transformation(data_2015)
data_2015["Year"] = 2015

transformation(data_2016)
data_2016["Year"] = 2016

transformation(data_2017)
data_2017["Year"] = 2017

transformation(data_2018)
data_2018["Year"] = 2018

#Combining datasets to create the final dataset.
data_final=pd.concat([data_2015,data_2016,data_2017,data_2018])
#In realtime the next time would be to save the data into the warehouse/data center.
#storing file on local system for the purpose of this assignment.
data_final.to_csv('../data/data_final.csv')
