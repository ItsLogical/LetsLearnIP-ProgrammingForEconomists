'''
Assignment: VAT
Created on 13 jun. 2018
@author: LetsLearnIP.com
'''

VAT_PERCENTAGE = 21.00

price_of_article_with_vat = float(raw_input("Enter the price of an article including VAT: "))

vat_of_article = price_of_article_with_vat / (1 + VAT_PERCENTAGE / 100)
price_of_article_without_vat = price_of_article_with_vat - vat_of_article

print "This article will cost %.2f euro without %.2f%% VAT." %(price_of_article_without_vat, VAT_PERCENTAGE)