##Joshua Mendiola - Titanic Survivorship Project

##initial imports for the project, taking in pandas for math calculations and matplot lib for modeling
import numpy as np
import pandas as pd
import seaborn as sbn
import matplotlib.pyplot as plt
##grabs the training and test dataset using the pandas readcsv function
training = pd.read_csv('/Users/joshuamendiola/Desktop/Data Science Practice/Datasets/train.csv')
testing = pd.read_csv('/Users/joshuamendiola/Desktop/Data Science Practice/Datasets/test.csv')

##adds new columns to the testing and training data, populating the training set with 1, and and testing with 0 
training['train_test'] = 1
testing['train_test'] = 0
##adds new column to the testing set, populating it with NaN, so it can properly concatenate with the training set
testing['survived'] = np.NaN
##concatenates the two tables together
allData = pd.concat([training,testing])

##prints the manipulated data
# print(allData.columns)
# print(allData.info())
# print(training.describe())

##separates the datasets into numerical and alphabetical sets
training_num = training[['Age','SibSp','Parch','Fare']]
training_alph = training[['Survived','Pclass','Sex','Ticket','Cabin','Embarked']]

##uses pyplot to make histograms of the numerical dataset
# for i in training_num.columns:
#     plt.hist(training_num[i])
#     plt.xlabel(i)
#     plt.ylabel("Amount of People")
#     plt.title("Training Statistics for " + i)
#     plt.show()

sbn.heatmap(training_num)
