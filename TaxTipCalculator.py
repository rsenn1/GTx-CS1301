meal_cost = 10.00
tax_rate = 0.08
tip_rate = 0.20

print("Subtotal:" , meal_cost)
tax_amount = meal_cost * tax_rate
print("Tax:" , tax_amount)
tip_amount = meal_cost * tip_rate
print("Tip:" , tip_amount)
total = meal_cost + tax_amount + tip_amount
print("Total:" , total)
