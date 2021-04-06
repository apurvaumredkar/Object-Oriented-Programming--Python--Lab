import numpy as np
from matplotlib import pyplot as plt
#WIND STATISTICS
print('WIND STATISTICS\n')
#importing the data file
wd = np.loadtxt('C:/Users/apoor/Desktop/OOP Practicals/Numpy Resources/wind.data')

#data over all locations at all times
min1 = np.min(wd[:,3:])
print("Minimum windspeed over all locations at all times:",min1)
max1 = np.max(wd[:,3:])
print("Maximum windspeed over all locations at all times:",max1)
mean1 = np.mean(wd[:,3:])
print("Mean of windspeeds over all locations at all times:",mean1)
std1 = np.std(wd[:,3:])
print("Standard Deviation of windspeeds over all locations at all times:",std1)

#data at each locations over all the days
min2 = np.min(wd[:,3:],axis=-2)
print("\nMinimum windspeed at each location over all the days:",min2)
max2 = np.max(wd[:,3:],axis=-2)
print("Maximum windspeed at each location over all the days:",max2)
mean2 = np.mean(wd[:,3:],axis=-2)
print("Mean windspeed at each location over all the days:",mean2)
std2 = np.std(wd[:,3:],axis=-2)
print("Standard Deviation of windspeeds at each location over all the days",std2)

#data across all locations at each day
min3 = np.min(wd[:,3:],axis=-1)
print("\nMinimum windspeed across all locations at each day:",min3,"Size:",len(min3))
max3 = np.max(wd[:,3:],axis=-1)
print("Maximum windspeed across all locations at each day:",max3,"Size:",len(max3))
mean3 = np.mean(wd[:,3:],axis=-1)
print("Mean windspeed across all locations at each day:",mean3,"Size:",len(mean3))
std3 = np.std(wd[:,3:],axis=-1)
print("Standard Deviation of windspeed across all locations at each day:",std3,"Size:",len(std3))

#location with max windspeed on each day
locmax = np.argmax(wd[:,3:],axis=-1)+1
print("\nLocation with maximum windspeeds on each day",locmax)

#date of maximum windspeed
max4 = np.where(np.max(wd[:,3:]))
print("\nYear:",int(wd[int(max4[0])][0]), "Month:",int(wd[int(max4[0])][1]),"Day:",int(wd[int(max4[0])][2]))

#average windspeed for the month of january for each location
j = wd[wd[:,1] == 1]
mean4 = j[:,3:].mean(axis=-2)
print("\nAverage Windspeed for January for each location",mean4)

print("\n\nDOW SELECTION\n")


#DOW SELECTION
dow = np.genfromtxt('C:/Users/apoor/Desktop/OOP Practicals/Numpy Resources/dow.csv',delimiter=',')
OPEN = 0
HIGH = 1
LOW = 2
CLOSE = 3
VOLUME = 4
ADJ_CLOSE = 5

#create a mask array where volume > 5.5 billion
mask = dow[:,VOLUME] >5500000000
print("Created mask:\n",mask)

#number of rows in mask
print("\nNo. of rows in mask:",np.sum(mask))

#find the index of row where volume > 5.5 billion
print("\nRows where volume > 5.5 billion:\n",np.where(mask)[0])