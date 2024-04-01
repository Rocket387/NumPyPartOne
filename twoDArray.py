import numpy as np

coin_toss = np.array([1, 0, 0, 1, 0])
coin_toss_again = np.array([[0, 0, 1, 1, 1],
                            [1, 0, 0, 1, 0]])

# selects the first column
print(coin_toss_again[:,0])

# selects the second row
print(coin_toss_again[1,:])

# selects the first three elements of the first row
print(coin_toss_again[0,0:3])


#columns = Tanya, Manual, Adwoa, Jeremy, Cody
#rows = test1, test2, test3
student_scores = np.array([[92, 94, 88, 91, 87],
                           [79, 100, 86, 93, 91],
                           [87, 85, 72, 90, 92]])

tanya_test_3 = student_scores[2,0]
print(tanya_test_3) #87

cody_test_scores = student_scores[:,4]
print(cody_test_scores) #87, 91, 92

