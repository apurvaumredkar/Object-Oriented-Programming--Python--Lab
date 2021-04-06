import numpy as np
import random as rd

#null vector of size 10
a = np.empty(10)
print(a)
#memory size of array
print(a.nbytes,"\n")

#null vector of size 10 but 5th element is 1
b = np.empty(10)
b[5] = 1
print(b,"\n")

#create array with values ranging from 10-49
c = np.arange(10,50,6)
print(c,"\n")

#reverse 1d array
print(c[::-1])

#create a 3d array
mda = np.array([[[1],[0],[0]],[[1],[2],[3]],[[1],[2],[3]]])
print(mda,"\n",'\nArray Dimension:',mda.ndim)

#finding indices of non zero elements in matrix
mat = np.array([[0,2,1],[3.2,8,0],[0,6,5]])
print("\n",mat)
mask = mat!=0
print("\n",np.where(mask))

#create a 3*3 identity matrix
print(np.identity(3))

#create a 3d matrix with random values and find the min and max

random3D = np.array([[[rd.randint(0,10)],[rd.randint(0,10)]],[[rd.randint(0,10)],[rd.randint(0,10)]],[[rd.randint(0,10)],[rd.randint(0,10)]],[[rd.randint(0,10)],[rd.randint(0,10)]]])
print(random3D)
print('Max value:',random3D.max(),'\nMin value:',random3D.min())
print('Mean:',random3D.mean(),'\nStandard Deviation:',random3D.std())

#CHECKERBOARD
checkerboard = np.array([np.zeros(900,dtype = int)]).reshape(30,30)
checkerboard[0:30:2,0:30:2] = 1
checkerboard[1:30:2,1:30:2] = 1
print(checkerboard)
checkerboard[1]*=-1
print('\n',checkerboard)

#Find the intersection of two 1d arrays
arrA = np.array([1,2,0,6,1,3])
arrB = np.array([3,2,6,4,9,8,2])
print(arrA,'\n',arrB,'\nIntersection of A & B is:',np.intersect1d(arrA,arrB))

#replace elements greater than 2 in arrA by -1
mask = arrA >=2
print(np.where(mask,-1,arrA))

#initialize two 2*8 arrays and stakc the horizontally and verticall to create a 2*16 and 4*8 arrays respectively
c = np.array(np.random.randint(10,size=(2,8)))
d = np.array(np.random.randint(10,size=(2,8)))
print('\nArray 1:\n',c,'\n\nArray 2:\n',d)
h = np.concatenate((c,d),-1)
v = np.concatenate((c,d),-2)
print('\nHorizontal Stack:\n',h,'\nVertical Stack:\n',v)

a = np.array(np.random.randint(10,size=(3,3)))
#swap rows and columns
print("\n",a)
temp = a[0].copy()
a[0] = a[1]
a[1] = temp
print("Row swap\n",a)
temp = a[:,1].copy()
a[:,1] = a[:,2]
a[:,2] = temp
print("Column swap:\n",a)

#reverse row and column elements
a[2] = a[2,::-1]
print("Row reversed\n",a)
a[:,1] = a[::-1,1]
print("Column reversed\n",a)



