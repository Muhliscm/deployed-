# Telecome Churn Prediction
<img src="/images/Customer-exit.png" height="600" width="720">

This project is a part of the [Kaggle](https://www.kaggle.com/) [Advanced Regression Challenge](https://www.kaggle.com/c/house-prices-advanced-regression-techniques).

#### -- Project Status: [Completed]

## Project Intro/Objective
The purpose of this project is to predict the price of real estate properties using machine learning regression

![Data Science](https://img.shields.io/badge/%20-%20Data%20Science-blueviolet?style=for-the-badge)
![Machine Learning](https://img.shields.io/badge/%20-Machine%20Learning-important?style=for-the-badge)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Anaconda](https://img.shields.io/badge/Anaconda-%2344A833.svg?style=for-the-badge&logo=anaconda&logoColor=white)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)

### Methods Used
* Inferential Statistics
* Descriptive statistics
* Exolanatory Data Analysis
* Future Engineering
* Future Selection
* Machine Learning
* Data Visualization
* Predictive Modeling
* etc.

### Technologies
* Python
* Numpy
* Pandas
* Matplotlib
* Seaborn
* Scikit learn
* jupyter
* etc. 

## Project Description
Data collected form kaggle advanced regression prediction challenge. Data visulized using univariate analysis, bivariate analysis, multivariates analysis.Data with different data type visualized accoridingly. Data preprocessing steps includes imputing missing values, log transformation of skewed data. future selection is done using correlation coefficient with a threshold of 0.8 and different regression models appied.

## Getting Started

1. Raw Data is being kept [click Here](https://github.com/Muhliscm/dsProjects/tree/main/30052021%20Housing%20data%20Kaggle/2.Prepared%20Data/house-prices-advanced-regression-techniques) within this repo.
2. Explonatory Data Analysis scripts are being kept [here](https://github.com/Muhliscm/dsProjects/blob/main/30052021%20Housing%20data%20Kaggle/8.%20Pipline/eda/20210817%20Eda-House_price_prediction_kaggle.ipynb)
3. Data preprocessing/transformation scripts are being kept [here](https://github.com/Muhliscm/dsProjects/blob/main/30052021%20Housing%20data%20Kaggle/8.%20Pipline/future%20engineering/20210818%20FE-House_price_prediction_kaggle.ipynb)
4. Future Selection scripts are being kept [here](https://github.com/Muhliscm/dsProjects/blob/main/30052021%20Housing%20data%20Kaggle/8.%20Pipline/future%20selection/20210818%20FS-House_price_prediction_kaggle.ipynb)
5. etc...


## Featured Notebooks/Analysis/Deliverables


   * [Multiple linear regression](https://github.com/Muhliscm/dsProjects/blob/main/30052021%20Housing%20data%20Kaggle/8.%20Pipline/model%20building%20and%20deployment/20210819%20Linear%20regression%20-House_price_prediction_kaggle%20Linear%20regression.ipynb)
   * [Random Forest regression](https://github.com/Muhliscm/dsProjects/blob/main/30052021%20Housing%20data%20Kaggle/8.%20Pipline/model%20building%20and%20deployment/20210309-random%20forest.ipynb)
   * [Tree Regression](https://github.com/Muhliscm/dsProjects/blob/main/30052021%20Housing%20data%20Kaggle/8.%20Pipline/model%20building%20and%20deployment/20210309-regression%20tree.ipynb)
   * [SVR](https://github.com/Muhliscm/dsProjects/blob/main/30052021%20Housing%20data%20Kaggle/8.%20Pipline/model%20building%20and%20deployment/20210309-SVR.ipynb)

   Penalized algorithms:
   * [Lasso Regression](https://github.com/Muhliscm/dsProjects/blob/main/30052021%20Housing%20data%20Kaggle/8.%20Pipline/model%20building%20and%20deployment/20210904-Lasso.ipynb)
   * [Ridge](https://github.com/Muhliscm/dsProjects/blob/main/30052021%20Housing%20data%20Kaggle/8.%20Pipline/model%20building%20and%20deployment/20210904-Ridge.ipynb)
   * [Elastic net](https://github.com/Muhliscm/dsProjects/blob/main/30052021%20Housing%20data%20Kaggle/8.%20Pipline/model%20building%20and%20deployment/20210904-Elastic%20net.ipynb)
   

# Model Selection and Conclusion

Random Forest has selected for future devolepment basis on the accuracy

<br>base model has an accuracy of 87.3 %
<br> tuned model using RandomizedSearchCV and improved accuracy to 88.3 %

Improvement of 1.13%. after boosting
