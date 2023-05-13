
Prints "Freezing" if the values
#represent a freezing temperature, and "Not freezing"
#if they don't.

temperature = -3.7
celsius = True

if temperature <= 0 and celsius == True:
    print("Freezing")
elif temperature <= 32 and celsius == False:
    print("Freezing")
else:
    print("Not freezing")



