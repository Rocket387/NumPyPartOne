import numpy as np

a = np.array([10, 2, 2, 4, 5, 3, 9, 8, 9, 7, 1])
boolean_more_than_five = a > 5
print(boolean_more_than_five) # prints true or false

var_for_more_than_five = a[a > 5]
print(var_for_more_than_five) #prints value

var_more_than_five_less_than_two = a[(a > 5) | (a < 2)]
print(var_more_than_five_less_than_two)

porridge = np.array([79, 65, 50, 63, 56, 90, 85, 98, 79, 51])

cold = porridge[porridge < 60]
hot = porridge[porridge > 80]
just_right = porridge[(porridge >= 60) & (porridge <=80)]

print(cold)
print(hot)
print(just_right)