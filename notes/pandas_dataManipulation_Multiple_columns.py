# 1. Identify the columns to group by
# 2 First run a uniqueness check using the script below
unique_categories = orders_df[['location', 'category']].drop_duplicates()
print(unique_categories)

# 3. Go ahead and group
summary_df = orders_df.groupby(['location','category']).agg(
    order_count=('order_id', 'count'),
    user_count=('user_id', 'nunique'),
    revenue=('amount', 'sum'),
    avg_amount=('amount', 'mean')
).reset_index()

print(summary_df)

# EXAMPLE WITH EACH OPERATION ON A SEPARATE LINE USING PARENTHESIS
summary_df = (
    orders_df
    .groupby(['location', 'category'])
    .agg(
        order_count=('order_id', 'count'),
        user_count=('user_id', 'nunique'),
        revenue=('amount', 'sum'),
        avg_amount=('amount', 'mean'))
    .reset_index()
)

print(summary_df)
# EXAMPLE ON SWITCHING CATEGORY FIRST AND LOACTION SECOND
# This only changes arrangement of rows but calculations remain the same
summary_df = (
    orders_df
    .groupby(['category', 'location'])
    .agg(
        order_count=('order_id', 'count'),
        user_count=('user_id', 'nunique'),
        revenue=('amount', 'sum'),
        avg_amount=('amount', 'mean'))
    .reset_index()
)

print(summary_df)

# EXAMPLE ON TRIPS DATA
distinct = trips_df[['city','ride_type']].drop_duplicates()
distinct
# Average trip fare and trip count based on city
city_avg_fare_count = trips_df.groupby(['city', 'ride_type']).agg(
  average_trip_fare = ('fare', 'mean'),
  trip_count = ('trip_id', 'count')
).reset_index()
city_avg_fare_count

# TO SORT OUR GROUPING
summary_df = (
    orders_df
    .groupby(['location', 'category'])
    .agg(
        order_count=('order_id', 'count'),
        user_count=('user_id', 'nunique'),
        revenue=('amount', 'sum'),
        avg_amount=('amount', 'mean'))
    .reset_index()
)

summary_df = summary_df.sort_values(
    by=['location', 'revenue'],
    ascending=[True, False]
)

print(summary_df)
# NB: Look out for the order of columns while sorting
# EXERCISE1- Sorting average fare in descending order
summary_df = (
    trips_df
    .groupby(['city', 'ride_type'])
    .agg(
        avg_fare=('fare', 'mean'),
        trip_count=('trip_id', 'count'))
    .reset_index()
)

summary_df = summary_df.sort_values(
  by=['avg_fare'],
  ascending = [False]
)
summary_df
# EXERCISE 2 Sorting City in ascending order and Ridetype by avg_fare
summary_df = (
    trips_df
    .groupby(['city', 'ride_type'])
    .agg(
        avg_fare=('fare', 'mean'),
        trip_count=('trip_id', 'count'))
    .reset_index()
).sort_values(
  by=['city', 'avg_fare'],
  ascending=[True, False]
)
summary_df

# You can decide to remove a category for Uk eg grocery
orders_no_grocery_uk_df = orders_df[
    ~((orders_df['category'] == 'Grocery') & (orders_df['location'] == 'UK'))]
print(orders_no_grocery_uk_df)
# Then
summary_df = (
    orders_no_grocery_uk_df
    .groupby(['location', 'category'])
    .agg(
        order_count=('order_id', 'count'),
        user_count=('user_id', 'nunique'),
        revenue=('amount', 'sum'),
        avg_amount=('amount', 'mean'))
    .reset_index()
)

summary_df

# This example returns values without UK grocery
# This situation could mean data loss or querry error, or no activity during that period or an impossible combination








