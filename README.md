# Hawaii-Climate-Analysis

The goal of this project was to extract, process, and analyze Hawaii climate data contained in a SQLite database, as well as construct an API for the raw climate data. Python with SQLAlchemy was utilized to store, inspect, and manipulate the data, while Python with Pandas, Numpy, and Matplotlib was used to generate meaningful visualizations in a common Jupyter Notebook. The API was developed in VS Code using Python with SQLAlchemy to store and inspect the data, while Python with Flask powered the development of the web interface.

# Questions

Climate Analysis

Precipitation Analysis

How much total precipitation did Hawaii receive during the last twelve months on record?

What are the summary statistics for that precipitation data?

## Weather Station Analysis

What are the most active weather stations based on observation count?
What are the maximum, minimum, and average temperatures for the most active weather station?

## Temperature Analysis

For the most active weather station, what are the most frequent temperature observations for the last twelve months on record?
Are the monthly averages of the recorded June and December temperature observations statistically significant?
Historical Analysis
Given a set of start and end dates, what are the maximum, minimum, and average temperatures for the same date range one year prior?
Given a set of start and end dates, what is the total precipitation for each weather station for the same date range one year prior?
Given a set of start and end dates, what are the daily maximum, minimum, and average temperatures for the same date range for all years on record?

## Climate API

## Static Routes

How much total precipitation did Hawaii receive during the last twelve months on record?
What weather stations are collecting climate data?
For the most active weather station, what is the recorded temperature for each day during the last twelve months on record?
Dynamic Routes
Given a start date, what are the maximum, minimum, and average temperatures for that date and all future dates on record?
Given a set of start and end dates, what are the maximum, minimum, and average temperatures for those dates and all in-between?

# Tasks

## Climate Analysis

Define the SQLAlchemy environment and establish a connection to the SQLite database.
Automap the database, reflect the tables as classes, and create a session.
Precipitation Analysis
Calculate the latest twelve month date range from the last available record in the database.
Query precipitation data for dates within that range and sort records from oldest to newest.
Plot the precipitation data for that date range.
Calculate the summary statistics for the precipitation data.
Create a Pandas data frame of the calculated statistical values.
Weather Station Analysis
Query weather station information and the number of records tied to each station, and sort by the latter in descending order.
Query maximum, minimum, and average observed temperature for all records from the most active weather station.
Temperature Analysis
Query temperature observations for the most active weather station in the aforementioned twelve month date range.
Create twelve equally sized temperature range bins and sort the temperature observations into the appropriate bins.
Plot a histogram of the temperature distribution for the most active weather station in that date range.
Query all June and December temperature observations and create separate Pandas data frames for each dataset.
Perform an independent t-test on the June and December datasets, and analyze the t-statistic and p-value.
Historical Analysis
Determine a set of start and end dates, and calculate dates one year prior to those dates.
Query maximum, minimum, and average observed temperature for all records on or within the year prior date range.
Plot a bar chart of the average observed temperature with an error bar reflecting the difference in maximum and minimum observed temperatures.
Query weather station information and the total precipitation recorded by each station for the year prior date range, and sort in descending order.
Query daily maximum, minimum, and average observed temperature for all days from any year matching dates within the year prior date range.
Combine records into a Pandas data frame and set date as the index.
Plot an area chart of the maximum, minimum, and average observed temperatures.

## Climate API

Define the Flask application environment and establish a connection to the SQLite database.
Automap the database, reflect the tables as classes, and create a session.
Define a path for the API home screen.
Define a function to display API functionality on the home screen.

## Static Routes

Define a path for the precipitation information API.
Define a function to query precipitation data for the last twelve months on record and display it in JSON format.
Define a path for the weather station information API.
Define a function to query weather station data and display it in JSON format.
Define a path for the temperature information API.
Define a function to query temperature data for the last twelve months on record and display it in JSON format.
Dynamic Routes
Define a path for the temperature information API that accepts a start date.
Define a function to import the given start date, query the temperature data on and after that date, calculate the appropriate daily summary values, and display those summary values in JSON format.
Define a path for the temperature information API that accepts start and end dates.
Define a function to import the given start and end dates, query the temperature data for and in-between those dates, calculate the appropriate daily summary values, and display those summary values in JSON format.

# Observations

## Climate Analysis

### Precipitation Analysis

For the majority of days in the most recent twelve month period, the total daily precipitation amounts in Hawaii were at or below two inches, with occasional days seeing anywhere up to nearly seven inches.
In the most recent twelve month period, there were 2021 recorded precipitation amounts, with a mean of 0.177 inches, a standard deviation of 0.461 inches, and a maximum of 6.7 inches.

## Weather Station Analysis

The most active weather station was Waihee (2772 observations), closely followed by Waikiki (2724 observations) and Kaneohe (2709 observations).
The maximum, minimum, and average temperatures for the most active weather station (Waihee) were 85, 54, and 71.7 degrees Fahrenheit respectively.

## Temperature Analysis

For the most active weather station (Waihee) in the most recent twelve month period, the majority of temperatures were between 69 and 79 degrees Fahrenheit, with occasional days seeing temperatures as high as 83 degrees Fahrenheit and as low as 59 degrees Fahrenheit.
The t-test of the June and December temperature data produced a p-value of 3.902e-191. This is far below the accepted cutoff of 0.05 and indicates that the averages of the two datasets are statistically significant.

## Historical Analysis

For a date range of 2017-12-18 to 2018-01-17, the average temperature for the same period one year prior was approximately 70 degrees Fahrenheit, with an error window of approximately 20 degrees Fahrenheit.
For a date range of 2017-12-18 to 2018-01-17, the Manoa Lyon Arbo weather station had the highest recorded precipitation amount of 10.93 inches for the same period one year prior. All other weather stations recorded less than 3.25 inches of precipitation in that prior year period.
For a date range of 2017-12-18 to 2018-01-17, the daily maximum, minimum, and average temperatures for the same days in all prior years were between 75 and 81 degrees Fahrenheit, 55 and 67 degrees Fahrenheit, and 68 and 73 degrees Fahrenheit respectively.

## Climate API

### Static Routes

The URL for the precipitation information API correctly displays all of the recorded precipitation amounts for each day during the latest year on record.
The URL for the weather station information API correctly displays all of weather stations that contributed daily observations to the baseline climate data.
The URL for the temperature information API correctly displays all of the observed temperatures for the most active weather station during the latest year on record.

## Dynamic Routes

For a given start date of 2016-01-01, the URL for the temperature information API returns the daily maximum, minimum, and average temperatures on and after that start date.
For a given start and end date set of 2016-01-01 and 2016-12-31, the URL for the temperature information API returns the daily maximum, minimum, and average temperatures for and in-between those start and end dates.

# Disclaimer

The baseline data used for this analysis was provided by a third party source and its accuracy in relation to actual Hawaii climate data is unknown.
