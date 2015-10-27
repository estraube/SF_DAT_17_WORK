# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 20:57:13 2015

@author: estraube
"""

import pandas as pd

#1
data = pd.read_csv('/Users/estraube/Dropbox/ga_class/SF_DAT_17/data/titanic.csv', index_col=0)
data.head()

#2
feature_cols = ['Fare','Parch']
X = data[feature_cols]
y = data.Survived

#3
from sklearn.cross_validation import train_test_split

X_train, X_test, Y_train, y_test = train_test_split(X, y, random_state=1)

# TASK 4: fit a logistic regression model and examine the coefficients
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()
logreg.fit(X_train, Y_train)
zip(feature_cols, logreg.coef_[0])
#intercept and slope Beta1 results

#5
y_pred_class = logreg.predict(X_test)
from sklearn import metrics
print metrics.accuracy_score(y_test, y_pred_class)