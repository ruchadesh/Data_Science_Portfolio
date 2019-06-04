Introduction: 
Source: Kaggle dataset 
Background: 
 I was very much interested in working on credit card transaction as the data itself is very challenging. As we all know, credit card fraud is a serious problem in digital ecommerce. Because we don’t want our customer to pay for which they haven't even bought. Vast majority of transactions are legitimate. Hence, these transactions reduce the model’s sensitivity to fraud. 

Gathering data:
The datasets contain transactions made by credit cards in September 2013 by European cardholders. This dataset presents transactions that occurred in two days, where we have 492 frauds out of 284,807 transactions. 
Number of rows: ~284K 
Number of columns: 
28 features from PCA transformations (to protect user identities and sensitive features)
Time  :
Number of seconds elapsed between this transaction and the first transaction in the dataset
Amount : amount of transaction 
Class variable: 1 for fraud transaction  , 0: otherwise

It contains only numerical input variables which are the result of a PCA transformation. Unfortunately, due to confidentiality issues, we cannot provide the original features and more background information about the data. Features V1, V2, ... V28 are the principal components obtained with PCA, the only features which have not been transformed with PCA are 'Time' and 'Amount'. Feature 'Time' contains the seconds elapsed between each transaction and the first transaction in the dataset. The feature 'Amount' is the transaction Amount, this feature can be used for example-dependent cost-sensitive learning. Feature 'Class' is the response variable and it takes value 1 in case of fraud and 0 otherwise.

Data Assessment and cleaning: 
There were no missing values present in the dataset. 
Data had no quality and tidiness issues as well. 


Data Exploration:
 
The dataset is highly unbalanced, the positive class (frauds) account for 0.172% of all transactions.

Given the class imbalance ratio, we recommend measuring the accuracy using the Area Under the Precision-Recall Curve (AUPRC). Confusion matrix accuracy is not meaningful for unbalanced classification.

Hence, I chose this approach. 
How to handle imbalanced dataset: 
1.	Over sampling: replicate the minority class without any information loss
2.	Collect more data – which did not seem feasible in this case, because practically even if we are to collect more data, we might end up getting no fraud transactions. 
3.	Change the prediction thresholds 
other classifiers, such as logistic regression, are capable of giving a probabilistic output (I.e. the chance that a given observation belongs to the positive class). For these classifiers, we can specify the probability threshold by which above that amount we'll predict the observation belongs to the positive class. If we set a very low value for this probability threshold, we can increase our True Positive Rate as we'll be more likely to capture all of the positive observations.
4.	Assign weights – assign different weights for the minority ad majority classes 


I have applied following methods:
1.	Use Logistic Regression directly to model the data;
2.	Over-sampling the data to get a balanced proportion of positive/negative values
3.	Change the performance metric, like using ROC, f1-score rather than using accuracy
