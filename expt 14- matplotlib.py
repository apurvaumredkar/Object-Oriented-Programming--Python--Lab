from matplotlib import pyplot as plt
import numpy as np
#question 1

x = np.linspace(0,10,100)
c1 = np.cos(x)
c2 = np.cos(x+1)
c3 = np.cos(x+2)
fig,ax = plt.subplots(nrows = 3)
ax[0].plot(x,c1)
ax[1].plot(x,c2)
ax[2].plot(x,c3)
plt.show()

#question 2
fig2,ax2 = plt.subplots(ncols = 3)
d1 = np.random.random((10,10))
