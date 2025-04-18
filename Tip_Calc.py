def tip_calculator(tip_percent, bill):
    return tip_percent + bill / 100

tip_percent = float(input('Enter tip percentage (%): '))
bill_dollars = float(input('Enter the bill amount ($): '))

suggested_tip = tip_calculator(tip_percent, bill_dollars)

print('Your tip amount should be $' + str(suggested_tip))
print('Your total bill would be $'+ str(suggested_tip + bill_dollars))
