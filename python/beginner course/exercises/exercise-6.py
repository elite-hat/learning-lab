# Price of House is $1M
# If buyer has good credit, they need to put down 10%
# Otherwise they need to put down 20%

# print the down payment

housePrice = 1000000
goodCredit = True
if goodCredit:
    print(housePrice * (10/100))
else:
    print(housePrice * (20/100))

# SOLUTION

price = 1000000
has_good_credit = True
if has_good_credit:
    down_payment = price * 0.1
else:
    down_payment = price * 0.2
print(f"Down Payment: ${down_payment}")