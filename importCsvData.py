import numpy as np


#You are working on a team of climate scientists and
# one of your roles is to take the weekly temperature data and
# input into NumPy arrays for later analysis.
# The sensor records the temperature 4 times a day, at 0:00, 6:00, 12:00, and 18:00.
# You are given last weeks data (Monday through Friday) and asked to create a NumPy array.
# columns time of day
# rows day of week

#importing the data in the CSV temperature_data.csv
#temperatures = np.genfromtxt('temperatures.csv', delimiter=',')
temperatures = np.array([[43.6,	45.1,	58.8,	53,],
                          [47,	44.5,	58.3,	52.6,],
                          [46.7,	44.2, 	57.9,	52.2, ],
                          [46.5,	44.1,	57.6, 	51.9,],
                          [46.2,	43.9,	57.2,	51.5,]])
print(temperatures)
#The columns are the times, starting at 0:00, and the rows are days, starting on Monday,
# and the values are the recorded temperatures at that time on those days.

temperatures_fixed = temperatures + 3.0
#One of the researchers noticed that the sensor had been incorrectly zeroed
# and all of the recorded temperatures are 3.0 degrees too cold.
print(temperatures_fixed)

monday_temperatures = temperatures_fixed[0,:]
#Another researcher asked you for the temperature values from Monday.
print(monday_temperatures)


#“Hmmm, interesting” the researcher mumbles,
# “can you also give me the 6:00 AM data for Thursday and Friday?”
thursday_friday_morning = temperatures_fixed[3:5,1]
#3:5 = rows 3 & 4 (thrusday, friday), 1 = column number(6am)
print(thursday_friday_morning)

temperature_extremes = temperatures_fixed[(temperatures_fixed < 50) | (temperatures_fixed > 60)]
#Select all temperatures that are under 50 degrees or over 60 degrees and
# save them to a new array temperature_extremes.
print(temperature_extremes)
