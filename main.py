#--------------------------------------------Libraries--------------------------------------------

from turtle import color, width
from numpy import size
import pandas as pd
import streamlit as st
import altair as alt
import seaborn as sns
import matplotlib.pyplot as plt


#--------------------------------------------Intro--------------------------------------------

st.write('''
# Grocery Store Performance
Simple web app that visualizes supermarket branch data. 
It looks at the predictor variables of the dataset to see if they correlate with the target variable.
The data comes from a kaggle dataset [here.](https://www.kaggle.com/datasets/surajjha101/stores-area-and-sales-data)
Libraries used: [pandas, streamlit, turtle, numpy, altair, seaborn, and matplotlib]

There are 896 store IDs.
In the dataset, there are 896 store IDs of a supermarket company.
''')

# read data
file_path = "Stores.csv"
stores_df = pd.read_csv(file_path)
# Store ID  Store_Area  Items_Available  Daily_Customer_Count  Store_Sales

# Create table describing stores_df
data_desc =pd.DataFrame({'Name':['Store ID', 'Store_Area', 'Items_Available', 'Daily_Customer_Count', 'Store Sales'],
 'Type':['Index', 'Predictor', 'Predictor', 'Predictor', 'Target'],
  'Description':['ID of the particular store', 'Physical Area of the store in square yards',
   'Number of different items available in the corresponding store', 'Number of customers who visited to stores on an average over month',
   'Sales in (US $) that stores made']})


# CSS to inject contained in a string--to hide the tables default index
hide_table_row_index = """
    <style>
    thead tr th:first-child {display:none}
    tbody th {display:none}
    </style>
    """

# Inject CSS with Markdown--to hide the tables default index
st.markdown(hide_table_row_index, unsafe_allow_html=True)

st.table(data_desc)


st.dataframe(stores_df, width=7000, height=300)

#--------------------------------------------Plots--------------------------------------------

# Plot top 50 performing stores
st.write('''
### Top 50 Performing Stores with Daily Customer Count and Store Area
''')
top_50 = stores_df.sort_values(by = ['Store_Sales'], ascending=False)[:50]
top_50_chart = alt.Chart(top_50).mark_circle().encode(x='Daily_Customer_Count', y='Store_Sales', size='Store_Area', color='Store_Area')
st.altair_chart(top_50_chart, use_container_width=True) 

# Plot bottom 50 performing stores
st.write('''
### Bottom 50 Performing Stores with Daily Customer Count and Store Area
''')
bottom_50 = stores_df.sort_values(by = ['Store_Sales'], ascending=True)[:50]
bottom_50_chart = alt.Chart(bottom_50).mark_circle().encode(x='Daily_Customer_Count', y='Store_Sales', size='Store_Area', color='Store_Area')
st.altair_chart(bottom_50_chart, use_container_width=True)

# Plot all store entries
st.write('''
### All Stores Daily Sales, Daily Customer Count, and Store Area
''')
all_stores_chart = alt.Chart(stores_df).mark_circle().encode(x='Daily_Customer_Count', y='Store_Sales', size='Store_Area', color='Store_Area')
st.altair_chart(all_stores_chart, use_container_width=True)

st.write('''
##### We have 3 predictor variables that we can compare with the target variable of Store_Sales
''')

# Plot relation of three predictor variables to Store_Sales
st.write('''
### Daily Customers vs. Store Sales
Based on the chart, there is little to no correlation between the amount of customers that enter the store and its daily sales.
''')
all_stores_chart = alt.Chart(stores_df).mark_circle().encode(x='Daily_Customer_Count', y='Store_Sales')
st.altair_chart(all_stores_chart, use_container_width=True)

st.write('''
### Items Available vs. Store Sales
There seems to be more correlation between Items_Available and Store_Sales than with Daily_Customer_Count, but it is still negligible.
''')
all_stores_chart = alt.Chart(stores_df).mark_circle().encode(x='Items_Available', y='Store_Sales')
st.altair_chart(all_stores_chart, use_container_width=True)

st.write('''
### Store Size vs. Store Sales
This plot seems very similar to the prevous one as far as correlation. The next step should be to quantify the correlation among predictors.
''')
all_stores_chart = alt.Chart(stores_df).mark_circle().encode(x='Store_Area', y='Store_Sales')
st.altair_chart(all_stores_chart, use_container_width=True)

# Create correlation heatmap and table
st.write('''
### Correlation Heatmap
We can see from the heatmap and the correlation table that no predictor variable shows even slight correlation with Store_Sales.
The two strongest predictors are Store_Area and Items_Available, but thay are not even above 0.1.
We were able to confirm the assumptions we made about the graph. Although all predictors perform poorly, Items_Available and Store_Area
were better predictors than Daily_Customer_Count.
''')
fig, ax = plt.subplots()
sns.heatmap(stores_df[['Store_Area', 'Items_Available', 'Daily_Customer_Count', 'Store_Sales']].corr(), ax=ax)
st.write(fig)

st.dataframe(stores_df[['Store_Area', 'Items_Available', 'Daily_Customer_Count', 'Store_Sales']].corr())

# Conculsion
st.write('''
### Conclusion
Although this dataset was clean and easy to work with, there are very few predictors. Also the predictors do not show any correlation.
It is not even worth it to calculate the p-values for statistical significance. Additionally, this dataset provided almost no background on 
what grocery chain this referred to. So, there was room to make additional assumption or create hypothesis about the data.
''')