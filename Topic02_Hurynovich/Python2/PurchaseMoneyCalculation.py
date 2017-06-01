"""Program to calculate Total cost of items."""
DOLLAR_PART = input("Input dollar part of item cost:\n")
CENTS_PART = input("Input cents part of item cost:\n")
QUANTITY = input("Input quantity of items:\n")
TOTAL_COST = DOLLAR_PART*QUANTITY + CENTS_PART*QUANTITY/100.0
print "Total cost: {0}$".format(TOTAL_COST)
