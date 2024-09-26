
import numpy as np # 1
print(np.__version__) #2. Imprime la versión de NUMPY y la configuración.

a = np.random.randint(4, size=(2, 3, 5)) #3. Generate a three-dimensional array of shape 2x3x5 with random values. Assign the array to the variable "a."

# Challenge: There are at least three easy ways to use NumPy to generate random arrays.
#  How many ways can you find?

a1 = np.random.rand(2, 3, 5)
a2 = np.random.random_integers(0, 3, size=(2, 3, 5)) 
a3 = np.random.randn(2, 3, 5) 

#4. Print a.

print(a)

#5. Create a three-dimensional array of shape 5x2x3 with all values equal to 1. Assign the array to the variable "b."

b = np.ones((5, 2, 3))

#6. Print b.

print(b)

#7. Do a and b have the same size? How do you demonstrate this in Python code?

equal_result = (a == b)
print(f"Equality Comparison Result:{equal_result}")

#8. Is it possible to add a and b? Why or why not?

ab = a + b
print(ab) # No, because theyre not the same shape. If yes, the elements would get added element wise.

#9. Transpose b to have the same structure as a (i.e., to become an array of shape 2x3x5). Assign the transposed array to the variable "c."

c1 = np.transpose(b)
c = np.transpose(c1)


#10. Try adding a and c. It should work now. Assign the sum to the variable "d." But why does it work now?

d = a + c

#11. Print a and d. Do you notice the difference and the relationship between the two arrays in terms of their values? Explain.

print(a)
print(d)
 # The second array consists of floating-point numbers (with a decimal point)
 
 
#12. Multiply a and c. Assign the result to e.

e = a * c
#13. Is e equal to a? Why or why not?

a == e # All true, they're equal

#14. Identify the maximum, minimum, and mean values in d. Assign those values to the variables "d_max," "d_min," and "d_mean."

d_max = np.max(d)
d_min = np.min(d)
d_mean = np.mean(d)

#15. Now we want to label the values in d. First, create an empty array "f" with the same shape (i.e., 2x3x5) as d using np.empty.

f = np.empty((2, 3, 5))

""" #16. Fill in the values in f. 
For each value in d, if it is greater than d_min but less than d_mean, assign 25 to the corresponding value in f.
 If a value in d is greater than d_mean but less than d_max, assign 75 to the corresponding value in f. 
 If a value is equal to d_mean, assign 50 to the corresponding value in f. 
 Assign 0 to the corresponding value(s) in f for d_min in d. 
 Assign 100 to the corresponding value(s) in f for d_max in d. 
 In the end, f should only have the following values: 0, 25, 50, 75, and 100. Note: You do not need to use NumPy for this question. """


f[(d > d_min) & (d < d_mean)] = 25
f[(d > d_mean) & (d < d_max)] = 75
f[d == d_mean] = 50
f[d == d_min] = 0
f[d == d_max] = 100



""" #17. Print d and f. Do you have the expected f? For example, if your d is:
array([[[1.85836099, 1.67064465, 1.62576044, 1.40243961, 1.88454931],
        [1.75354326, 1.69403643, 1.36729252, 1.61415071, 1.12104981],
        [1.72201435, 1.1862918 , 1.87078449, 1.7726778 , 1.88180042]],

       [[1.44747908, 1.31673383, 1.02000951, 1.52218947, 1.97066381],
        [1.79129243, 1.74983003, 1.96028037, 1.85166831, 1.65450881],
        [1.18068344, 1.9587381 , 1.00656599, 1.93402165, 1.73514584]]])

Your f should be: array([[[ 75., 75., 75., 25., 75.], [ 75., 75., 25., 25., 25.], [ 75., 25., 75., 75., 75.]],
array([[[ 75.,  75.,  75.,  25.,  75.],
        [ 75.,  75.,  25.,  25.,  25.],
        [ 75.,  25.,  75.,  75.,  75.]],

       [[ 25.,  25.,  25.,  25., 100.],
        [ 75.,  75.,  75.,  75.,  75.],
        [ 25.,  75.,   0.,  75.,  75.]]])
"""

print(d)
print(f)
"""
#18. Bonus question: instead of using numbers (i.e., 0, 25, 50, 75, and 100), how would you use string values ("A," "B," "C," "D," and "E") to label the elements of the array? You expect the result to be: array([[[ 'D', 'D', 'D', 'B', 'D'], [ 'D', 'D', 'B', 'B', 'B'], [ 'D', 'B', 'D', 'D', 'D']],
array([[[ 'D',  'D',  'D',  'B',  'D'],
        [ 'D',  'D',  'B',  'B',  'B'],
        [ 'D',  'B',  'D',  'D',  'D']],

       [[ 'B',  'B',  'B',  'B',  'E'],
        [ 'D',  'D',  'D',  'D',  'D'],
        [ 'B',  'D',   'A',  'D', 'D']]])
 Again, you do not need to use NumPy for this question. """


g = np.empty((2, 3, 5), dtype=object)

g[(d > d_min) & (d < d_mean)] = "A"
g[(d > d_mean) & (d < d_max)] = "B"
g[d == d_mean] = "C"
g[d == d_min] = "D"
g[d == d_max] = "E"

print(g)