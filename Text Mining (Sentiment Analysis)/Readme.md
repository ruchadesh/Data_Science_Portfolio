

# Business Case :

- To analyze reviews of resturants posted by customers on Yelp.
- To provide meaningful insights to the business and help it to improve the products/services,can be of significant.

# Objective:                 

Analyze what positve and nagetive words contribute to restaurants' reviews and make them better/worse in service. 

## What Software Do I Need?

To complete this project, i'll require the following softwares:

- Python libraries - (Numpy, Pandas, NLTK)
- Jupyter Notebook for coding

# Dataset:	               

Restaurant_Reviews.tsv is a dataset from Kaggle datasets which consists of 1000 reviews on a restaurant. It mainly contains reviews(in the form of a text) and positive/negative rating( 1/0) 

### To build a model to predict if review is positive or negative, following steps are performed.

- Data Gathering: Imported the dataset into Python jupyter notebook with Pandas library
- Text cleaning and pre-processing: 1. Removed Punctualtion and numbers from reviews by sleecting only text format using Regex
                                    2. Removed stopwords
                                    3. Lemmatization
                                    4. Converted al l text to lower case
                                    5. Create a corpus containign clean words
- Tokenziation: Converted each word in a corps into a token
- Vectorization: Created a sparse matrix for 1500 features to represent the number of occurence of each word in a corpus adn created a                    bag of words
- Prediction model: Built a random forest algorithm to predict the category of a review- positive/negative, compared the results with  
                    actual ratings with an accuracy of 67%
                    ( Dependent variable: Sparse matrix for words
                      Independent variable: Review rating category) 
      
