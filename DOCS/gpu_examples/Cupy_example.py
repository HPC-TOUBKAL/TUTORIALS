import cupy as cp
import numpy as np
import time

# Create a large array with NumPy
numpy_array = np.random.rand(10000000)

# Time the sum operation with NumPy
start_time = time.time()
numpy_sum = np.sum(numpy_array)
numpy_time = time.time() - start_time

print(f'NumPy Sum: {numpy_sum}, Time: {numpy_time} seconds')




# Convert the NumPy array to a CuPy array
cupy_array = cp.asarray(numpy_array)

# Time the sum operation with CuPy
start_time = time.time()
cupy_sum = cp.sum(cupy_array)
cupy_time = time.time() - start_time

print(f'CuPy Sum: {cupy_sum}, Time: {cupy_time} seconds')
