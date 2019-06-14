# Business Case :    

Company has developed a new web page in order to try and increase the number of users who "convert," meaning 	                the number of users who decide to pay for the company's product
# Objective:                 

To help the company understand if they should implement this new page, keep the old page, or perhaps run the 		                experiment longer to make their decision.

## What Software Do I Need?

To complete this project, i'll require the following softwares:

- Python (Numpy, Pandas, Matplotlib, StatsModels, Scipy)
- Jupyter Notebook

# Dataset:	               

Consisted of information for ~300K website users such as the time they visited the webpage, whether they were a part 	               of test/control group, if they visited old/new page and did the convert or not

# Data Assessment:

There were no missing values present in the dataset. Data had no quality and tidiness issues as well. 

# Data Analysis Steps Performed:

- Imported dataset into Python’s Jupyter notebook using Pandas Library and performed exploratory data analysis
- I used three approaches to compare the consumer performance on the website:
        - Probability approach : Computed statistics to find out the probabilities of conversion regardless of page. These   		                                            were used to analyze if one page or the other led to more conversions.
        - A/B test :             Conducted hypothesis testing assuming the old page is better unless the new page proves to be   
                                 definitely better at a Type I error rate of 5%. I sued a bootstrap sampling method to further calculate 		                               P-values
        - Regression approach:   Tested the null and alternative hypotheses using a logistic regression model. I also checked the effect 		                               of the country on user conversion. 

