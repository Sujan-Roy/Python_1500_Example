# Write a NumPy program to create an array of 10 zeros, 10 ones, and 10 tens.

import numpy as np

a= np.array([[1,2,3,4,5],[4,7,8,9,10]])
b= np.array([4,6,7,8],ndmin=2)
c= np.array([4,6,7,8],dtype=complex)
# Change the shape of array
a.shape=(5,2)
# Resize the array
d= b.reshape(2,2)
print(a)
print(b)
print(c)
print(d)
e=np.zeros(10,dtype=int)

f=np.ones(10,dtype=int)

g= np.ones(10)*10
print("An array with 10 zeros:")
print(e)
print("An array with 10 Ones:")
print(f)
print("An array with 10 tens:")
print(g)