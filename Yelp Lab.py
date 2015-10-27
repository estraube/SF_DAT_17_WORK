# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 21:09:07 2015

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


yelp_data = pd.read_csv('/Users/estraube/Dropbox/ga_class/SF_DAT_17/data/yelp.csv', index_col=0)

yelp_data.describe()

sns.pairplot(yelp_data, x_vars=['cool','useful','funny'], y_vars='stars', size=4.5, aspect=0.7)

sns.pairplot(yelp_data, x_vars=['cool','useful','funny'], y_vars='stars', size=4.5, aspect=0.7, kind='reg')

fig, axs = plt.subplots(1, 3, sharey=True)
yelp_data.plot(kind='scatter', x='cool', y='stars', ax=axs[0], figsize=(16, 6))
yelp_data.plot(kind='scatter', x='useful', y='stars', ax=axs[1])
yelp_data.plot(kind='scatter', x='funny', y='stars', ax=axs[2])

sns.pairplot(yelp_data)
#cool is a predictor of useful but not funny

lm = smf.ols(formula='funny ~ useful', data=yelp_data).fit()

# print the coefficients
lm.params
