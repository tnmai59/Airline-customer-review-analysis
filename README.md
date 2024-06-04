# Airline customer review analysis
This project used multiple machine learning methods, integrating Tabular data and text data to investigate factors affecting customers decision to promote an airline

# Data
The data is crawled from Skytrax, which is a verified airline review website. The data consists of text review, rating scores on 5 scaled and a binary variable.
![image](https://github.com/tnmai59/Airline-customer-review-analysis/assets/141378792/75385f3f-1e70-4065-b402-5fe965b0c754)

From crawled data, 2 datasets were created. One is the tabular data which is rating scores, the remaining is text data which is reviews.

# Modeling
- For tabular data, multiple ML models was used to predict the target variable (Recommended) based on rating scores, then explainAI model which are LIME, SHAP and permutation score were used to debug and analyze factors driven the prediction to target variables
- For text data: Using LDA identified topics within the customer reviews

# Result
- Best model: GradientBoosting with 95% accuracy, cost effective (Value For Money) is the most important factor affect customer decision to recommend an airline to others
- Discover 2 topic customers interested in which are "Delay" and "Online Service"

# Future work
- Estimate how much "Delay" and "Online Service" affect customer decision by combining related text reviews into tabular data for prediction.


