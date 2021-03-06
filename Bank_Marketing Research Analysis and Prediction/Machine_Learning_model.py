1. Loading required Libraries and Dataset
In [1]:
# Load libraries
%matplotlib inline
import matplotlib.pyplot as plt
#setting dimension of graph
plt.rcParams["figure.figsize"]= (12, 7)

import pandas as pd
import numpy as np
import seaborn as sns

from pandas.tools.plotting import scatter_matrix

from sklearn.decomposition import PCA
from sklearn.preprocessing import scale
from sklearn.preprocessing import Imputer
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestRegressor

In [2]:
# Load dataset
url = "C:/Users/rucha/Desktop/bank.csv"
dataset = pd.read_csv(url)

2. Data Exploration
In [3]:
#Information of data
dataset.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 45211 entries, 0 to 45210
Data columns (total 17 columns):
age           45211 non-null int64
job           45211 non-null object
marital       45211 non-null object
education     45211 non-null object
default       45211 non-null object
balance       45211 non-null int64
housing       45211 non-null object
loan          45211 non-null object
contact       45211 non-null object
day           45211 non-null int64
month         45211 non-null object
duration      45211 non-null int64
campaign      45211 non-null int64
pdays         45211 non-null int64
previous      45211 non-null int64
poutcome      45211 non-null object
is_success    45211 non-null object

dtypes: int64(7), object(10)
memory usage: 5.9+ MB
we have 45211 observations of 17 variables (7-Numerical Variables and 10-Categorical Variables).

In [4]:
#check for any missing values
dataset.apply(lambda x: sum(x.isnull()),axis=0)
Out[4]:
age           0
job           0
marital       0
education     0
default       0
balance       0
housing       0
loan          0
contact       0
day           0
month         0
duration      0
campaign      0
pdays         0
previous      0
poutcome      0
is_success    0
dtype: int64
Fortunatly there are no any explicit missing values for any variable.

In [5]:
# head
print(dataset.head())
   age           job  marital  education default  balance housing loan  
0   58    management  married   tertiary      no     2143     yes   no   
1   44    technician   single  secondary      no       29     yes   no   
2   33  entrepreneur  married  secondary      no        2     yes  yes   
3   47   blue-collar  married    unknown      no     1506     yes   no   
4   33       unknown   single    unknown      no        1      no   no   

   contact  day month  duration  campaign  pdays  previous poutcome is_success  
0  unknown    5   may       261         1     -1         0  unknown         no  
1  unknown    5   may       151         1     -1         0  unknown         no  
2  unknown    5   may        76         1     -1         0  unknown         no  
3  unknown    5   may        92         1     -1         0  unknown         no  
4  unknown    5   may       198         1     -1         0  unknown         no  
There are many 'unknown' values under Categorical variables.We have to treat them!!!

In [6]:
# Target variable distribution
count = dataset.groupby('is_success').size()
percent = count/len(dataset)*100
print(percent)
is_success
no     88.30152
yes    11.69848
dtype: float64
From the distribution of Target variable: "is_success" it is found that data is imbalanced becouse there is approx 88% is 'no' and 12% is 'yes'.



Analysis of Indepedent Numerical Variables

# Impute outliers function
def impute_outliers(df, column , minimum, maximum):
    col_values = df[column].values
    df[column] = np.where(np.logical_or(col_values<minimum, col_values>maximum), col_values.mean(), col_values)
    return df
In [8]:
#lets see statistic of Numerical variables before Outlier treatment
dataset.describe()


# scatter plot matrix
scatter_matrix(dataset)
plt.show()

# age
sns.boxplot(x='is_success', y='age', data=dataset)

sns.boxplot(x='is_success', y='balance', data=dataset)


# Fixing balance column
dataset_new = dataset
min_val = dataset_new["balance"].min()
max_val = 20000
dataset_new = impute_outliers(df=dataset_new, column='balance' , minimum=min_val, maximum=max_val)

sns.boxplot(x='is_success', y='day', data=dataset)

sns.boxplot(x='is_success', y='duration', data=dataset)

# Fixing duration column
min_val = dataset_new["duration"].min()
max_val = 2000
dataset_new = impute_outliers(df=dataset_new, column='duration' , minimum=min_val, maximum=max_val)



Analysis of Indepedent Categorical Variables:

# Impute unknowns function
def impute_unknowns(df, column):
    col_values = df[column].values
    df[column] = np.where(col_values=='unknown', dataset[column].mode(), col_values)
    return df
