


<h1 align="center"> Telecom Churn Prediction</h1>

<p align="center"> 
<img src="images/Customer-exit.png" height="600px" width="900px">
</p>

<p> </p>

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<h2> :floppy_disk: Table of Content</h2>

 
  * [Introduction](#Introduction)
  * [Problem Statement](#Problem-Statement)
  * [Objectives](#Objectives)
  * [Data Summary](#Data-Summary)
  * [Steps Involved](#Steps-Involved)
  * [Pre-processing](#Pre-processing)
  * [Algorithms used](#Algorithms-used)
  * [Conclusion](#Conclusion)


![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)


<h2> 📄 Introduction</h2>

Customer churn prediction is the process of identifying which customers are likely to leave a service or cancel a subscription based on their usage of the service. It is crucial for many businesses because acquiring new clients is often more expensive than retaining existing ones. To predict churn effectively, companies need to synthesize and utilize key indicators defined by their team to signal when a customer has a probability of churning so that their company can take action.


![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)


<h2> ❓ Problem Statement</h2>

In This problem, we trying to solve churning in the telecom industry. Telecom companies face an average annual churn rate of 10-15%, which is significantly high due to the cost of acquiring new customers. To retain highly profitable customers, we use machine learning models to predict churn on an individual customer  basis and take countermeasures such as discounts, special offers, or other gratifications to keep the customers.


![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<h2> 🎯 Objectives: </h2>

1. Building a predictive model to find and retain customers at the highest risk of churn

2. Gathering information regarding the factors that affect this prediction the most.

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<h2> :book: Data Summary </h2>

The data contained 7043 user details who used the service and some of them quit the service due to some issues.

The dataset contains the following information:

* **customerID**
* **gender** - Male/Female
* **SeniorCitizen** - Is Senior Citizen Or Not
* **Partner** - Have partner or Not
* **Dependents** - Have Dependents or Not
* **tenure** - Tenure in months
* **PhoneService** - Have phone service or not
* **MultipleLines** - Do they have multiple lines or no phone at all
* **InternetService** - Internet service type like optic fiber..etc
* **OnlineSecurity** - Have online Security or Not
* **OnlineBackup** - Have an online backup or not
* **DeviceProtection** - Have device protection or not
* **TechSupport** - Do they get support from the company side
* **StreamingTV** - Use Streaming Tv
* 	**StreamingMovies** - Do they watch movies online
* 	**Contract** - package type - Monthly/yearly
* 	**PaperlessBilling** - Online or offline payment
* 	**PaymentMethod** - What kind of payment service they use
* 	**MonthlyCharges** - Subscribed monthly package amount
* 	**TotalCharges** - Total Amount spent by customer till this date
* 	**Churn** - Customer churned or Not (Target variable)


![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<h2> 📑 Steps involved </h2>

1. Exploring the data: Analyzing the features and target variable, checking for null values and duplicates, plotting the distribution of target variable, etc.

2. Treating numerical and categorical features separately, Encoding, etc.

3. Train test split, Transformation, Scaling, etc.

4. Develop different models and evaluate them.

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<h2>🛠️ Pre-processing </h2>

In this project, the dependent variable is ‘User Churned Or Not’, the prediction of which gives us the customers are likely to leave a service or cancel a subscription

![image](images/churne_or_not.png)
![image](images/unbalanced.png)


We can observe that the dataset is unbalanced. So we have to focus on sampling to make each class in dependent variable to same ratio Or we can consider another matrix like recall to find the performance of the algorithms.

![image](https://user-images.githubusercontent.com/92729412/194842482-fd3c3d78-d67b-4a8f-834e-b4573cfc57bb.png)

VIF value is under 5. Therefore we assume that the multicollinearity between the independent variables is negligible.

![image](https://user-images.githubusercontent.com/92729412/194842509-3ce4caaf-0077-4e03-956f-fdf74fc1fdf3.png)

We can observe from the above chart that due to high snowfall and lower temperatures, the number of rented bike count is deficient in the winter compared to summer and spring. People use rental bikes primarily for short-distance travel like traveling to school or work. That's why the percentage of rented bikes count is lesser on a holy day. Since bikes are rented only on a functioning day, there is no doubt why the percentage of rented bikes count is zero on a non-functioning day.

![image](https://user-images.githubusercontent.com/92729412/194884056-e4d85ab6-84d6-46fc-9aef-02a781c0e8fe.png)

We might infer from the large rise in rental rates between 6:00 am to 8:00 am and 10:00 am to 6:00 pm that there is very high demand during the opening and closing hours of offices.  There is a consistent increase in demand for rental bikes from 10:00 AM to 6:00 PM. The least popular time to rent a bicycle is in the early morning hours (1:00 AM to 6:00 AM).  Regardless, of the seasons, this has been the general trend noticed.

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<h2>Getting Started</h2>
1. Raw Data is being kept here [Click Here](https://github.com/Muhliscm/dsProjects/blob/main/telecome_churn_prediction/churn_original.csv)  <br>
2. Exploratory Data Analysis scripts are being kept [here](https://github.com/Muhliscm/dsProjects/blob/main/telecome_churn_prediction/credit_churn_EDA.ipynbhttps://github.com/Muhliscm/dsProjects/blob/main/telecome_churn_prediction/credit_churn_EDA.ipynb)<br>
3. Machine learning model building scripts Kept [here](https://github.com/Muhliscm/dsProjects/blob/main/telecome_churn_prediction/Model_building.ipynb)<br>


<h2>💻 Algorithms used</h2>

* Linear Regression

* Random Forest

* Gradient Boosting Machine

* XGBoost

<h3> Best Hyper-parameters </h3>

* Random Forest:

max_depth : 8

min_samples_leaf : 40

min_samples_split : 50

n_estimators : 100

* GBM:

max_depth : 8

min_samples_leaf : 40

min_samples_split : 50

n_estimators : 80

* XGBoost:

eval_metric : rmse

max_depth : 6

n_estimators : 500

<h3> Model Comparison </h3>

All the models are evaluated on the basis of following evaluation metrics.

![image](https://user-images.githubusercontent.com/92729412/194840929-6cfe7fcb-6422-41f0-9349-9ba80e9cfd03.png)

<h2> :bulb: Conclusion</h2>

This project focus on predicting the bike-sharing demand using Seoul Dataset.

* In contrast to Linear Regression, the results demonstrate that XGBoost, Random Forest, and GBM algorithms performed well on the dataset.

* Among these three models, XGBoost is found to have better performance with least test-MAE(139.62) and highest test - R2 Score(87%). Therefore XGBoost algorithm can be used as an effective tool for Bike Sharing Demand Prediction.

* Analyzing feature importance showed that functioning day, temperature, and rainfall were the most influential variables in predicting the rental bike demand at each hour for all the models.

* The intriguing relationship between the variables that can have an immediate impact on the dependent variable, "Rented Bike Count," is revealed by this project.

* As a result of this project, bike-sharing companies can better predict the hourly demand for bikes and enhance the customer experience.
 
![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<!-- CREDITS -->
<h2 id="credits"> :scroll: Credits</h2>

Nivya T | Avid Learner | Data Scientist | Machine Learning Engineer | Deep Learning Enthusiast

<p> <i> Contact me for Data Science Project Collaborations</i></p>


[![LinkedIn Badge](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/nivyathiruvoth/)
[![GitHub Badge](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/nivyathiruvoth)
[![Medium Badge](https://img.shields.io/badge/Medium-1DA1F2?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@nivyathiruvoth)
[![Resume Badge](https://img.shields.io/badge/resume-0077B5?style=for-the-badge&logo=resume&logoColor=white)](https://drive.google.com/file/d/1o5VojatmPA-amnQkOJ-xb6yIq_Jof8D2/view?usp=sharing)
