# NumPy Practice Questions (Including Random
# Module)

#--------------------------- 🟢Section A — Array Creation & Basics--------------------------

# Q1. Create a One-Dimensional Array

import numpy as np
arr=np.array([1,2,3,4])
print(arr)



# Create a NumPy array containing values from 1 to 10.
# Then:

arr=np.arange(1,11)
print(arr.shape)

# 1. Print the shape
arr=np.arange(1,11)
print(arr.shape)
# 2. Print the size
arr=np.arange(1,11)
print(arr.size)
# 3. Print the number of dimensions
print(arr.ndim)


#-----------------------------------Q2. Create Arrays Using NumPy Functions--------------------------------

# Create:
# 1. A 3×3 matrix of zeros

matrix=np.zeros((3,3))
print(matrix)


# 2. A 2×4 matrix of ones

matrix=np.ones((2,4))
print(matrix)
# 3. A 4×4 identity matrix

matrix=np.eye((4))
print(matrix)

#------------------------------Q3. arange() vs linspace()-----------------------------------------

# 1. Create an array from 0 to 20 with step size 2 using arange()

arr=np.arange(0,20,2)
print(arr)

# 2. Create 5 equally spaced values between 0 and 20 using linspace()

arr=np.linspace(0,20,5)
print(arr)

# 3. Explain the difference between both outputs

# 1. arange():--arange ka use tab hota hai jab hame Step Size (Interval) control karna ho,
# aur ye end value ko exclude karta hai.


#2. linespace():--- linspace ka use tab hota hai jab hame Total Number of Elements control karne hon,
# aur ye end value ko include karta hai


# -------------------------------Q4. Data Types-----------------------------------------------
# Create:

# [1,2,3,4]

# Then:
# 1. Check datatype

arr=np.array([1,2,3,4])
print(type(arr))

# 2. Convert datatype to float
arr=np.array([1,2,3,4],dtype='float' )

print(arr)

#---------------------------------🟡Section B — Indexing & Slicing---------------------------------------

# Q5. Basic Indexing
# Given:

arr = np.array([10,20,30,40,50])

# Perform:
# 1. Print first element

print(arr[0])

# 2. Print last element

print(arr[-1])


# 3. Print middle element
print(arr[2])


# 4. Reverse the array

print(arr[::-1])


#----------------------------------------Q6. Basic Slicing-------------------------------
# Using the same array:

arr = np.array([10,20,30,40,50])

# 1. Extract first 3 elements

print(arr[:3])

# 2. Extract last 2 elements

print(arr[-2:])

# 3. Extract elements from index 1 to 4

print(arr[1:4])

# 4. Extract every second element

print(arr[0::2])


#---------------------------------------------Q7. Matrix Indexing-----------------------------
# Given:

arr = np.array([
[1,2,3],
[4,5,6],

[7,8,9]
])

# Perform:
# 1. Print element 5

print(arr[1,1])

# 2. Print second 

print(arr[1])

# 3. Print third column

print(arr[:,2])

# 4. Print last row using negative indexing

print(arr[-1])


#-----------------------------------Q8. Matrix Slicing-------------------------------
# Using the same matrix:
arr = np.array([
[1,2,3],
[4,5,6],

[7,8,9]
])

# 1. Extract:

# [[1,2],
# [4,5]]


print(arr[0:2,0:2])

# 2. Extract:

# [[5,6],
# [8,9]]

print(arr[1:,1:])

# 3. Extract corner elements [1,3,7,9]

print(arr[::2,::2])


#---------------------------------------Q9. Reverse Rows & Columns-----------------------------

# Using:

[[1,2,3],
[4,5,6],
[7,8,9]]

# 1. Reverse rows
print(arr[::-1,])

# 2. Reverse columns
print(arr[:,::-1])

# 3. Reverse both rows and columns
print(arr[::-1,::-1])


#----------------------------🔵Section C — Boolean Indexing--------------------------------------

# Q10. Filtering Values
# Given:

arr = np.array([5,10,15,20,25,30])

# 1. Extract values greater than 15
out=arr[arr>15]
print(out)

# 2. Extract even numbers

out=arr[arr%2==0]
print(out)

# 3. Replace values greater than 20 with 0
arr[arr>20]=0
print(arr)


#-------------------------------------Q11. Boolean Indexing in Matrix--------------------------
# Given:

arr = np.array([
[10,20,30],
[40,50,60]
])

# 1. Extract values greater than 25
out=arr[arr>25]

print(out)

# 2. Replace values greater than 25 with -1

arr[arr>25]=-1
print(arr)

#-------------------------Q12. Scalar Broadcasting------------------------------------------
# Add 10 to:

arr=np.array([1,2,3,4])

result=arr+10
print(result)


#--------------------------------Q13. Row-wise Broadcasting-------------------------------

# Given:

A = np.array([
[10,20,30],
[40,50,60]
])
B = np.array([1,2,3])

# Add B to A .

result=A+B
print(result)

