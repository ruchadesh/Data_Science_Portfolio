# Introduction: 

What is Health Insurance?
	Health Insurance is a program that covers medical expenses through private/ social or social welfare program
Why do we care about Health Insurance?
	Health Insurance has started declining since 2000. Due to unemployment and rise in insurance cost, the rates of coverage have declined significantly.
Why there is a rise in public insurance?
	Since the pool of people with private health insurance has shrunk.
The project plans to answer following questions:
It is imperative for people to select the right health insurance. 


# Objective: 

To predict best suitable ‘metal’ insurance plan category for the incoming customer.  


# Data Set Description

The dataset consists data of various health insurance plans collected and managed by www.healthinsurance.gov
All the Attributes that are used in the training of the model is as follows:
	State Code: Code for every state in the country
	FIPS County Code: IT is the Federal Information Processing Standard Code 	for a county
	County Name: Name of the county where the insurance is being offered 
	Plan ID (Standard Component): Unique ID of the plan
	Plan Type: it Contains information about the plan type and provider 	network. 
	Rating Area: Geographic ratings that the health insurance provides 	should use. 
	Child Only Offering- binary: whether benefits for child are included or 	not.  
  	Source Accreditation 
	Adult Dental : whether adult dental is included or not. 
	Child Dental: whether child dental is added or not.   
	EHB Percent of Total Premium: Essential Health Benefit of a insurance plan
	Premium Child: Amount of premium only for a child 
	Premium Adult Individual Age 60: amount of premium for an individual of age 60 
	Premium Couple 21. Amount of premium for a couple of age 21 
	Couple+1 child, Age 21 . Amount of premium for a couple of age 21 and a single 	child
  Medical Deductible - Individual - Standard. The amount of deductible attributed 	for medical expenses 
	Drug Deductible - Individual - Standard : Amount of deductive attributed for 	prescription drugs
	Medical Maximum Out Of Pocket - Individual - Standard: Max Amount of money 	that customer pays including deductible and co insurance 
	Drug Maximum Out Of Pocket - Individual - Standard: Max Amount of money that 	customer pays for drugs including deductible and co insurance 


# Pre-Processing:

Whether a plan includes the Dental coverage or not, plays an important role while predicting plan type
For the column Child Dental and Adult Dental, the nominal data values are interpreted as binary values as shown

# Predictive modelling using SAS Enterprise guide: 

- Decision tree
-  neural Netwrok 
- Random forest


# Observations and conclusion:

-The accuracy of decision tree model varies in between the range of 64-72%
- After comparing accuracy of decision tree, neural network and random forest models it can be concluded that the health insurance plan types can be predicted with maximum accuracy using random forest.

