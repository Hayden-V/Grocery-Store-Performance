# Grocery Store Performance
Simple web app that visualizes supermarket branch data. 
It looks at the predictor variables of the dataset to see if they correlate with the target variable.
The data comes from a kaggle dataset [here.](https://www.kaggle.com/datasets/surajjha101/stores-area-and-sales-data)

### Conclusion
Although this dataset was clean and easy to work with, there are very few predictors. Also the predictors do not show any correlation.
It is not even worth it to calculate the p-values for statistical significance. Additionally, this dataset provided almost no background on 
what grocery chain this referred to. So, there was room to make additional assumption or create hypothesis about the data. Run the file to see how I arrived at this conclusion.

### How to run
1. Download the repository.
1. Setup a virtual environment with all files inside.
1. Activate your virtual environment and use "pip install -r requirements.txt" to install all packages.
1. View the web app with the following command "streamlit run main.py"
1. Here is an example:(venv) C:\Users\User\dev\super_market>streamlit run main.py
1. The program will open a tab in your web browser and display the app.
