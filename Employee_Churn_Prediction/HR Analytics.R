library ("klaR")
library ("caret")
library ("e1071")
library("ggplot2")
library("neuralnet")
library("ROSE")
library("ggthemes")
library("tidyverse")

set.seed(1234)
Hr = read.csv(file.choose())

######### plot for class varible 
plot(Hr$left)

ggplot(data = Hr) +
  geom_bar(stat="count", aes(satisfaction_level, fill=as.factor(left)))

ggplot(data = Hr) +
  geom_bar(stat="count", aes(promotion_last_5years, fill=as.factor(left)))


ggplot(data = Hr) +
  geom_bar(stat="count", aes(salary, fill=as.factor(left)))

##### correlation 


class(Hr$salary)
num.cols <- sapply(Hr,is.numeric)
cor.data <- cor(Hr[,num.cols])
# visualisation of corrolation with corrlot
corrplot(cor.data, method = "circle" , type = "lower")

cor.test(Hr$left , Hr$satisfaction_level)

################### Skewness 
hist(Hr$left , col = "blue")
ggplot(data = Hr, aes(x = left)) + geom_bar()

########### over sampling 



data_balanced_over <- ovun.sample(left ~ ., data = Hr, 
                                  method = "over",
                                  N = 2*nrow(subset(Hr,Hr$left==0)),
                                  seed=1)$data
table(data_balanced_over$left)

data_balanced_over$left <- as.factor(data_balanced_over$left)

############### Naive Bays
ShuffledHr <-data_balanced_over[sample(nrow(data_balanced_over)),]
train <- ShuffledHr[1:15000,]
test <- ShuffledHr[15001:22856,]
model <- NaiveBayes(left ~ ., data=train)
#test the model
predictions <- predict(model, test)
warnings()
confusionMatrix(test$left, predictions$class)

################## Rpart
library(ggplot2) 
library(rpart) 
Hr.ct<-rpart(train$left ~ ., data=train[,1:18], cp=0.02)
plot(Hr.ct) 
text(Hr.ct, use.n = T, digits = 3, cex = 0.6)
Prediction <- predict(Hr.ct, newdata=test, type='class')
head(Prediction)
confusionMatrix(Prediction, test$left)
summary(Hr.ct)

##################### Cross valid
folds <- cut(seq(1,nrow(data_balanced_over)),breaks=10,labels=FALSE)
outputData=0

#Perform 10 fold cross validation 
for(i in 1:10){
  #Segement your data by fold using the which() function 
  testIndexes <- which(folds==i,arr.ind=TRUE)
  testData <- data_balanced_over[testIndexes, ]
  trainData <- data_balanced_over[-testIndexes, ]
  
  classifier = NaiveBayes(left ~ ., data=trainData)
  pred = predict(classifier, testData)
  misClassifyError = mean(pred$class != testData$left)
  Accuracy = 1-misClassifyError
  outputData[i] = Accuracy
}
head(outputData,10)
summary(outputData)


########## Gradient boosting

library(gbm)
Hr.gbm <- gbm(left ~ ., data=train, n.trees=100, interaction.depth=6, shrinkage=0.01)
Prediction = predict(Hr.gbm, newdata=test, n.trees=100, type="response")
Prediction <- ifelse(Prediction > 0.5,1,0)
Prediction
confusionMatrix(Prediction,test$left )
plot(Hr.gbm)

####### cross validation for gbm 
folds <- cut(seq(1,nrow(Hr)),breaks=10,labels=FALSE)
outputData=0

#Perform 10 fold cross validation 
for(i in 1:10){
  #Segement your data by fold using the which() function 
  testIndexes <- which(folds==i,arr.ind=TRUE)
  testData <- Hr[testIndexes, ]
  trainData <- Hr[-testIndexes, ]
  
  classifier = gbm(left ~ ., data=trainData ,n.trees=100, interaction.depth=6, shrinkage=0.01 )
  pred = predict(classifier, testData ,n.trees=100, type="response" )
  pred <- ifelse(pred > 0.5,1,0)
  misClassifyError = mean(pred != testData$left)
  Accuracy = 1-misClassifyError
  outputData[i] = Accuracy
}
head(outputData,10)
summary(outputData)
