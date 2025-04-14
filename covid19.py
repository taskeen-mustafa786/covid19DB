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

# Show list of available countries
countries = df['Country/Region'].tolist()
print("\nAvailable countries:\n")
print(", ".join(countries))

# Take country name input from the user
country = input("\nEnter the country name from the above list to view COVID-19 stats: ")

# Check if the entered country exists in the dataset (case-insensitive match)
matching_countries = [c for c in countries if c.lower() == country.lower()]

if matching_countries:
    country_data = df[df['Country/Region'].str.lower() == country.lower()]

    # Extract values
    confirmed = country_data['Confirmed'].values[0]
    recovered = country_data['Recovered'].values[0]
    deaths = country_data['Deaths'].values[0]

    # Plot
    plt.figure(figsize=(8, 5))
    labels = ['Confirmed', 'Recovered', 'Deaths']
    counts = [confirmed, recovered, deaths]
    colors = ['blue', 'green', 'red']

    plt.bar(labels, counts, color=colors)
    plt.title(f'COVID-19 Summary for {matching_countries[0]}')
    plt.ylabel('Count')
    plt.grid(axis='y')
    plt.tight_layout()

    # Show the plot
    plt.show()
else:
    print(f"\nCountry '{country}' not found in the dataset. Please check the spelling and try again.")
