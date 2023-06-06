# Write a NumPy program to find missing data in a given array.

import numpy as np

array= np.array([[4,6,np.nan],
                [7,np.nan,8],
                [34,np.nan,np.nan]])

print("Original Array=\n",array)

print("Show the missing data in the array")
print(np.isnan(array))

array2= np.array([[2+3j,5,7],
                  [15j+2,6,8]])
print("Original Array 2=",array2)
print("Complex array=")
print (array2[np.iscomplex(array2)])