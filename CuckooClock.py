current_hour = 5
time_of_day = "PM"

cuckoo = "Cuckoo!"*current_hour
colon = ": "
my_str = "The current time is {0}{1}{2}{3}" .format(current_hour,time_of_day,colon,cuckoo)
print(my_str)


