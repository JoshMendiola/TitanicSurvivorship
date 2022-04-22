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

##creates a heatmap of the numeric data
# sbn.heatmap(training_num.corr())
# plt.show()

##creates a pivot table of the training table using survival as the index
# print(pd.pivot_table(training, index = 'Survived', values = ['Age','SibSp','Parch','Fare']))

##creates barplots of the amount of people from each group
# for i in training_alph.columns:
#     sbn.barplot(training_alph[i].value_counts().index,training_alph[i].value_counts()).set_title(i)
#     plt.show()


## creates pivot tables using survival as an index, comparing class, sex, and embarking location
# print(pd.pivot_table(training, index = 'Survived', columns = 'Pclass',
#                      values = 'Ticket' ,aggfunc ='count'))
# print("\n")

# print(pd.pivot_table(training, index = 'Survived', columns = 'Sex', 
#                      values = 'Ticket' ,aggfunc ='count'))
# print("\n")

# print(pd.pivot_table(training, index = 'Survived', columns = 'Embarked', 
#                      values = 'Ticket' ,aggfunc ='count'))
# print("\n")

##uses a lamda expression to create a new column in the training set, that counts how many cabins a passenger owned
##if the value is not a number, it sets it to 0, if there is multiple, it adds a split
training['cabin_multiple'] = training.Cabin.apply(lambda x: 0 if pd.isna(x) 
                                                    else len(x.split(' ')))
# print(training['cabin_multiple'].value_counts())

# print(pd.pivot_table(training, index = 'Survived', columns = 'cabin_multiple',
#                values = 'Ticket' ,aggfunc ='count'))

# n stands for null
# in this case we will treat null values like it's own category
training['cabin_adv'] = training.Cabin.apply(lambda x: str(x)[0])

#comparing survival rates by cabin
#print(training.cabin_adv)
#print(pd.pivot_table(training,index='Survived',columns='cabin_adv', values = 'Name', aggfunc='count'))

training['numeric_ticket'] = training.Ticket.apply(lambda x: 1 if x.isnumeric() else 0)
training['ticket_letters'] = training.Ticket.apply(lambda x: ''.join(x.split(' ')[:-1]).replace('.','').replace('/','').lower() if len(x.split(' ')[:-1]) >0 else 0)