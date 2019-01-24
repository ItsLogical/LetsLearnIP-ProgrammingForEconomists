'''
Assignment: Electronics
Created on 13 jun. 2018
@author: LetsLearnIP.com
'''

DISCOUNT_PERCENTAGE = 15

first_article_price = float(raw_input("Enter the price of the first article: "))
second_article_price = float(raw_input("Enter the price of the second article: "))
third_article_price = float(raw_input("Enter the price of the third article: "))

most_expensive_article_price = first_article_price
if (first_article_price >= second_article_price and first_article_price >= third_article_price):
    most_expensive_article_price = first_article_price
elif (second_article_price >= first_article_price and second_article_price >= third_article_price):
    most_expensive_article_price = first_article_price
elif (third_article_price >= second_article_price and third_article_price >= first_article_price):
    most_expensive_article_price = first_article_price

discount = most_expensive_article_price / 100 * DISCOUNT_PERCENTAGE
total_price = first_article_price + second_article_price + third_article_price - discount

print "Discount: %.2f" %discount
print "Total: %.2f" %total_price

''' Example input / output
Enter the price of the first article: 200
Enter the price of the second article: 50
Enter the price of the third article: 25
Discount: 30.00
Total: 245.00
'''