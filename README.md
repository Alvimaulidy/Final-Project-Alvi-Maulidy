# Final Project Job Connector Data Science "Property Rent Estimator"
by Alvi Achmad Maulidy

## Final Project Goals
As property prices is always growing, the information how much a property or an appartment should be rent is still not right enough. Using the right method to predict, and that is a regression model, we can predict the actual base rent, which is a suitable range price based on the makret place.

## Dataset
The data was scraped from Immoscout24, the biggest real estate platform in Germany. Immoscout24 has listings for both rental properties and homes for sale, however, the data only contains offers for rental properties. The scraping process is described in this blog post and the corresponding code for scraping and minimal processing afterwards can be found in this Github repo. At a given time, all available offers were scraped from the site and saved. This process was repeated four times, so the data set contains offers from the dates 2018-09-22, 2019-05-10, 2019-10-08, and 2020-02.
source data: https://www.kaggle.com/corrieaar/apartment-rental-offers-in-germany
## Data Cleaning
this dataset contains rental offers from all around states in germany, thats why there are some sorting and cleaning i need to do:
1. Sorting the rental offers that are in main districts of Nordrhein Wesfalen state.
2. Droping extreme rent values and wrongly coded values in every categories of dataset.
3. make binaries variable to later be used for modelling the data.
4. make a overview data if the data has no missing values.
## Exporatory Data Analysis
Elaborations of a general overview of rental real estate in Nordrhein Westfalen.
## Modelling
Using Gradient Boosting, Linear Regression, Desicion Tree Regressor, and Random Forrest Regressor as base model and finding the best result of it. After that we can do tuning.

| Model                     |        MAE         |          MSE          |       R2Score         |
|---------------------------|--------------------|-----------------------|-----------------------|
|LinearRegression           | 144.74662854355935 |   46857.74579715562   |  0.7892173552276706   |
|GradientBoosting           | 132.81020087252773 |  42051.949485203426   |  0.8108355197304086   |
|DecisionTreeRegressor      | 186.37424734191382 |   84418.49670654729   |  0.6202558680364356   |
|RandomForestRegressor      | 135.37578429841625 |   42872.432266892254  |  0.8071446991889513   |

from these results we can see that Gradient Boosting as base model has best result with MAE 132.81 and R2Score 0.81.
To upgrade the result, we can find the best parameter by using hyperparameter GridSearchCV.
Result:
| Model                     |        MAE         |          MSE          |       R2Score         |
|---------------------------|--------------------|-----------------------|-----------------------|
|GradientBoosting           | 120.86784900683685 |   30890.77399237393   |  0.8610424182724532   |

as we can see that we have improved the result, but the MAE is still 120 euro and that is still a bit high for the error. In conclusion, there are still some rooms to reduce, that could be the adress of property, because a strategic location could impact the end result.

## Dashboard
Thanks to startbootstrap.com, I have built this dashbord to support Rent Predictor.

![img1](C:/Users/alvim/pwdk/FinalProject/Readme github/Home.png)

![img2](C:/Users/alvim/pwdk/FinalProject/Readme github/Marketing Anlysis.png)

![img3](C:/Users/alvim/pwdk/FinalProject/Readme github/predict 1.png)

![img4](C:/Users/alvim/pwdk/FinalProject/Readme github/predict 2.png)

![img5](C:/Users/alvim/pwdk/FinalProject/Readme github/result.png)
