VAT_PERCENTAGE = 21.00

price_including_vat = float(raw_input("Enter the price of an article including VAT: "))
price_excluding_vat = price_including_vat / (1 + VAT_PERCENTAGE / 100)
print "This article will cost %0.2f euro without %0.2f%% VAT." % (price_excluding_vat, VAT_PERCENTAGE)