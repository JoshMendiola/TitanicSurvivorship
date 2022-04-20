#Joshua Mendiola - Titanic Survivorship Project

#initial imports for the project, taking in pandas for math calculations and matplot lib for modeling
import numpy as np
import pandas as pd
import seaborn as sbn
import matplotlib.pyplot as plt
#grabs the training and test dataset using the pandas readcsv function
training = pd.read_csv('/Users/joshuamendiola/Desktop/Data Science Practice/Datasets/train.csv')
testing = pd.read_csv('/Users/joshuamendiola/Desktop/Data Science Practice/Datasets/test.csv')

training['train_test'] = 1
testing['train_test'] = 0
testing['survived'] = np.NaN
allData = pd.concat([training,testing])

print(allData.columns)

