# World Countries Data Analysis

This project fetches and analyzes data about countries from the [REST Countries API](https://restcountries.com/). The analysis includes filtering and sorting countries based on population, extracting specific information like capital cities, and more.

## Features
1. **Data Fetching**: Fetches country data (e.g., name, capital, continent, population) from the REST Countries API.
2. **Data Storage**: Saves the fetched data to a CSV file for future analysis.
3. **Data Analysis**:
   - Filters countries with populations greater than 10 million.
   - Lists countries and their capitals with populations above 10 million.
   - Filters countries by specific conditions (e.g., by population size, capital city, country names).
   - Ranks countries based on population and saves the updated DataFrame to a new CSV file.
   - Allows for integer-location-based indexing and string filtering with `iloc` and `str.contains`.
