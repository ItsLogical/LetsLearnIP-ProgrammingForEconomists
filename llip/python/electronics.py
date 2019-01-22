DISCOUNT_MULTIPLIER = 0.15

price1 = float(raw_input("Enter the price of the first article: "))
price2 = float(raw_input("Enter the price of the second article: "))
price3 = float(raw_input("Enter the price of the third article: "))

highest = price1
if price2 > highest :
    highest = price2
if price3 > highest :
    highest = price3

discount = highest * DISCOUNT_MULTIPLIER

print "Discount: %0.2f" % discount
print "Total: %0.2f" % (price1 + price2 + price3 - discount)