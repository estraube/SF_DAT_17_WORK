# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 12:22:38 2015

@author: estraube
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
pd.set_option('max_columns', 50)
%matplotlib inline

d = {'Chicago': 1000, 'New York': 1300, 'Portland': 900, 'San Francisco': 1100,
     'Austin': 450, 'Boston': None}
cities = pd.Series(d)
cities

cities['Chicago']

cities[cities < 1000]

print ('Seattle' in cities)

cities = cities * 3

print cities[['Chicago', 'New York', 'Portland']]
print'\n'
print cities[['Austin', 'New York']]
print'\n'
print cities[['Chicago', 'New York', 'Portland']] + cities[['Austin', 'New York']]

cities.notnull()
cities.first_valid_index()

data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
        'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions', 'Lions', 'Lions'],
        'wins': [11, 8, 10, 15, 11, 6, 10, 4],
        'losses': [5, 8, 6, 1, 5, 10, 6, 12]}
        
type(data)

football = pd.DataFrame(data, columns=['year','team','wins','losses'])
football

%cd ~/Dropbox/ga_class/Misc_GA_stuff

!head -n 5 mariano-rivera.csv

from_csv = pd.read_csv('mariano-rivera.csv')
from_csv.head()

%cd ~/Dropbox/ga_class/Misc_GA_stuff/gregreda.com/content/notebooks/data

!head -n 5 peyton-passing-TDs-2012.csv

cols = ['num', 'game', 'date', 'team', 'home_away', 'opponent',
        'result', 'quarter', 'distance', 'receiver', 'score_before',
        'score_after']
no_headers = pd.read_csv('peyton-passing-TDs-2012.csv', sep=',', header=None,
                         names=cols)
no_headers.head()

football.head()
football.to_excel('football.xlsx', index=False)
!ls -l *.xlsx

del football

football = pd.read_excel('football.xlsx', 'Sheet1')
football

#Database

from pandas.io import sql
import sqlite3

conn = sqlite3.connect('/Users/estraube/Dropbox/ga_class/Misc_GA_stuff/gregreda.com/_code/towed')