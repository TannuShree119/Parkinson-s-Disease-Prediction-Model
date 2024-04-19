# Parkinsons-Disease-Prediction-Model

## Overview

Welcome to my first project repository! This project aims to develop a machine learning model to predict the presence of Parkinson's disease based on various biomedical voice measurements. The dataset used in this project contains biomedical voice measurements from people with and without Parkinson's disease.

![Basal-ganglia-cropped](https://github.com/TannuShree119/Parkinsons-Disease-Prediction-Model/assets/159888826/734fdccb-7c0c-4cdc-b74c-a39fccfbc7bf)

## Dataset

The Parkinson's disease dataset used in this project is sourced from a [Kaggle Dataset](https://www.kaggle.com/datasets/thecansin/parkinsons-data-set)

## Data loading, exploration and pre-processing
First the dataset was loaded and explored to understand its structure, dimensions, and data types. Then the dataset was preprocessed by separating the features and the target variable, calculating the correlation matrix, and visualizing the feature distributions.

## Data Splitting and Standardization
Now the dataset was split into training and testing sets, and the features are standardized using StandardScaler

## Model Training
A Support Vector Machine (SVM) model with a linear kernel was trained on the standardized training data

## Model Evaluation
The performance of the trained SVM model was evaluated using the accuracy score and a confusion matrix

![image_2024-04-19_151625376](https://github.com/TannuShree119/Parkinsons-Disease-Prediction-Model/assets/159888826/c609fe5e-d188-4fc9-b0f1-982c591067f9)

## Building a Predictive System
A predictive system was built where an example input data was standardized and used to make a prediction using the trained SVM model.

## Deploying the model
 Lastly after validating the result and the model, it was deployed using StreamLit, to make the testing of model for users an easy process

 Here is the preview of the application:

 


