#Recommend a meal based on the
#current weather and time of day. Specifically, the program
#should recommend:
#
# - soup if it's cold and either evening or night
# - a biscuit if it's morning and cold
# - cereal if it's morning and hot, or whenever the time is night
# - pizza whenever it's either evening or night

hot = True
cold = False
morning = True
evening = False
night = False

#Soup: False
#Biscuit: False
#Cereal: True
#Pizza: False

soup = (cold and evening or night)
biscuit = (morning and cold)
cereal = (morning and hot or night)
pizza = (evening or night)

print("Soup:" , soup)
print("Biscuit:" , biscuit)
print("Cereal:" , cereal)
print("Pizza:" , pizza)


