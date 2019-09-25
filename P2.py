# #Using pandas take in tne Cambridge Salary set and do the following:

#1. Describe the data set to give a data understanding

#2. calculate the total salary budget for all divisions

#3. Submit your code and dataset via github and post the link to blackboard


import pandas as pd

Salaries = pd.read_csv('Cambridge_Salaries')# importing the Cambridge Salaries data set

understanding = Salaries.describe() #Calling the function to describe the statistics of the data set

Total_Budget = salaries.sort_values('Division') #Calling the function to give the total salary amount by each division

print('The data set is described by the following statistics')
print(Salaries)
print('The total salary budget for all division is')
print(Total_Budget)
