![brooklyn_bridge.jpeg](/Resources/Images/brooklyn_bridge.jpeg)
# Brooklyn Housing Analysis

Housing markets in the contemporary era provide a vast, diverse, and highly relatable set of data for beginners to work with. By looking at housing prices within Brooklyn, New York, we can adequately assess the housing market using a variety of tools. Brooklyn is the second most expensive borough, after Manhattan, and it also has a high residential turnaround. Creating a model based on the housing market in Brooklyn could be an invaluable tool. It may also prove useful to apply what we learn to assess other housing markets in the US, especially to home buyers who are looking to live in fast growing, highly populated, urban areas.

## Data

Data used in analysis was Brooklyn property sales from 2003-2017 sourced from kaggle.com by Tommy Wu. Original data was taken from the City of New York and cleaned up to be used for analysis.

## Research Questions

-   Can we predict future home prices in Brooklyn based on the year that the home was bought?
-   Does square footage of Brooklyn homes drastically effect the price of the home?
-   How do the neighborhoods compare in pricing within Brooklyn?
-   How have prices fluctuated within a specific range of years?
-   Are there any other factors that contribute to changes in housing prices?

## Technologies Used

### Google Slides Presentation
[Brooklyn Housing Analysis](https://docs.google.com/presentation/d/1S5SWDg1g-fo5eKKniRpoEzsBGJHBH_mhhbNbJsAG0nc/edit?usp=sharing).

### Data Cleaning and Analysis

Pandas will be used to clean the data and perform an exploratory analysis. Further analysis will be completed using Python and Plotly.

#### Data Cleaning: Excel / Pandas / Python
We used the pandas library to clean the data. First, we dropped any columns that were irrelevant or couldn't be interpreted. Next, we removed any rows with null values to ensure that the data was complete and accurate. After that, we built a helper script specifically to target the 'sale_price' column and identify and remove any outliers. 
![helper.png](/Resources/Images/helper.png)
This helped to ensure that the data in the 'sale_price' column was accurate and consistent, which is important for any further analysis or modeling that will be done. Finally, we made sure that all columns were of the correct data type, turning objects into integers. This ensures that we can use the data correctly in any further analysis or modeling.

#### Data Analysis


### Database Storage

Postgres(SQL) is the database we intend to use.

### Machine Learning Model

SciKitLearn is the machine learning library we'll be using to create a classifier.

We initially chose a Linear Regression model. The benefit of using a linear regression model is that it is easy to implement and computationally inexpensive. It can also be used to predict future values based on historical data. Linear regression can provide a good starting point for more complex models. However, it also makes strong assumptions about the data, such as linearity and equal variances of errors. If these assumptions are not met, the model may not be accurate. It also may not be able to capture complex relationships in the data. In addition, if you have a small data set or you have outliers in your data, a linear regression model can be affected and might not give accurate results.

We began by creating several plots in a jupyter notebook with plotly. We compared simple variables such as zip code and year of sale to the sale price of all the homes in the dataset.

Next, we decided to begin training our model with these preliminary features in order to predict the sale price, sale price being what we are testing on:

* block
* zip_code
* gross_sqft
* year_built
* sale_price
* SchoolDist
* YearBuilt

We chose these features as they initially seemed easy to incorporate with our linear regression model, as well as give us a better understanding of the relationships within our dataset. 

### Dashboard

Tableau will be used to display a dashboard/story. Google Slides is being used as a placeholder for visualization.

[**Tableau Public Link**](https://public.tableau.com/views/BrooklynHomeAnalysis/BrooklynHomesDashboardFinal?:language=en-US&:display_count=n&:origin=viz_share_link)

#### Interactive elements
-Interactive maps generated from zip codes of Brooklyn with heat map overlayed based on building type.

-Interactive data table showing details of sales and ml learning results with capability of filtering the table based on zip code and neighborhood.

![heatmap.png](/Resources/Images/heatmap.png)

## Communication Practices
We will primarily be using Slack for communication. We will also be using Zoom for group coordination on certain tasks. We are all collaborating on various facets of the project; choosing a dataset, building a database, choosing a machine learning model, connecting the database to the model, as well as updating the GitHub and README have been completed together as a team.


