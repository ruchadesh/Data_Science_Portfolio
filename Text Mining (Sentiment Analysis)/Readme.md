

# Business Case :

- To analyze reviews of resturants posted by customers on Yelp.
- To provide meaningful insights to the business and help it to improve the products/services,can be of significant.

# Objective:                 

Analyze what positve and nagetive words contribute to restaurants' reviews and make them better/worse in service. 

## What Software Do I Need?

To complete this project, i'll require the following softwares:

- Python libraries - (Numpy, Pandas, Matplotlib, StatsModels, Scipy)
- Jupyter Notebook for coding

# Dataset:	               

Restaurant_Reviews.tsv is a dataset from Kaggle datasets which consists of 1000 reviews on a restaurant. It mainly contains reviews(in the form of a text) and positive/negative rating( 1/0) 

To build a model to predict if review is positive or negative, following steps are performed.
### Data Gathering: IMported the dataset into Python jupyter notebook with Pandas library
###

There were no missing values present in the dataset. Data had no quality and tidiness issues as well. 

# Data Analysis Steps Performed:

- Imported dataset into Python’s Jupyter notebook using Pandas Library and performed exploratory data analysis
- I used three approaches to compare the consumer performance on the website:
        - Probability approach : Computed statistics to find out the probabilities of conversion regardless of page. These   		                                            were used to analyze if one page or the other led to more conversions.
        - A/B test :             Conducted hypothesis testing assuming the old page is better unless the new page proves to be   
                                 definitely better at a Type I error rate of 5%. I sued a bootstrap sampling method to further calculate 		                               P-values
        - Regression approach:   Tested the null and alternative hypotheses using a logistic regression model. I also checked the effect 		                               of the country on user conversion. 

