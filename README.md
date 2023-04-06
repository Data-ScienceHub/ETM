# Hum Engagement Time Machine
## Griffin McCauley, Eric Tria, Theo Thormann, Jake Weinberg
### UVA MSDS Capstone Project 2023

### Project Overview

Working in collaboration with our sponsor, Hum, our group has sought to design and develop a multilayer perceptron (MLP) model which will help academic publishers more quickly and accurately identify users who display behaviors associated with high quality engagement and will hopefully provide a foundation for future projects aimed at subjects such as peer reviewer recruitment and relevant content recommendation. Using first-party customer data collected by Hum's customer data platform (CDP), we were able to extract streams of online actions and events performed by each user over their entire lifecycle, and, through careful and deliberate feature engineering, we managed to successfully derive a set of attributes upon which we could generate behavioral clusters indicative of high versus low quality user engagement. The four features we used to base our clustering and subsequent classifcation upon were the Number of Unique Articles per Event, the Percentage of Articles Reached Through Google, the Percentage of Content Consumed that was an Article, and the Number of Events Performed per Day Active. The two classes determined through applying k-means clustering on these features were then used assign training labels to each user in our dataset. ....

## Table of Contents

* Code
 * notebooks produced during the course of this project and documents various iterations and previous versions of our model and codebase
* Data
 * a collection of .csv files used in the training and testing of some of our early-stage models
* Resources
 * documents chronicling our progress over the course of the year and supplemental administrative materials related to our team's composition and organization
* Final
 * the code, data, and documentation for our final model

## Data

## Models

## Clustering

## Classification

## Results

## Manifest

* Code
 * eda
  * eda.ipynb
  * eda.py
  * eda_features.ipynb
  * env-format.txt
 * lib
  * aws_helper.py
  * file_helper.py
  * models.py
  * snowpark_conn.py
  * snowpark_runner.py
 * notebooks
  * classification.ipynb
  * clustering.ipynb
  * data_extraction.ipynb
  * de_requirements.txt
 * resources
  * aws_exeuction_role.png
  * aws_sagemaker_notebook.png
  * aws_tags.png
 * AWS_setup.md
 * ClusterAnalysis.ipynb
 * FinalModel.ipynb
 * HumMLP.ipynb
 * HumMLP_kNN.ipynb
 * IdleSequenceLengths.ipynb
 * RNN_sql_cleaning.ipynb
 * RNNdatacleaning.ipynb
 * profile_event.ipynb
 * stacked_hist.ipynb

* Data
 * RNNdata.csv
 * data.md
 * hum_schema.png
 * new_features_40.csv
 * reached_16_all.csv
 * reached_16_first_16.csv
 * training_labels.csv

* Final

* Resources
 * RNN_Models
  * Links
   * .gitkeep
   * Linksheet.md
  * PDFs
   * Predicting Customer Churn with Neural Networks in Keras _ by Kenny Hunt _ Towards Data Science.pdf
 * 02-13Update.pdf
 * 2022-02-19 New Model Proposal v2.pptx
 * 2023-01-29 DS6013 Project Proposal.pdf
 * Budget Proposal.pdf
 * Capstone Slides.pdf
 * CapstoneProjectBudget.pdf
 * DS6013 Capstone Project Proposal.pdf
 * EngagementTimeMachine_ProgressReport1.pdf
 * Final Project Report.pdf
 * Introduction - Hum-UVA_EngagementTimeMachine.pptx.pdf
 * Project Proposal.md
 * Retention Model Proposal v1.pdf
 * Talent Dashboard.pdf
 * Team Charter.pdf
 * Weekly Progress.md
 * eda.png
 * literature.txt
 * methods.png
 * model_2.png
