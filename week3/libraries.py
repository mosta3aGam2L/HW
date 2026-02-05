#Task for numpy library
import numpy as np

arr=np.array([[1,2,3],[4,5,6]])
'''print(arr.shape)
print(arr)
print(arr.dtype)'''

# 2-Random array
'''a=np.random.rand(2,2)
print(a)
print(a.min())
print(a.max())
print(a.std())
'''
#3-operations 
#print(arr.shape,{",number of elemnent =  "},arr.size)

#4-Mathematical Operations & ufuncs (3 Questions)
'''arr = np.array([1, 4, 9, 16, 25,36])
print(np.sqrt(arr))
a=np.random.rand(3,3)

print("Mean ",a.mean(),"sum =",a.sum())
print("Random 3x3 matrix:\n", a)

'''
#5-indexing and slicing
'''
arr = np.array([10, 20, 30, 40, 50, 60])
print(arr[:-1]) #all 
print(arr[0:4])

print(arr[arr < 25])  # output:[10 20]

arr[arr > 30]=0 #Modify the array so that all values less than 30 become 0.
print(arr)

print(arr < 30)#   output[True, True, False, False, False, False]
'''
#6- Random Numbers & Performance (3 Question

np.random.seed(42)
arr = np.random.randint(1, 101, size=15)
print( arr)

import time

py_arr = list(range(1, 11))

# loop
start_time = time.time()

py_result = []
for x in py_arr:
    py_result.append(x + 10)

end_time = time.time()
print("Python loop result:", py_result)
print("Python loop time:", end_time - start_time, "seconds")

##7- linear algebra
A = np.array([[2, 1, 3],
              [0, 1, 4],
              [5, 2, 1]])

# )   1-(determinant)
det_A = np.linalg.det(A)
print("Determinant of A:", det_A)

# 2- (inverse)
if det_A != 0:
    inv_A = np.linalg.inv(A)
    print("Inverse of A:\n", inv_A)
else:
    print("Matrix is singular, cannot compute inverse.")
