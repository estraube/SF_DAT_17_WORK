# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 19:04:04 2015

@author: estraube
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import train_test_split
from sklearn import metrics
import statsmodels.formula.api as smf

# visualization
import seaborn as sns
import matplotlib.pyplot as plt

#1
data = pd.read_csv('/Users/estraube/Downloads/train.csv')
import datetime
data['Hour'] = data.apply(lambda x: datetime.datetime.strptime(x['Dates'], "%Y-%m-%d %H:%M:%S").hour, axis = 1)

data.head()
data.shape
data.value_counts()

data.PdDistrict.value_counts().plot(kind='bar')

data.groupby([data.Category,data.PdDistrict]).Dates.count()

x = data.groupby([data.Category,data.PdDistrict])

x.count()
data.groupby([data.Category,data.Hour]).size().to_csv('csvvv', sep='\t', encoding='utf-8')

data.groupby([data.Category,data.PdDistrict]).Dates.count()
data.Hour.value_counts()

data.groupby([data.Hour,data.Category]).Hour.count()

for neigh in data.PdDistrict.unique():
   fig = plt.figure()    
   neighborhood = data[data.PdDistrict == neigh].groupby([data.Category]).X.count()
   neighborhood.plot(axes=fig, kind='bar', title = neigh)
   
for neigh in data.PdDistrict.unique():
   fig = plt.figure()    
   neighborhood = data[data.PdDistrict == neigh].groupby([data.Hour]).X.count()
   neighborhood.plot(axes=fig, kind='bar', title = neigh)
   
data[data['Category'] == 'VANDALISM'].groupby([data.Category]).Hour.mean()

data.Address.value_counts()

data['TimeOfDay'] = for i in data:
    if data.Hour < 10:
     return 'morning'
    elif data.Hour >= 10:
     return 'evening'

data['Weekend'] = data.DayOfWeek.map({'Monday':'Weekday', 'Tuesday':'Weekday', 'Wednesday':'Weekday', 'Thursday':'Weekday', 'Friday':'Weekday', 'Saturday':'Weekend', 'Sunday':'Weekend'})
    