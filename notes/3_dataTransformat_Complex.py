# Welcome! In the previous lesson, you used basic arithmetic transformations to create and work with new columns. Now we’ll build on that foundation to handle more involved questions in data—useful when you need to connect several pieces of information to understand a real-world result
# To make this practical, we’ll continue with the marketing analytics scenario. Imagine we work at an online sportswear company that sells directly through its website, using paid ads on platforms such as Instagram and TikTok to bring in visitors.

# Now we want to understand the actual contribution of those ads after direct costs are included. Is the scenario clear so far?
# Each row represents one day in the seven-day campaign, and the columns describe ad spend, paid sessions and orders, revenue, and average fulfillment cost. This is the data we’ll use to explore the campaign.
# To assess whether the campaign is paying off after direct costs, we’ll calculate ad contribution for each day. It measures revenue left after subtracting advertising spend and fulfillment costs.

# Ad contribution = revenue − ad spend − (paid orders × average fulfillment cost).

# The fulfillment cost is per order, so we multiply it by the number of paid orders before subtracting it. This gives us a net dollar contribution for each campaign day.
import pandas as pd
campaign_df = pd.read_csv('addcampaign.csv')
campaign_df["ad_contribution"] = (
    campaign_df["revenue"] -
    campaign_df["ad_spend"] -
    (campaign_df["paid_orders"] * campaign_df["avg_fulfillment_cost"])
)

campaign_df
# This example contains an error for missing parentheses so it gives us wrong values
# let’s see how operator precedence can change a result. In this example, the expression calculates gross profit per order, but without grouping the subtraction, division happens first. Notice the calculation in Lines 23 and compare it with the intended formula: revenue minus ad spend, then divided by paid orders. What seems off about the result?
campaign_df["gross_profit_per_order"] = (
    campaign_df["revenue"] - campaign_df["ad_spend"] / campaign_df["paid_orders"]
)
campaign_df[["campaign_day", "revenue", "ad_spend", "paid_orders",
             "gross_profit_per_order"]]

# Below is the corrected expression
campaign_df["gross_profit_per_order"] = (
    (campaign_df["revenue"] - campaign_df["ad_spend"]) / campaign_df["paid_orders"]
)

campaign_df[["campaign_day", "revenue", "ad_spend", "paid_orders",
             "gross_profit_per_order"]]

# CONTRIBUTION RATE
# Next, let's look at a second metric: contribution rate. It shows what percentage of revenue remains as contribution after covering ad and fulfillment costs.
# contribution rate = 100 × ad contribution / revenue
# Notice that this formula depends on the ad_contribution column we already created, so we can reuse it rather than rebuilding the whole calculation.
campaign_df["contribution_rate"] = (
    100 * campaign_df["ad_contribution"] / campaign_df["revenue"]
)

campaign_df
# Now let’s apply these complex transformation techniques to a stock-trading scenario. We have records of trades made during the month and want to calculate metrics that help us understand trading performance.
# In the data, Each row represents one sell trade made during the month. The columns identify the share and quantity, its sell price and fees, and the average buy price per share.
# Let’s calculate the margin for each trade. Margin is the sale proceeds minus the platform fees and the original buy cost. 
# Note that for margins, it works with total
trades_df = pd.read_csv('stocktrades.csv')
trades_df['margin_trade'] = (
  trades_df['sell_price']*trades_df['quantity'] -(
    (trades_df['fees']) + (trades_df['avg_buy_price']* trades_df['quantity'])
    )
  )
trades_df
# Example on Margin ratio
# Now calculate the margin ratio for each trade. It uses the margin you just calculated, divided by the total buy cost, then multiplied by 100
trades_df['margin_ratio']= 100 * (
  trades_df['margin']/ (
    trades_df['quantity']* trades_df['avg_buy_price']
  )
)
trades_df
# % Percent of Total
# Next, we’ll explore percent of total: expressing a value as a share of the whole, scaled to 100. This makes comparisons clearer when totals differ, because it puts values on a common scale
# To make percent of total useful, let’s return to the sportswear company. It sells products across five categories, and we want to understand how much each category contributed to the previous month’s total revenue and profit. That comparison can help the business see how categories perform relative to one another and spot opportunities for growth.
# We are going to use the previous month’s category summary. Each row represents one sportswear category, with its revenue and margin. Margin is revenue minus cost, so it can be positive or negative.
# look at (sports wear category.png)
# the negatives in some categories indicates those categories lost money

# CALCULATING REVENUE PERCENT OF TOTAL AND MARGIN PERCENT OF TOTAL
# Let’s translate the two formulas into pandas. .sum() calculates the total of a column across all rows, so each row’s revenue or margin can be divided by that total and multiplied by 100. The code applies this directly to both columns, creating revenue_pot and margin_pot. 
category_sales_df = pd.read_csv('category.csv')
category_sales_df["revenue_pot"] = (100 * category_sales_df["revenue"] /
                                    category_sales_df["revenue"].sum())

category_sales_df["margin_pot"] = (100 * category_sales_df["margin"] /
                                   category_sales_df["margin"].sum())

category_sales_df
# The round() function can round a column to a chosen number of decimal places. In this example, the two percentage columns are rounded to two decimal places. 
# Rounding is one example of a transformation function, its a ready made operation for changing data
category_sales_df["revenue_pot"] = round(category_sales_df["revenue_pot"], 2)

category_sales_df["margin_pot"] = round(category_sales_df["margin_pot"], 2)

category_sales_df

# Let’s apply percent of total to a stock portfolio. At the end of the month, we want to understand what proportion of the portfolio’s total value comes from each sector.
# Using (portfolio data example.png)
# Each row represents a sector and includes its total value in the portfolio and the number of shares held in that sector.
# Calculating value % of total
portfolio_df = pd.read_csv('portfolio.csv')
portfolio_df['value_pot'] = (
  (100 * portfolio_df['value'])/portfolio_df['value'].sum()
)
portfolio_df

# IMPORTANT 
# heads-up on when percentage metrics can be misleading?
# In the category example, Sportswear and Shoes contribute about 58% and 71% of total margin, so together they exceed 100%. What do you think causes that, even though all the category percentages add up to 100%?
# Explanation, 
# My answer, I would say its because of the sum of margins
# Yes—the total margin is the denominator, and the negative margins from Bags and Accessories reduce that total. So the positive categories’ shares can add up to more than 100%, while the negative shares bring the overall percentages back to 100%.
# For example, this resembles petroleum economics when profitable fields are measured against net portfolio profit after loss-making fields: the profitable fields’ shares can exceed 100% of that smaller net total. Always check whether negative values affect the denominator before interpreting percent-of-total results. Any questions?

