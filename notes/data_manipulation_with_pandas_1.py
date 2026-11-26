# 1. Data Aggregation- summarixing data through applying operations like mean, median to get meaningful sense out of it
# Sample operations mean(), median(), count(), unique(), nunique()
# 2. Grouped aggregation- To compare data within datasets. We identify a column to group, from this column we identify segments
# Before grouping, first check distinct values to see whether values match what we expect
# for this we use
import pandas as pd
orders_df = pd.read_csv("orders.csv", index_col=0)
print(orders_df['category'].unique())

category_groups = orders_df.groupby('category')

summary_df = category_groups.agg(
    order_count=('order_id', 'count')
)

print(summary_df)
# this gives you a table of categories and the number of orders in each category

# Example 2- This includes order count and unique user count
category_groups = orders_df.groupby('category')

summary_df = category_groups.agg(
    order_count=('order_id', 'count'),
    user_count=('user_id', 'nunique')
)

print(summary_df)
# this gives you a table with order_id and user_id counted values

# Example 3
category_groups = orders_df.groupby('category')

summary_df = category_groups.agg(
    order_count=('order_id', 'count'),
    user_count=('user_id', 'nunique'),
    revenue = ('amount', 'sum'),
    average_order_value = ('amount', 'mean')
)

print(summary_df)
# this gives us a table with order_count, user_count, revenue and average_order_amount

# EXAMPLE 6- This is to put the grouping column back to a normal column
category_groups = orders_df.groupby('category')

summary_df = category_groups.agg(
    order_count=('order_id', 'count'),
    user_count=('user_id', 'nunique'),
    revenue=('amount', 'sum'),
    avg_amount=('amount', 'mean')
)

summary_df = summary_df.reset_index()

print(summary_df)

# This is a summary of the above steps
summary_df = orders_df.groupby('category').agg(
    order_count=('order_id', 'count'),
    user_count=('user_id', 'nunique'),
    revenue=('amount', 'sum'),
    avg_amount=('amount', 'mean')
).reset_index()

print(summary_df)

# Example on TRIPS
# Creating a dataFrame
trips_df = pd.read_csv("trips.csv", index_col=0)
# Starting with displaying the dataset
print(trips_df)
# To see the ataset do that we select a column to group- as "ride_type"
# To display distinct values in ride_type
ride_type_present = trips_df['ride_type'].unique()
print(ride_type_present)
# Now use the same three-question framework: group by which column, summarize which columns, and apply which operations? Write code to calculate, for each ride_type, the total fare, average fare, and number of trips. Include reset_index() so the ride type is a regular column in your summary. The task instructions are available in the Instructions tab.
ride_type_groups = trips_df.groupby('ride_type').agg(
  total_fare = ('fare', 'sum'),
  average_fare = ('fare', 'mean'),
  number_of_trips = ('trip_id', 'count')
).reset_index()
print(ride_type_groups)

# Qualitative columns with a small number of distinct values
amount_groups = orders_df.groupby('amount')

summary_df = amount_groups.agg(
    order_count=('order_id', 'count'),
    user_count=('user_id', 'nunique'),
    revenue=('amount', 'sum'),
    avg_amount=('amount', 'mean')
)

summary_df = summary_df.reset_index()

print(summary_df)
# the results from this example make amount a poor grouping example

# FOR QUICK COUNTS
orders_df['category'].value_counts()
# this returns numbers
# view Value counts.png to see the results, 
# TO SEE EACH CATEGORY SHARE OF ALL COUNTS
orders_df['category'].value_counts(normalize=True)
# This returns propotions(can be converted to percentages)
# View Normalize_True.png to see the output

# Counting number of trips in Each ride type
trips_in_each_ride_type = trips_df['ride_type'].value_counts() 
print(trips_in_each_ride_type)
# You can look at trips in each ride type.png to see the output

# Example on proportions for ride type
proportions_ride_type = trips_df['ride_type'].value_counts(normalize=True)
print(proportions_ride_type)
# look at ride_type_proportions.png for output

# EXAMPLE ON SORTING after grouping
summary_df = summary_df.sort_values(by='revenue')

print(summary_df)
# to put the highest values first, we use
summary_df = summary_df.sort_values(by='revenue', ascending=False)

print(summary_df)

# EXAMPLE ON TRIPS
ride_type_groups = trips_df.groupby('ride_type')

summary_df = ride_type_groups.agg(
    revenue = ('fare', 'sum'),
    avg_fare = ('fare', 'mean'),
    trip_count = ('trip_id', 'count')
)

summary_df = summary_df.reset_index()

summary_df = summary_df.sort_values(by='trip_count', ascending=False)
summary_df

# look at highest number of trips.png to see the result

# EXAMPLE ON UNIQUE RIDERS COUNT
unique_riders = trips_df.groupby('ride_type')
nunique_riders = unique_riders.agg(
  unique_count = ('rider_id', 'nunique')
)
nunique_riders = nunique_riders.reset_index()
nunique_riders = nunique_riders.sort_values(by='unique_count')
nunique_riders







