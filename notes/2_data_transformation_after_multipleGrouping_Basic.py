# Transformation is a row level operation
# This creates new columns from existing ones by applying a formular or a function
# EXAMPLE 1
# Incase you want to convert the money spent on advertising per day from Dollars to Euros, 
# Using a conversion factor of 1USD = 0.92 Euros
# We multiply the column of USD by 0.92 in a new column

# Key to note, 
# 1- Which column give the input values
# 2- Which formular or function do we apply
import pandas as pd
campaign_spend_df = pd.read_csv('spend_data.csv')
campaign_spend_df["ad_spend_eur"] = campaign_spend_df["ad_spend_usd"] * 0.92
print(campaign_spend_df)
# the same transformation pattern applies on all other arithmetic operations, eg addition , subtraction, powers

# We can combine multiple columns in one formula
# EXAMPLE 2= Stock trading dataset
# Eachh row represents a sell trade, with information eg quantity sold, sale price, fees and average purchase price. 
# We will use these fields to calculate useful measure of trading perfomance
trades_df = pd.read_csv('trades.csv')
trades_df['net_sale_amount']= (trades_df['sell_price']*trades_df['quantity'])-trades_df['fees']
print(trades_df)
# RATIOS

# Now let’s apply ratios to the advertising scenario. The company has gradually increased its daily ad spend and wants to know whether that extra spending is paying off. Are additional orders coming at a reasonable cost, or are they becoming more expensive to acquire?
# Using campaign days data
# It records ad spend, paid sessions from people visiting the website, paid orders placed after those visits, and the resulting revenue and average fulfillment cost. Each row represents one campaign day. We’ll use these columns to examine the data next.
# To judge how well paid visits turn into orders, we’ll calculate the paid conversion rate (pCVR): the percentage of paid visitors who place an order. It helps compare how effectively campaign traffic converts into sales.
# For the second campaign day, the table shows 500 paid sessions and 50 paid orders, giving a pCVR of 10%. In general, calculate it as paid orders divided by paid sessions, then multiply by 100. Next, we’ll implement this metric in pandas.
campaign_performance_df = pd.read_csv('campaign.csv')
campaign_performance_df["pcvr"] = 100 * (
        campaign_performance_df["paid_orders"] / campaign_performance_df["paid_sessions"]
)
campaign_performance_df
# check 'pcvr calculation.png' to see the result
# The second metric is Cost per Order (CPO): the average advertising spend needed to acquire one order. It helps us assess the cost-efficiency of the campaign.
# For the second campaign day, $1,000 in ad spend divided by 50 orders gives a CPO of $20. In general, divide ad spend by paid orders for each day. Notice that a day with no orders has no defined cost per order; we’ll see how pandas represents that case when we implement the calculation.
campaign_performance_df["cpo"] = (
        campaign_performance_df["ad_spend"] / campaign_performance_df["paid_orders"]
)

campaign_performance_df
# Here, the code calculates Cost per Order by dividing ad spend by paid orders. Run it and notice what happens on the campaign day with zero orders: pandas produces inf (infinity) for that division rather than raising an error. This is a useful edge case to remember when working with ratios.
# The output shows the CPO for each campaign day. On the day with zero paid orders, pandas returns inf because dividing by zero makes the ratio undefined. Keep this behavior in mind when interpreting ratio results.

# STOCK TRADING SCENARIO
# At the end of the month, we want to assess the profit or loss on each sell trade using simple ratios. We’ll calculate a measure of how the sale price compares with the average buy price for each trade.
# For each trade, calculate the Return Multiple, which shows how many times over you got your money back. Divide the sell price by the average buy price. For example, a result of 1.5 means the sale price was 1.5 times the average buy price.
trades_df['return_multiple'] = (
  trades_df['sell_price']/trades_df['avg_buy_price']
)
trades_df

# PRICE CHANGE RATIO
# Now extend your work by calculating the Price Change Ratio for each trade. It expresses the percentage change from the average buy price to the sell price: 
# price_change_ratio = 100 × (sell_price−avg_buy_price)/avg_buy_price
# price_change_ratio=100×(sell_price−avg_buy_price)/avg_buy_price. A positive value indicates a gain; a negative value indicates a loss.
trades_df['price_change_ratio'] = (
  100 * (
    trades_df['sell_price']-trades_df['avg_buy_price']
  )/ trades_df['avg_buy_price']
)
trades_df
# the price change ratio is coverted into a percentage.
# METRICS CAN BE MISLEADING, 
# Observe the sample size, eg in (high pcvr with only 2 orders and 0 pcvr with 2 orders as well.png)
# pcvr on the first order is 50% yet, it produced 1 order since the total orders are 2, therfore 50%
# It is better to have a larger sample size than few samples
