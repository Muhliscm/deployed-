<h1 align="center"> Bicycle Demand Predictions</h1>

<p align="center"> 
<img src="images/bike_sharing.jpg" height="600px" width="900px">
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
Bike-sharing systems are a means of renting bicycles where the process of obtaining membership, rental, and bike return is automated via a network of kiosk locations throughout a city. Using these systems, people can rent a bike from one location and return it to a different place on an as-needed basis. Currently, there are over 500 bike-sharing programs around the world.

This project is a part of Kaggle bike demand prediction: https://www.kaggle.com/competitions/copy-of-sw5-mi-e23-bike-sharing



![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)


<h2> ❓ Problem Statement</h2>

Bicycle demand prediction refers to the task of forecasting the future demand for bicycles in a specific area or for a particular period. It involves using historical data and various factors or features that can influence bicycle usage to make predictions about how many bicycles will be needed or rented in the future. This prediction can be valuable for various purposes, such as urban planning, transportation management, bike-sharing system optimization, and more.


![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<h2> 🎯 Objectives: </h2>

1. Make predictions about how many bicycles will be needed or rented in the future

2. Using historical data and various factors or features that can influence bicycle usage

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<h2> :book: Data Summary </h2>

The data contained 7043 user details who used the service and some of them quit the service due to some issues.

The dataset contains the following information:

* **Id**	
* **datetime** - date
* **yr**	- 0 for 2011, 1 for 2012
* **mnth**	- month - 1-12
* **hr**	- hour -0-23
* **season**	- 1 = spring, 2 = summer, 3 = fall, 4 = winter
* **holiday**	- whether the day is considered a holiday
* **weekday**	- whether the day is neither a weekend nor a holiday
* **workingday**
* **weathersit**<br>
  weather -
  1: Clear, Few clouds, Partly cloudy, Partly cloudy
  2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist
  3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds
  4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog
* **temp**	 - temperature in Celsius
* **atemp**	- "feels like" temperature in Celsius
* **hum**	- relative humidity
* **windspeed**	
* **count** - number of total rentals (Feature to be predicted)




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


We can observe that the dataset is unbalanced. So we have to focus on sampling to make each class in dependent variable to same ratio Or we can consider matrix like recall to find the performance of the algorithms.

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<h2>Getting Started</h2>

1.[RawData](https://github.com/Muhliscm/dsProjects/blob/main/telecome_churn_prediction/Model_building.ipynb) <br>
2.[Exploratory Data Analysis scripts](https://github.com/Muhliscm/dsProjects/blob/main/telecome_churn_prediction/credit_churn_EDA.ipynb)<br>
3.[Machine learning model building scripts](https://github.com/Muhliscm/dsProjects/blob/main/telecome_churn_prediction/Model_building.ipynb)<br>


<h2>💻 Algorithms used</h2>

* Logistic Regression

* Kernal-SVM

* SVM
  
* Random Forest
  
* KNN

* Decision Tree

* Naive Bayes	



<h3> Model Comparison </h3>

All the models are evaluated on the basis of the following evaluation metrics.

![image](images/model_perfomance.png)

<h3> Best Hyper-parameters </h3>

* Logistic Regression:
  
  C: 206.913808111479 <br>
  max_iter:100 <br>
  penalty: 'l2'<br>
  solver: 'newton-cg' <br>

<h2> :bulb: Conclusion</h2>

This project focuses on predicting  customers are likely to leave a service or cancel a subscription

* In eda we found that Independent people have more chance to churn. Especially single women.
 
* We Chose Logistic Regression as the best model for further improvements based on recall. Because our dataset was unbalanced.

* Among all these models logistic regression gives us a recall score of 0.802


* As a result of this project, telecom companies can better predict the churning customers and focus on methodologies to sustain them.
 
![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<!-- CREDITS -->
<h2 id="credits"> :scroll: Credits</h2>

MUHLIS CM | Data Scientist | Machine Learning Engineer 

<p> <i> Contact me for Data Science Project Collaborations</i></p>

[![LinkedIn Badge](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/muhliscm/)
[![GitHub Badge](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Muhliscm)
