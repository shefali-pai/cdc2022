# Storm Stoppers

Introduction:
According to the storm data on the United States of America from NOAA, in 2021 978 people were killed directly and indirectly by storms. There are many different types of storms that can occur, such as tornados, thunderstorms, hail, wind, and more. While these are only a few of the storms that can impact people, they can still have devastating effects for communities and can cause deaths and injuries. These storms happen all year round and can be more prevalent based on location. The location can also impact the type of storm hitting the area. Using the NOAA dataset from the U.S., we wanted to analyze whether we could predict future storms based on the region they appear in. Based on the trends presented based on the type of storm that occurred, the latitude and longitude, and how many deaths that occurred, we can work to see when these storms will most likely occur as well as where. We are also interested in predicting how many deaths/injuries can occur based on these storms that occur.  

Assumptions used in Data Cleaning:
We cleaned our data using Python. When cleaning the data, we had to assume several conditions that would allow us to remove specific columns. Within the location data, we assumed several variables would not be necessary for our analysis. We assumed that columns relating to location outside of latitude and longitude, and specific region should be removed as they all conveyed similar or the same information. When working with the fatalities dataset, it was mostly good but we removed several of the additional dates included. The details dataset had the most information and required the most work. We had to requantify the property damage column and ensure all of the values had the same units. Additionally, we removed several other overlapping variables that were present in other datasets. Once the cleaning was complete, we joined all three datasets by the event identification number. 

Methodology:
In analyzing our data, we moved over to R Studio. In our analysis, we followed multiple approaches. In order to begin working with our variables we conducted an exploratory data analysis. 


From there we attempted a linear regression to see if there were relationships among variables in predicting months, or deaths using years, months, deaths, and event types. We used forward selection to select our variables. Forward selection picks one predictive variable, tests its predictive power and if it’s accurate, keeps the variable and moves onto the next term. It continues that trend until all the variables are attempted for fit.  From that analysis, we found the most correlation between predicting deaths through using the month and year. Our analysis said that no predictive variables should be used in predicting month specifically. When testing the linearity conditions of our model for predicting deaths, we see that linearity, zero mean, independence and constant variance. It should be noted that normality has some left skew but is otherwise well fit to a normal distribution. Although we found correlation between deaths and these other variables, we cannot say that there is causation as there may be other variables that are not within the dataset to cause deaths not noted here. 

In addition to the modeling, we wanted to visualize some of the trends we noticed. We took our dataset and created an interactive element in PowerBI. We wanted to see what sort of trends could be drawn out from a more friendly visualization software.

Challenges:
We faced two challenges in working with our dataset. The first was a lack of accurate documentation regarding the variables in the datasets. The second was the separation of the data into three different types of documentation. Oftentimes, this documentation had variables that were overlapping or somewhat contradictory to one another. 




