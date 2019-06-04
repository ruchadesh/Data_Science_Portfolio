# Introduction: 
- People analytics can help to assess the effectiveness of people practices, programs and processes. 
- This project helps to understand hwo knowledge of socuial and data sciences can help you make more informed and objective people decisions
- It includes the application of analytical processes to the Human Resources Department of an organziation in order to increase the employee performaNCE
  and get a better return on investment
  
# Objective:

To predict whether the particular employee will leave the company or not
  
# Dataset information:

The dataset used for this project is taken from Kaggle competition. 
  It consists of total 18 variables (columns) and 14999 data rows. 
  
  Dependent variable  : left 
   		      : determines whether particular employee has left the company or not 
                      : has discrete values ( 0 – did not leave the company , 1 – left the company ) 

  Independent variables :  These variables give the information of the factors affecting the employee churn such as Last Evaluation ,  
                           Number of projects,Average monthly hours , time spent at the company , Whether they have had a work accident,  
                           whether they have had a promotion in the last 5 years , Department,etc. 
                           
  # Data cleaning 

 -  Changed few factor variable to numerical values in R. For example Salary variable is changed from (High, Medium, Low) to (1, 2, 3). Similarly we changed Overtime variable with (Yes, No) values to (1,0)

-  Imputed NA and missing values in R studio. 

  # Data exploration

-  Linear dependency between two variables can be checked by correlation matrix 
-  Use of corrplot function to visualize a graphical display of correlation matrix 
-  Maximum correlation can be seen between  Satisfaction_level and  left columns. ( -0.388375)

  # Over sampling to handle unbalanced dataset:
  - Works with minority class. 
It replicates the observations from minority class to balance the data.
Advantage: No information loss. 
Disadvantage of this method is that, since oversampling simply adds replicated observations in original data set, it ends up adding multiple observations of several types, thus leading to overfitting. Although, the training accuracy of such data set will be high, but the accuracy on unseen data will be worse.

# Predictive Modeling in R

- Classification : 
       This method is used to accurately predict  the target class for each case in the data.  We have used following classification method to decide whether the particular employee will leave the company or not. 
Naïve Bayes Classifier 
Recursive Partitioning 
Generalized Boosted models

# Model Evaluation:

- Helps to find the best suitable model for the data 
Makes the decision about the performance of the model in the future. 
Two methods are used : 

	1. Hold-Out method :    Input dataset is divided into training and test 
                                                dataset 
	2. K- fold Cross validation :  It is used to estimate the expected level of fit 
                                                       of a model to a dataset that is independent of the data 
                                                       that were used to train the model. 
                                                       
 # Conclusion:
 
-  From the correlation matrix , it can be concluded that Satisfaction level of the employee is the most important factor affecting the employee churn

- Out of three classifiers, generalized boosted model performs well with the accuracy of 88% 

- Cross validation sampling method helps to increase the accuracy for all three models.

                                                       





  

  
  
