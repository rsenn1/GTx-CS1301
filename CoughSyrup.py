dosage = 100
time_since_last_dose = 7
is_nighttime = False
took_something_cross_reactive = False

#You've been battling a cold. You're deciding whether
#to take cough syrup or not, and if so, how much to take.
#
#If it's nighttime, then you may double
#your dose since you won't be taking any until morning.
#
#However, if you've taken something cross-reactive
#(took_something_cross_reactive), then you should not take
#any cough syrup.

if not(is_nighttime) and not (took_something_cross_reactive):
    print(dosage*time_since_last_dose)
if took_something_cross_reactive:
    print(0)
if is_nighttime and not(took_something_cross_reactive):
    print(2*dosage*time_since_last_dose)


