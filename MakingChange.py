amount = 67
quarters = amount // 25
amount  = amount - quarters * 25
dimes = amount // 10 
amount = amount - dimes * 10
nickels = amount // 5
amount = amount - nickels *5
pennies = amount 
print("Quarters:", quarters)
print("Dimes:", dimes)
print("Nickels:", nickels)
print("Pennies:", pennies)
