# ---------------------  IMPORT AND CREATE DATA OF COUNTRIES FROM API  --------------------- #
import pandas as pd
# import requests
# import csv
#
# # Step 1: Fetch data from REST Countries API
# url = "https://restcountries.com/v3.1/all"
# response = requests.get(url)
#
# # Ensure the request was successful
# if response.status_code == 200:
#     countries_data = response.json()
#
#     # Step 2: Define the CSV file and write headers
#     initial_csv_path = 'countries_data.csv'
#     with open(initial_csv_path, mode='w', newline='', encoding='utf-8') as file:
#         writer = csv.writer(file)
#         writer.writerow(["Country", "Capital", "Continent", "Population"])  # Headers
#
#         # Step 3: Extract data and write to CSV
#         for country in countries_data:
#             name = country.get("name", {}).get("common", "N/A")
#             capital = country.get("capital", ["N/A"])[0] if country.get("capital") else "N/A"
#             continent = country.get("region", "N/A")
#             population = country.get("population", "N/A")
#
#             writer.writerow([name, capital, continent, population])
#
#     print("Data saved to countries_data.csv")
# else:
#     print(f"Failed to retrieve data. HTTP Status code: {response.status_code}")
#

# -----------------------------  DATA ANALYSIS  ----------------------------- #


# Load data from CSV file
df = pd.read_csv('countries_data.csv')
print("The World Countries:")
print(df)

# Shape of the DataFrame (rows,column)=(250, 4)
print(df.shape)

# This will show you the First 10 entries(rows) in your dataset
print(df.head(10))

# This will show you the Last 10 entries(rows) in your dataset
print(df.tail(10))


# Filter Countries with populations over 10 million (no need to repeat this step)
print("Countries with Population Greater than 10 Million:")
countries_above_10_million = df[df['Population'] > 10_000_000]
print(countries_above_10_million)

# Extract the list of country names with population above 10 million
all_countries_above_10_million = countries_above_10_million['Country'].tolist()
print("Countries with populations above 10 million:")
print(all_countries_above_10_million)

# Extract the list of tuples containing Country and Capital for countries above 10 million
countries_and_capitals = countries_above_10_million[['Country', 'Capital']].values.tolist()
print("Countries and their capitals with populations above 10 million:")
print(countries_and_capitals)

# Check for a specific country (Germany)
Country = 'Germany'
print(f"Details for {Country}:")
print(df[df['Country'] == Country])  # Use '==' for a single value, not 'isin'

# Check for a specific Capital (Rome)
Contains_City = df[df['Capital'] == 'Rome']
print("Countries with the capital 'Rome':")
print(Contains_City)

# List of specific countries
specific_countries = ['Israel', 'Italy']

# Check if 'Country' column contains the specified countries
countries_in_specific_list = df[df['Country'].isin(specific_countries)]
print("Countries in the specific list (Israel and Italy):")
print(countries_in_specific_list)

# Set 'Capital' column as index
df_with_capital_as_index = df.set_index('Capital')
print("DataFrame with Capital as the index:")
print(df_with_capital_as_index)

# Filter the columns 'Country' and 'Population'
df_filter = df.filter(items=['Country', 'Population'])
print("Filtered DataFrame with only Country and Population:")
print(df_filter)


# Add a Rank column based on Population (descending)
df['Rank'] = df['Population'].rank(ascending=False, method='min')


# Convert the Rank column to integers
df['Rank'] = df['Rank'].astype(int)

# Save the updated DataFrame back to a CSV file
df.to_csv('updated_countries_data.csv', index=False)

# Set the Rank column as the index
df = df.set_index('Rank')

# Access a row by its rank (e.g., rank 1)
print(df.loc[1])
# Country            China
# Capital          Beijing
# Continent           Asia
# Population    1402112000
# Name: 1, dtype: object

print(df.loc[249])
#                                 Country Capital  Continent  Population
# Rank
# 249                       Bouvet Island     NaN  Antarctic           0
# 249   Heard Island and McDonald Islands     NaN  Antarctic           0


df = df.set_index('Country')  # Set 'Country' as the index
print(df)

# Filter by row with index 'Nicaragua'
print(df.loc['Switzerland'])

# Example: Filter specific columns for the row with index 'Nicaragua'
print(df.loc['Switzerland', ['Continent', 'Capital']])

# Filters the rows (not columns) where the index contains the substring 'United'
print(df[df.index.str.contains('United')])

# iloc is a method in Pandas used for integer-location-based indexing.
# df.iloc[row_index, column_index]
print(df.iloc[0,0])

print(df.iloc[2])       # Selects the 3rd row (index starts at 0)
print(df.iloc[:, 2])     # Selects the 4th column  : = all the rows


sort_Population = df[df['Population']>100_000_000].sort_values(by='Population')

# This filters the DataFrame to include only the rows where the Population is greater than 100 million
# df[df['Population'] > 100_000_000]
# This sorts the filtered data by the Population column in ascending order
# .sort_values(by='Population')
