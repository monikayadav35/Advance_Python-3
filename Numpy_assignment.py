#--------------------------🟢Section A: Basics & Indexing---------------------------------

#-------------------------------- Q1. One-Dimensional Array-------------------------------


# Create an array [10, 20, 30, 40, 50]

import numpy as np
arr=([10,20,30,40,50])


# Perform:
# 1. Print first element

print(arr[0])

# 2. Print last element
print(arr[-1])


# 3. Print elements from index 1 to 3

print(arr[1:3])
# 4. Reverse the array

print(arr[::-1])

#--------------------------------------------- Q2. Matrix Basics--------------------------------

# Create a 2×3 matrix using np.arange(1,7)

matrix=np.arange(1,7)
print(matrix)
matrix=matrix.reshape(2,3)
print(matrix)




# 1. Print shape

print(matrix.shape)
# 2. Print second row

print(matrix[1])

# 3. Print first column
print(matrix[0])

# -----------------------------🟡Section B: Slicing (VERY IMPORTANT)-----------------------------------

# ---------------------------------Q3. Basic 1D Slicing-------------------------------
# Given:

import numpy as np

arr = np.array([1,2,3,4,5,6])

# Perform:

# 1. Extract elements from index 1 to 4


print(arr[1:4])


# 2. Extract first 3 elements

print(arr[:3])

# 3. Extract last 3 elements

print(arr[-3:])


# 4. Reverse the array using slicing

print(arr[::-1])


# Q4.--------------------------- Step Slicing-----------------------------------------------

# Using the same array:
arr = np.array([1,2,3,4,5,6])

# 1. Extract every 2nd element

print(arr[::2])
# 2. Extract elements in reverse order with step

print(arr[::-2])

# 3. Extract elements starting from index 1 with step 2

print(arr[1::2])

# Q5. 2D Slicing (Sub-matrix)
# Given:


arr = np.array([
[10,20,30],
[40,50,60],
[70,80,90]
])

# Extract:
# 1. First two rows and first two columns

print(arr[0:2,0:2])

# 2. Last two rows and last two columns

print(arr[1:3,1:3])
# 3. Entire second row

print(arr[1])


# 4. Entire third column

print(arr[:,2])

#--------------------------- Q6. Advanced 2D Slicing-----------------------------
# From the same matrix:

arr = np.array([
[10,20,30],
[40,50,60],
[70,80,90]
])


# 1. Extract:

# [[20,30],
# [50,60]]

print(arr[0:2,1:3])

# 2. Extract:

# [[10,30],
# [70,90]]


print(arr[::2,::2])


# 3. Reverse:
# rows

print(arr[::-1,:])

# columns

print(arr[:,::-1])

# Q7. Negative Indexing + Slicing
# Using:

arr = np.array([10,20,30,40,50])

# Perform:
# 1. Extract last 2 elements

print(arr[-2:])
# 2. Extract all elements except last one

print(arr[:-1])

# 3. Reverse using negative slicing

print(arr[::-1])

# ---------------------------------🔵Section C: Boolean Indexing

# Q8

# Given:

arr = np.array([10,20,30,40,50])

# 1. Extract values greater than 25

arr1=arr[arr>25]
print(arr1)

# 2. Replace values greater than 25 with 0


arr[arr>25]=0
print(arr)


# ---------------------------------------------🟣Section D: Broadcasting

# Q9

# Add [1,2,3] to:

# [[10,20,30],
# [40,50,60]]


arr=np.array([1,2,3])
arr2=np.array([[10, 20, 30], [40, 50, 60]])

print(arr+arr2)


# Q10

# Add column vector:

# [[1],
# [2]]

# to:

# [[10,20,30],
# [40,50,60]]


arr = np.array([[10, 20, 30], [40, 50, 60]])
col_vac = np.array([[1], [2]])

print(arr+col_vac)

# ----------------------------------------🟠Section E: Axis & Aggregation

# Q11

# Given:

# [[1,2,3],
# [4,5,6]]

# 1. Find total sum


arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr.sum())

# 2. Column-wise Sum 
print(arr.sum(axis=0))

# 3. Row-wise Sum 
print(arr.sum(axis=1))



# Q12

# Find:

# 1. Mean of each row

print(arr.mean(axis=1)) 

# 2. Maximum of each column

print(arr.max(axis=0))
