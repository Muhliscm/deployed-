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

The training data contained 10,000 user details who used the service of the Capital Bikeshare program in Washington, D.C.
Test data has 7379 user details

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

3. Train test split, Transformation, Scaling, Future Selection etc.

4. Develop different models and evaluate them, Fine Tuning

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<h2>🛠️ Pre-processing </h2>

In this project, the dependent variable is the ‘number of total rented bike count’, the prediction of which gives us how many bicycles will be needed or rented in the future
### Correlation Matrix
![image](images/corr_matrix.png)
### Correlation of Target With other variables
![image](images/correlation.png)

### VIF
![image](images/Vif.png)

### Linear Regression Feature Importance
![image](images/lr_feature_imp.png)

### Random Forest Regression Feature Importance
![image](images/rf_feature_imp.png)







![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<h2>Getting Started</h2>

1.[RawData](https://github.com/Muhliscm/dsProjects/tree/main/bike-sharing-kaggle/data) <br>
2.[Exploratory Data Analysis scripts](https://github.com/Muhliscm/dsProjects/blob/main/bike-sharing-kaggle/EDA.ipynb)<br>
3.[Machine learning model building scripts](https://github.com/Muhliscm/dsProjects/blob/main/bike-sharing-kaggle/Feature_engineering.ipynb)<br>


<h2>💻 Algorithms used</h2>

* Linear Regression

* Random Forest Regression


<h3> Best Hyper-parameters </h3>

* Random Forest Regression:

 'n_estimators': 50 <br>
 'min_samples_split': 150<br>
 'min_samples_leaf': 50<br>
 'max_depth': 8<br>
  
<h2> :bulb: Conclusion</h2>

This project focuses on how many bicycles will be needed or rented in the future

* In eda we found that Data is not linear. So linear regression gives a very poor score. So we used no linear models  
 
* We Chose random forest regression as the best model for further improvements based on recall

* Among all these models random forest regression gives us a r2 score of 0.78

*  Companies can use this prediction for their bike-sharing system optimization
 
![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<!-- CREDITS -->
<h2 id="credits"> :scroll: Credits</h2>

MUHLIS CM | Data Scientist | Machine Learning Engineer 

<p> <i> Contact me for Data Science Project Collaborations</i></p>

[![LinkedIn Badge](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/muhliscm/)
[![GitHub Badge](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Muhliscm)
