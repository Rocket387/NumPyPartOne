import numpy as np

# With a list
l = [1, 2, 3, 4, 5]
l_plus_3 = []
for i in range(len(l)):
    l_plus_3.append(l[i] + 3)

print(l_plus_3)

#with list is the same as with an array but less code
# With an array
a = np.array(l)
a_plus_3 = a + 3
print(a_plus_3)