#-----------------------------------Q14. Column-wise Broadcasting--------------------------
# Given:

A = np.array([
[10,20,30],
[40,50,60]
])
B = np.array([
[1],
[2]
])

# Add B to A .

result=A+B
print(result)

#---------------------------Check whether these operations are valid:----------------------
# 1.

(2,3) + (3,)

a1=np.array([2,3])
a2=np.array([3,])
print(a1+a2)
#Kyuki Piche wala dimension 3 aur 3 match kar gaya. NumPy isse row-wise stretch karke add kar dega

2.

(3,2) + (2,)

a1=np.array([3,2])
a2=np.array([2,])
print(a1+a2)
#Kyunki Piche wala dimension 2 aur 2 match kar gaya. Ye bhi row-wise add ho jayega.

3.

(2,3) + (2,)

a1=np.array([2,3])
a2=np.array([2,])
print(a1+a2)

#Kyuki Piche wala dimension 3 aur 2 match nahi karta. Isliye ValueError aayega

# Explain why.
# NumPy hamesha dimensions ko piche se (Right-to-Left) compare karta hai. 
# Do dimensions tabhi compatible hote hain jab:Wo dono Barabar (Equal) hon.
# Ya phir unme se ek 1 ho.


# -------------------------🟠Section E — Aggregation & Axis------------------------------

# Q16. Sum Operations
# Given:

arr = np.array([
[1,2,3],
[4,5,6]
])

# Find:
# 1. Total sum
total = np.sum(arr)
print(total)

# 2. Row-wise sum

row_sum = np.sum(arr, axis=1)
print(row_sum)

# 3. Column-wise sum

col_sum = np.sum(arr, axis=0)
print(col_sum)

#--------------Q17. Statistical Operations

# Using the same matrix:
arr = np.array([[1, 2, 3], [4, 5, 6]])

# 1. Mean of each row

row_mean = np.mean(arr, axis=1)
print(row_mean)

# 2. Mean of each column

col_mean = np.mean(arr, axis=0)
print(col_mean)

# 3. Maximum value in each row
row_max = np.max(arr, axis=1)
print(row_max)

# 4. Minimum value in each column
col_min = np.min(arr, axis=0)
print(col_min)


#-----------------------------Q18. Standard Deviation---------------

# Find standard deviation of:

# arr=np.array=([10,20,30,40,50])
# std_devi=np.std(arr)
# print(std_devi)

#-----------------------🔴Section F — Reshape & Flatten------------------

# Q19. Reshaping
# Create:

# # arr = np.array([1, 2, 3, 4, 5, 6])

# # Then:
# # 1. Convert into 2×3 matrix

# matrix= arr.reshape(2, 3)
# print(matrix)

# # 2. Convert into 3×2 matrix
# matrix = arr.reshape(3, 2)
# print(matrix)

# # 3. Convert into column vector

# column_vector = arr.reshape(6, 1)
# print(column_vector)

#-----------------------Q20. Flattening------------------
# Given:

arr = np.array([[1, 2, 3], [4, 5, 6]])

# # 1. Flatten using flatten()

flat = arr.flatten()
print("Flatten:", flat)
# 2. Flatten using ravel()
rav = arr.ravel()
print("Ravel:", rav)

# 3. Explain difference

# flatten() data ki nayi copy banata hai, jabki 
# ravel() original array ka sirf ek view (reference) dikhata hai.

# ravel() se bane array ko change karege,
# toh original array bhi badal jayega.
# flatten() mein original array safe rehta hai.


#-------------------------------⚫Section G — Copy vs View------------------

# Q21. Observe Memory Sharing
# Run:

a = np.array([1,2,3])
b = a

b[0] = 100

print("Array a:", a)
print("Array b:", b)

#1. Print a
# 2. Explain why it changed

# b = a karne se koi naya array nahi banta,
# dono variables memory mein ek hi address share karte hain 
# (Reference assignment).
# Isliye b mein change karne par original array 
# a bhi badal jata hai kyunki dono ka data source same hai.


#Q22. Create Independent Copy

# Modify previous code so changing b does not affect a .
a = np.array([1,2,3])
b = a
b=a.copy()
b[0] = 100

print("Array a:", a)
print("Array b:", b)

#-------------------🟤Section H — Normalization

# Q23. Min-Max Normalization

# Normalize:

# [10,20,30,40,50]

# between 0 and 1.
import numpy as np

data = np.array([10, 20, 30, 40, 50])
normalized = (data - data.min()) / (data.max() - data.min())

print(normalized)


#----------------------------Q24. Matrix Normalization

# Normalize:

# [[1,2],
# [3,4]]

import numpy as np

matrix = np.array([[1, 2], [3, 4]])


norm_matrix = (matrix - matrix.min()) / (matrix.max() - matrix.min())

print(norm_matrix)


#-----------------------------Q25. Column-wise Normalization

# Normalize each column independently:

# [
# [10,100],
# [20,200],
# [30,300]
# ]

