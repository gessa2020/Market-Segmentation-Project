# Market Segmentation End to End Machine Learning with deployment Project

# Promoting financial products to bank customers
![](IMAGES/Image1.jpg)
## Introduction
In 2016, a retail bank sold several products (mortgage account, savings account, and pension account) to its customers. It kept a record of all historical data, and this data is available for analysis and reuse. Following a merger in 2017, the bank has new customers and wants to launch some marketing campaigns.

The budget for the campaigns is limited. The bank wants to contact a customer and propose only one product

__The marketing department needs to decide:__

- Who should be contacted?
- Which one of the products should be proposed?
- Will such campaigns be profitable?

##  Problem statement 
__Given a set of bank products,predict which product would be consumed by a customer__

<h3>Objective</h3>
Our assignment is to develop classification models which we use to predict which among the given set of products
a customer would subscribe to. 
 
<h4>Classification workflow</h4>
From the historical data, we can train a machine learning product-based classification model on customer profile variables to predict a product category that a customer would take up, we can base on that information to know if a customer would subscribe to a <b> mortgage </b> , <b> savings</b>, or <b> pension</b> account.

You can apply this classification model to new customer data to predict a product that would they subscribe to. 
Using this prediction, you can decide which offers are proposed and Which product is offered to which customer.The solutions can be displayed, compared, and analyzed.

## Skilled demonstrated.
- Python was used for coding the project as well as use of some data science algorithms
- I used jupyter notebooks as the main IDE for coding

## Data sourcing
I got access to the data to address the stated problem above from a github repository.
The dataset contains 23 numerical columns namely:

'customer_id', 'age', 'age_youngest_child', 'debt_equity', 'gender','bad_payment', 'gold_card', 'pension_plan',
 'household_debt_to_equity_ratio', 'income', 'members_in_household','months_current_account', 'months_customer', 'call_center_contacts','loan_accounts', 'number_products', 'number_transactions','non_worker_percentage', 'white_collar_percentage', 'rfm_score','Mortgage', 'Pension', 'Savings', 'nb_products'.

Click <a href="https://raw.githubusercontent.com/vberaudi/utwt/master/unknown_behaviors.csv">HERE</a> to access 
the 2016 raw data.

You can also click <a href="https://raw.githubusercontent.com/vberaudi/utwt/master/unknown_behaviors.csv">HERE</a> to 
access the 2017 raw data.

## Data tranformation and cleaning.
1.  I had to first dropped the 'unnamed 0' column since it was not meaningful for our project.
2.  I removed duplicated data from the dataset 
3.  There was no missing data so imputation was performed
4.  For purposes of creating meaningful visualizations, we encoded the gender column into male and female values
5.  We also encoded other categorical values into Yes and NO values to create meaningful visualizations

## Data Analysis and Visualization
Graph showing distribution of individual numerical variables![](IMAGES/numerical_visuals.png)
### key takes ways from the plot above
- We have some variables that are fairly normally distributed and those which are highly skewed.
- Variables like age,income,debt_equity,household_debt_to_equity_ratio are fairly normally distributed
- Variables like age_of_youngest_child,months_current_account are fairly skewed.
- Variables such as number_of_products,number_of_transactions,loan_accounts,months_customer, members_in_household are highly skewed.

Graph showing distribution of individual Categorical variables![](IMAGES/categorical_visuals.png)
### key takes ways from the plot above
1. Among the three products the bank is selling, the most consumed product is Savings, followed by Pension and the least is Mortgage.
2. There is almost an equal number of males customers compared to female customers
3. There are negligible cases of bad payment from customers who consume loans
4. The gold card service is one which has not been taken up my majority of the customers.

Graph showing Bivariate plots between variables![](IMAGES/bivariate_visuals.png)
### key takes ways from the plot above in regards to mortgage, savings and pension
1. Customers with no loan accounts are the highest subscribers to savings and the number of subscribers to savings
account generally decreases with increase in loan accounts
2. Customer who have 2 or more members in thier household generally subscribe to the savings account
3. Customers who subcribe to the mortgage account generally increase with increase in the members of thier household
4. Just like mortgage, the most customers who subscribed to pension accounts have no loan accounts and they decrease
with increase in loan accounts.

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









