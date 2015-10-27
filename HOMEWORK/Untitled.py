# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 20:30:18 2015

@author: estraube
"""
import numpy as np
from pandas import Series, DataFrame
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime


### Exploratory Data Analysis!!!! ####
data = pd.read_csv('/Users/estraube/Downloads/train.csv')
data.head()
data.info()

data['Hour'] = data.apply(lambda x: datetime.datetime.strptime(x['Dates'], "%Y-%m-%d %H:%M:%S").hour, axis = 1)
data['Weekend'] = data.DayOfWeek.map({'Monday':0, 'Tuesday':0, 'Wednesday':0, 'Thursday':0, 'Friday':0, 'Saturday':1, 'Sunday':1})

data.head()

data.PdDistrict.value_counts().plot(kind='bar')

data.Category.value_counts().plot(kind='bar')
data.Category.value_counts() / data.Category.shape[0]
data.Category.value_counts()


for neigh in data.PdDistrict.unique():
   fig = plt.figure()    
   neighborhood = data[data.PdDistrict == neigh].groupby([data.Category]).X.count()
   neighborhood.plot(axes=fig, kind='bar', title = neigh)
   
for neigh in data.PdDistrict.unique():
   fig = plt.figure()    
   neighborhood = data[data.PdDistrict == neigh].groupby([data.Hour]).X.count()
   neighborhood.plot(axes=fig, kind='bar', title = neigh)

data.groupby([data.Category]).Hour.mean()
data.groupby([data.PdDistrict]).Hour.mean()


data[data.PdDistrict == 'SOUTHERN'].Hour.value_counts(sort=False).plot(kind='bar')