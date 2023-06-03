#  Write a NumPy program to create an array of integers from 30 to 70.
#  Write a NumPy program to create an array of all even integers from 30 to 70.
import numpy as np

list=np.arange(30,71,dtype=float)
print(list)

list2= np.arange(30,71,2)
print(list2)

# Linspace function used for number of evenly spaced values between the interval
x= np.linspace(10,20,2,retstep=False)
print(x)