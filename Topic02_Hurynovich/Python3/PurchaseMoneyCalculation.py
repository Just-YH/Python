"""Program to calculate Total cost of items."""
import re

COST = input("Input cost below:\n")
QUANTITY = input("Input quantity below:\n")
PRICE = re.search(r"\d+[.,]\d+", COST.replace(',', '.'),)
TOTAL_COST = (float(PRICE.group())) * int(QUANTITY)
print("Total cost: {0}$".format(TOTAL_COST))
