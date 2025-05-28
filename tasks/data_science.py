# Each cell in Jupyter is like a separate script
import numpy as np

# Create a 2-D array, set every second element in
# some rows and find max per row:

x = np.arange(15, dtype=np.int64).reshape(3, 5)
x[1:, ::2] = -99
x

x.max(axis=1)
# array([ 4,  8, 13])

# Generate normally distributed random numbers:
rng = np.random.default_rng()

samples = rng.normal(size=250000)
samples

# Create arrays
array_1 = np.array([1, 2, 3])
array_2 = np.array([4, 5, 6])

# Perform element-wise operations
dot_product = np.dot(array_1, array_2)  # Dot product
elementwise_sum = array_1 + array_2  # Element-wise addition
squared = np.square(array_1)  # Element-wise squaring

print(dot_product, elementwise_sum, squared)