matrix = np.array([[10, 100], [20, 200], [30, 300]])

col_min = matrix.min(axis=0)
col_max = matrix.max(axis=0)

norm_matrix = (matrix - col_min) / (col_max - col_min)

print(norm_matrix)

#-----------------------🟠Section I — Random Module (NEW)

# Q26. Generate Random Float Values

# Generate:
# 1. A single random float between 0 and 1

single_val = np.random.random() 
print(single_val)

# 2. An array of 5 random float values
float_val = np.random.random(5) 
print(float_val)


#---------------------------------Q27. Random Integer Array
# Generate:
# 1. 5 random integers between 1 and 10

arr=np.random.randint(1,10,size=5)
print(arr)
# 2. A 3×3 matrix of random integers between 50 and 100
arr=np.random.randint(50,100,size=(3,3))
print(arr)

#---------------------------Q28. Random Choice

# Given:

arr =np.array( [10,20,30,40,50])

# Randomly select:
# 1. One value
single_val = np.random.choice(arr)
print(single_val)

# 2. Three values
three_vals = np.random.choice(arr, size=3)
print(three_vals)

#-------------------------------------Q29. Random Normal Distribution

# Generate:
# 1. 5 random values from normal distribution

arr=np.random.randn(5)
print(arr)
# 2. A 2×3 matrix using randn()
arr=np.random.randn(2,3)
print(arr)

#---------------------------------Q30. Set Random Seed

# Generate random integers between 1 and 100 using:
arr = np.random.randint(1, 101, size=5)
print(arr)

# np.random.seed()


# Run the code multiple times and observe the output.
np.random.seed(42)
print(np.random.randint(1,7,3))

# 
# Explain why the same values are generated.
#Jab hum seed(42) likhte hain, 
# toh hum formula ko ek fixed starting point de dete hain.

#---------------------------Q32. Permutation

# Using:

arr = np.array([1,2,3,4,5])

# 1. Generate a permutation of the array
permuted_arr=np.random.permutation(arr)
print(permuted_arr)


# 2. Compare permutation with shuffle

permuted_arr=np.random.permutation(arr)
np.random.shuffle(arr)
print(arr)


#------------------------------------------------Q33. Random Matrix Statistics

# Generate a 4×4 matrix of random integers between 1 and 50.
# Then:
# 1. Find maximum value
matrix = np.random.randint(1, 51, size=(4, 4))
print( matrix)
print(matrix.max())
# 2. Find minimum value

print( matrix.min())
# 3. Find row-wise sum
print( matrix.sum(axis=1))

# 4. Find column-wise mean
print( matrix.mean(axis=0))

#-----------------------------------Q34. Random Filtering
# Generate 10 random integers between 1 and 100.
# Then:
# 1. Extract even numbers

matrix=np.random.randint(1,101,size=10)
arr=matrix[matrix%2==0]
print(arr)

# 2. Extract values greater than 50

print(matrix[matrix>50])
greater_than_50 = arr[arr > 50]
print("Values > 50:", greater_than_50)
# 3. Replace values less than 30 with 0
matrix[matrix<30]=0
print(matrix)

#--------------------------Q35. Random Normalization Challenge
# Generate a random array of size 8.
arr = np.random.randint(1, 100, size=8)
print("Original Array:", arr)

# Normalize all values between 0 and 1.
arr_min = arr.min()
arr_max = arr.max()

normalized_arr = (arr - arr_min) / (arr_max - arr_min)

print("Normalized Array:", normalized_arr)


#---------------------------------------------------------🚀Bonus Challenges-----------------------------------

# Q36.

# Create a 5×5 matrix with values from 1 to 25.

matrix = np.arange(1, 26).reshape(5, 5)
print("Original Matrix:\n", matrix)

# Then:
# 1. Print diagonal elements
diag_elements = np.diag(matrix)
print( diag_elements)
# 2. Replace diagonal elements with 0

matrix[np.diag_indices(5)] = 0

print( matrix)

# Q35.

# Create:

# [[1,1,1],
# [2,2,2],
# [3,3,3]]

# without manually typing rows.
# 1. Pehle np.tile se 1,2,3 ko 3 baar repeat karke matrix banayi
temp = np.tile([1, 2, 3], (3, 1)) 

# 2. Phir .T (Transpose) karke rows ko columns bana diya
matrix = temp.T

print(matrix)


# Q36.

# Generate a random matrix and:
matrix = np.random.randint(1, 11, size=(3, 3))
print(matrix)

# 1. Reverse rows
print(matrix[::-1,:])

# 2. Reverse columns
print(matrix[:,::-1])
# 3. Flatten the matrix
print(matrix.flatten())

# Q37.

# Generate a random 3×3 matrix and extract:
matrix=np.random.randint(1,11,size=(3,3))
print(matrix)


# 1. First row
print(matrix[0,:])
# 2. Last column
print(matrix[:,-1])
# 3. Center element
print(matrix[1,1])
# 4. Corner elements
print(matrix[::2,::2])
