#When taking out a mortgage (a type of loan) for a house, the
#mortgage is defined by three variables: the total cost of the
#house, the interest rate at which you will pay back the
#mortgage, and how many months you have to pay back the
#mortgage.

cost = 150000
rate = 0.0415
years = 15

months = years * 12
monthly_rate = rate / 12
total = (cost * months * monthly_rate) / (1 - ((1 + monthly_rate) ** -months))
final_cost = round(total, 2)
my_str = "The total cost of the house will be ${0}" .format(final_cost)
print(my_str)





