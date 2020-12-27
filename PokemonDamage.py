#In the Pokemon game franchise, damage is calculated using this formula:
#https://studio.edx.org/asset-v1:GTx+CS1301+1T2017+type@asset+block@DamageCalc.png
#
#In that formula, the variable Modifier is calculated using this formula:
#https://studio.edx.org/asset-v1:GTx+CS1301+1T2017+type@asset+block@ModifierCalc.png

STAB = 1
Type = 0.25
Critical = 2
Other = 1
Random = 1
Level = 50
Attack = 125
Defense = 110
Base = 60

modifier = STAB * Type * Critical * Other * Random
print(((2 * Level + 10) / 250 * (Attack / Defense) * Base + 2) * modifier)
