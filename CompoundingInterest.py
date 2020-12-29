#Find the amount of money in an account with the initial investment, interest rate, and number of years.

principal = 5000
rate = 0.05
time = 5

import math
e = math.e
amount = principal * e ** (rate * time)
print("After " + str(time) + " years invested with a " + str(rate) + " interest rate, a $" + str(principal) + " investment will be worth $" + str(round(amount, 2)) + ".")



