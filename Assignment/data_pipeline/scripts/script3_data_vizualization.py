#importing required libraries
import sys
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
print('This script creates reports and visualizations based on data.' )
#data analysis/reporting
#reading the final data into a pandas dataframe
data_report= pd.read_csv("../data/data_final.csv").loc[pd.read_csv("../data/data_final.csv")['Department'] == 'Information & Technology Service']

#Analysis/Reporting
#Creating a report based on the data. 
#calculating the average salary for each Job_Title in the Information & Technology Service department over the years
data_avg = (data_report.groupby(['Department', 'Job_Title','Year']).agg(Average_Compensation=("Total_Compensation",'mean')).reset_index().round(2))
#report can be sent out via email but here just saving it
data_avg.to_csv('../data/data_avg.csv')
#printing report to console
print("\n--------------------------------------------------RERPORT------------------------------------------------------")
print("\nReport generated for average salaries over the years for different Job_Titles has been created and saved.\nBelow is a glimpse of the report\n",data_avg.head(4))
print("\n----------------------------------------------------------------------------------------------------------------")
#extract data for 5 highest paying jobs in the latest year
df= data_avg[data_avg['Job_Title'].isin(data_avg[data_avg.Year == data_avg['Year'].max()].nlargest(5, 'Average_Compensation').Job_Title)]
#printing report to console
print("\n---------------------------------")
print("Highest paying jobs in IT are\n")
for job in df['Job_Title'].unique():
    print(job)
print("---------------------------------")

#Visualization
#Creating a plot of Salary trends for the 5 top-paying jobs in IT
#setting the column 'Year' as x axis,'Average_Compensation' as y-axis and using different coloured lines to distinguish 'Job_Title'
dx = df.pivot(index='Year', columns='Job_Title', values='Average_Compensation')
#adding data point markers and titles to plot
dx.plot(marker='o', title="Salary trends for the 5 top-paying jobs in IT")
#setting the size and position of legend
plt.legend(loc=2,prop={'size': 5})
#setting range and scale of x and y axis
plt.yticks(np.arange(65000, 90000, 2000))
plt.xticks(np.arange(2015,2019,1))
# displaying the plot
plt.show()




