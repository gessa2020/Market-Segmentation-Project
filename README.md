# Market Segmentation End to End Machine Learning with deployment Project

## Bank customer Segmenation for effective design of marketing strategies.
![](IMAGES/cover_image.jpg)
## Introduction
Customer segmentation is one of those important aspects that a business has to carefully consider before formulating products or services to it's customer base. Therefore pitching the right message to the right customer and at the right time has been the objective for all banks.Banks look at customer segmentation to gain insight, on how to decide on specific offers, improve customer service, and understand customer behaviour & more. The success or failure of a marketing campaign depends on how customers are segmented. Based on the customer segmentation, banks unleash product recommendations like saving plans, loans, wealth management, etc. on target customer groups.

##  Problem statement 
__How can we segment our customer base to improve cross-selling opportunities?__

<h3>Objective</h3> 
To segment and analysis bank customers so as to understand the kind of clients a bank has which can then be used in developing profitable products that can generate more revenue to the bank. 
 
<h4>Workflow</h4>
From the historical data, we will first train a machine learning clustering  model on customer profile variables to come up with target groups also known as clusters, there after, we will then train a classification model that ca predict which cluster a customer belongs to so as to tailor specific products to the client depending on the charactistics of the cluster.

## Skilled demonstrated.
- Python was used for coding the project as well as some data science algorithms
- I used jupyter notebooks as the main IDE for coding
- I used Visual Studio to develop and deploy the streamlit application

## Data sourcing
I just wanted to get my hands dirty with customer segmentation, so i went to kaggle.com and and got my hands on to this  <a href="https://www.kaggle.com/datasets/sidharth178/customer-segmentation">Dataset</a> so as to practice my skills. 
 The sample Dataset summarizes the usage behavior of about nearly 1000 active credit card holders during the last 6 months. The file is at a customer level with 10 behavioral variables.
 These include:'Customer Id', 'Age', 'Edu', 'Years Employed', 'Income', 'Card Debt','Other Debt', 'Defaulted', 'DebtIncomeRatio'

## Data tranformation and cleaning.
1.  I had to first dropped the 'unnamed 0' column since it was not meaningful for our project.
3.  There was some missing data in the defaulted variable, so i filled it in with the median for that column.


## Data Analysis and Visualization
Graph showing distribution of individual numerical variables![](IMAGES/Histogram_image1.png)
### key takes ways from the plot above
- The average age of clients is about 35 years with the age distribution being fairly skewed to the right
- Income and Card Debt are highly skewed to the right
- Debt income ratio and years employed have distributions that are skewed to the right.
- The highest number of clients have education in category 1.0

Graph showing Generated Clusters![](IMAGES/cluster_image.png)
### key takes ways from the plot above
Three clusters were generated using two principle components 

Graph showing Models generated![](IMAGES/model_image1.png)
From the generated clusters, we can draw the following conclusions
1. 


### key Analysis find from 2016  data
1. We saw that 38.85% of the bank customers bought the savings product.
2. The percentage of customers who bought the pension product is 22.76%. 
3. The least consumed product was mortgage accounts with 15.41%.
4. The highest number of customers bought one product with a percentage of 45.06%. 
5. The percentage of customers who bought several products are 15.39%.

## Model buiding
We used the gradient boosting model to build 3 classfiers to predict which product a customer would subscribe to. 
we then used each of the individual classifiers to predict which product a new customer would subscribe to using the 
2017 data as test data.
### Results from modelling
1. We can see that 26.42% of the new customers are predicted to buy the savings product
2. The percentage of customers predicted to buy the mortgage product is 14.15% 
3. The least consumed product was pension accounts with 5.19% of the bank customers
4. The highest number of customers bought one product with a percentage of 37.74%
5. The percentage of customers who bought several products are 3.99%



## Conclussions and Recommendations
### Conclusion

1. We can see that just like in 2016, the best selling product is still the savings product and therefore more emphasis in form of marketing should be put in selling this product to increase on the product uptake.
2. Unlike in 2016 where the least consumed product was mortgage, 2017 prediction results show that pension will be the least consumed product.
3. From the Prediction results, we also see that mortgage becomes the next consumed product after savings. 

### Final Remarks
Given more time, Since the constraint given was to contact the customers to sell them only one product and you can not select all of them, We may need to explore the contact channel and their effectiveness to be able to select the best channel to use according to their profitability, and also select which product will be sold to a given customer.









