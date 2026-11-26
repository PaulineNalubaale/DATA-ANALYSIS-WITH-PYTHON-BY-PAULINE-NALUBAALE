# DATA FILTERING
# Welcome! In this lesson, we’ll explore data filtering, a common way to focus on the records relevant to a question. It can answer a question directly or prepare a smaller, relevant subset for further analysis—useful whether we’re examining business data or petroleum trends.
# To ground our work in a business scenario, we’ll use the Fortune 50, a smaller list drawn from the Fortune 500. The full Fortune 500 ranks the largest U.S. corporations by revenue; the Fortune 50 gives us a manageable set of companies to explore
# First inspect the data given
# let’s select only the columns we need. This keeps the table focused and makes the filtering results easier to verify. In the code here, loc[] receives : first, meaning keep all rows, then a list of column names, which determines the columns and their order.
import pandas as pd
fortune_full_df = pd.read_csv('fortune500.csv')

fortune_df = fortune_full_df.loc[ :, ["company",
                                      "sector",
                                      "rank_2025",
                                      "revenue",
                                      "profit",
                                      "market_cap"]]

fortune_df
# column selection is useful at two points. First, during initial data acquisition, select the fields relevant to your project. Later, repeat it as different analysis tasks need different subsets of columns
# Imagine we’re financial analysts looking at the Fortune 50. Our goal is to find the companies that operate in the Technology sector. The full dataset contains many sectors, so filtering is the right operation: it lets us keep only the rows that meet this condition. Take a look at the data we’ve selected so far, then we’ll apply the filter.
fortune_tech_df = fortune_df.loc[fortune_df["sector"] == "Technology"]

fortune_tech_df
# The result contains six Technology companies, including Apple, Alphabet, Microsoft, and Nvidia. In the code, the condition checks each row’s sector value; loc[] keeps only the rows where that comparison is true. The filtering condition goes in the first argument of loc[], replacing the : we used earlier to keep all rows.
# EXERCISE 1
# Selecting only 3 columns
fortune_df = fortune_full_df.loc[
  :, ["company", 
      "profit", 
      "sector"]
  ]
fortune_df
# Among these companies in this example are those with a negative profit, lets select them out
fortune_df = fortune_df[fortune_df['profit']<0]
fortune_df
# To select and Filter
fortune_full_df = fortune_full_df.loc[:, ["company", 
  "profit"]]
fortune_full_df = fortune_full_df[fortune_full_df["profit"] < 0]
fortune_full_df
# Companies valued at more than 1 trillion dollars
fortune_df = fortune_df.loc[
  :, [
    "company",
    "market_cap"
  ]
]
fortune_df = fortune_df[fortune_df["market_cap"]>1000000]
fortune_df

# BOOLEAN MASKS OR A FLAG
# Boolean mask (also called a flag): a series of True and False values, one for each company. 
# True marks companies whose sector matches Technology; False marks the others. Masks are useful beyond filtering too—for example, to count matches, support conditional operations, or validate data.
# Example
filtering_condition = fortune_df["sector"] == "Technology"

filtering_condition
# The result here is a boolean mask

# The mask contains one value per row, and loc[] keeps the rows marked True. In a dataframe
filtering_condition = fortune_df["sector"] == "Technology"

fortune_tech_df = fortune_df.loc[filtering_condition]

fortune_tech_df
# The output matches the earlier one-step filter: the same six Technology companies are kept. This confirms that passing the saved Boolean mask to loc[] gives the same result as placing the condition directly inside loc[].
# Filtering companies with market cap greater than 1 trillion
fortune_mkt_df = fortune_df["market_cap"] > 1000000
fortune_df = fortune_df.loc[fortune_mkt_df]
fortune_df
# PARTIAL STRING MATCHING
# To find distinct sectors
unique_sectors = fortune_df["sector"].unique()
unique_sectors
# Below is the result, 
['Retail' 'Health Care' 'Technology' 'Financials' 'Energy' 'Automotive' 'Food & Drug Stores' 'Telecommunications' 'Food, Beverages & Tobacco' 'Media' 'Transportation']
# It is shows the list with lists the distinct sector labels, including two different food-related labels: “Food & Drug Stores” and “Food, Beverages & Tobacco.” That shows why matching part of a label can help find related categories without listing every variant.
# To find food companies
food_companies_df = fortune_df.loc[fortune_df['sector'].str.contains('Food')]
food_companies_df.loc[:, ['company', 'sector']]
 # str.contains()This checks whether the specified word appears anywhere in sector
# Next, we’ll compare matching text anywhere with matching text at the beginning. Run this code to find sector labels that start with Food, then compare its results with the previous search.

food_companies_df = fortune_df.loc[fortune_df['sector'].str.startswith('Food')]
food_companies_df.loc[:, ['company', 'sector']]
# str.startswith() This gets only companies that have sectors starting with Food

# For companies in sectors of Health care or Healthcare, 
health_care_companies = fortune_df.loc[fortune_df['sector'].str.contains('Health')]
health_care_companies.loc[:, ['company', 'sector']]
# For companies whose names end with group
companies_ending_group = fortune_df.loc[fortune_df['company'].str.endswith('Group')]
companies_ending_group

# MISSING VALUES
# Now let’s consider missing values in the Fortune 50 data. Some companies have no employee-count value, which may mean information was lost and needs follow-up.
# Missing-value filtering can support business logic, when an absence itself matters, and data quality, when we need to find incomplete records to exclude or fill. This differs from filtering for an empty string or zero.
# In pandas, missing values can appear as NaN in numeric columns or None in text columns. isna() detects either kind of missing value. Run the code to find which Fortune 50 companies have no employee-count data.
# Lets find which companies have no employee count
missing_employees_df = fortune_df.loc[fortune_df['employees'].isna()]
missing_employees_df.loc[:, ['company', 'employees']]

# isna() returns True for rows where that value is missing, allowing the filter to keep those companies.
has_employees_df = fortune_df.loc[fortune_df['employees'].notna()]
has_employees_df.loc[:, ['company', 'employees']]

# Companies with missing market cap
companies_missing_mktcap = fortune_df.loc[fortune_df['market_cap'].isna()]
companies_missing_mktcap.loc[:, ['company', 'market_cap']]