# job
temp1 = pd.crosstab(dataset['job'], dataset['is_success'])
temp1.plot(kind='bar')
print(dataset.groupby(['job']).size()/len(dataset)*100)


# marital
temp2 = pd.crosstab(dataset['marital'], dataset['is_success'])
temp2.plot(kind='bar')
print(dataset.groupby(['marital']).size()/len(dataset)*100)
marital
divorced    11.517109
married     60.193316
single      28.289576
dtype: float64

. Feature Engineering
In [39]:
#Seperating Target variable from other variables
dataset_Y = dataset_new['is_success']
dataset_X = dataset_new[dataset_new.columns[0:12]]
In [40]:
#converting Independent Categorical into Numeriacal by creating Dummy variables
dataset_X_dummy = pd.get_dummies(dataset_X)
print(dataset_X_dummy.head())

4. Feature Selection with PCA
In [41]:
#converting dataframe into numpy Array
X = dataset_X_dummy.values
Y = dataset_Y.values

# Split-out validation dataset
validation_size = 0.20
seed = 7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)
In [42]:
#Scaling the values
X_t = scale(X_train)

#initially lets create 39 components which is actual number of Variables we have
pca = PCA(n_components=39)

pca.fit(X_t)

#The amount of variance that each PC explains
var= pca.explained_variance_ratio_

#Cumulative Variance explains
var1=np.cumsum(np.round(pca.explained_variance_ratio_, decimals=4)*100)
In [43]:
#lets see Cumulative Variance plot
plt.plot(var1)
Out[43]:
[<matplotlib.lines.Line2D at 0xcf36860>]

From Cumulative Variance plot we can find that first 32 components are explaining nearly 100% variability of actual data.


pca = PCA(n_components=32)
pca.fit(X_t)
X_train_PC=pca.fit_transform(X_t)

5. Model Training
In [45]:
# Test options and evaluation metric
seed = 7
scoring = 'accuracy'
Implementing Logistic Regression(LR), Linear Discriminant Analysis(LDA), K-Nearest Neighbor(K-NN), Decision Tree(CART), Naive Bayes(NB) and Support Vector Machine(SVM).
In [46]:
# Spot Check Algorithms
models = []
models.append(('LR', LogisticRegression()))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('K-NN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC()))
models.append(('RandomForest',RandomForestRegressor()))
In [47]:
# evaluate each model in turn
results = []
names = []
for name, model in models:
    kfold = model_selection.KFold(n_splits=10, random_state=seed)
    cv_results = model_selection.cross_val_score(model, X_train_PC, Y_train, cv=kfold, scoring=scoring)
    results.append(cv_results)
    names.append(name)
    msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
    print(msg)
LR: 0.891755 (0.005013)
LDA: 0.891202 (0.004555)
K-NN: 0.883958 (0.004866)
CART: 0.854734 (0.005656)
NB: 0.859241 (0.004832)
SVM: 0.893553 (0.005163)
RandomForest: 0.885432 (0.005324)
"Support Vector Machine" has highest Accuracy but it is taking more time compare to other algorithms for Training.
"Logistic Regression" is also has nearly same accuracy and it is very faster than SVM.
6. Model Selection
In [48]:
# Comparing Algorithms
fig = plt.figure()
fig.suptitle('Algorithm Comparison')
ax = fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(names)
Out[48]:
[<matplotlib.text.Text at 0x1085cac8>,
 <matplotlib.text.Text at 0x1084e780>,
 <matplotlib.text.Text at 0x10591198>,
 <matplotlib.text.Text at 0x105917f0>,
 <matplotlib.text.Text at 0x10591e48>,
 <matplotlib.text.Text at 0x105744e0>]

According to Accuracy and Computation Time Logistic Regression seems the best model.
7. Making Prediction
In [49]:
#Scaling the X_validation data
X_v = scale(X_validation)

pca.fit(X_v)
X_validation_PC=pca.fit_transform(X_v)
In [50]:
# Make predictions on validation dataset by choosing best Algorithm
lr = LogisticRegression()
lr.fit(X_train_PC, Y_train)
predictions = lr.predict(X_validation_PC)
print("Accuracy : ", accuracy_score(Y_validation, predictions))
print(confusion_matrix(Y_validation, predictions))
print(classification_report(Y_validation, predictions))
('Accuracy : ', 0.88289284529470313)
[[7744  283]
 [ 776  240]]
             precision    recall  f1-score   support

         no       0.91      0.96      0.94      8027
        yes       0.46      0.24      0.31      1016

avg / total       0.86      0.88      0.87      9043

Main challenge in this model was Exploratary Data Analysis on Unbalaced Data.
