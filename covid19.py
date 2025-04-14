import pandas as pd
import matplotlib.pyplot as plt

# Reading the data from the CSV file
df = pd.read_csv('country_wise_latest.csv')

# Display sample data
print("Printing Covid-19 data sample:")
print(df.head())

# Basic statistics
print("\nPrinting basic statistics of Covid-19 data:")
print(df.describe())

