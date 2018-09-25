# Estimator for change in stock price affecting overall value 
stock_price = 10
buying_amount = 2600 
discount = .1
percent_increase = 0

stock_owned_without_discount = buying_amount / stock_price 

# amount of stock owned
stock_owned = buying_amount / (stock_price*(1 - discount))
print("you own %s shares" % stock_owned)
# value without discount
value_without_discount = buying_amount
print("the value without the discount would be %s" % value_without_discount)

# value of the stock after discount
value_of_owned_stock = stock_owned * stock_price
print("the value after the discount is %s" % value_of_owned_stock)

# value gained on an individual stock 
value_gained_on_single_stock = stock_price/(1-discount) - stock_price
print("on each stock you own, you gain %s" %value_gained_on_single_stock)

# gains
gains = value_gained_on_single_stock * stock_owned
print("you would gain %s in total" % gains)

# price goes up by .5%
new_stock_price = stock_price*(1 + percent_increase)
gains_without_discount = new_stock_price * stock_owned_without_discount  - value_without_discount
gains_with_discount = new_stock_price * stock_owned - value_of_owned_stock
print("if the stock rose by %s percent to %s, you would have made %s " % (percent_increase, new_stock_price, gains_with_discount))
print("without the discount, you would have only made %s" % gains_without_discount)