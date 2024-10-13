import numpy as np
from numba import cuda, njit
import timeit

@njit
def matrix_multiply_cpu(A, B):
    m, n = A.shape
    p = B.shape[1]
    C = np.zeros((m, p), dtype=A.dtype)

    for i in range(m):
        for j in range(p):
            tmp = 0.0
            for k in range(n):
                tmp += A[i, k] * B[k, j]
            C[i, j] = tmp

    return C

# Define the matrix multiplication kernel
@cuda.jit
def matrix_multiply_kernel(A, B, C):
    i, j = cuda.grid(2)
    
    if i < C.shape[0] and j < C.shape[1]:
        tmp = 0.0
        for k in range(A.shape[1]):
            tmp += A[i, k] * B[k, j]
        C[i, j] = tmp

# Host (CPU) code
def matrix_multiply(A, B):
    # Transfer data to GPU
    A_gpu = cuda.to_device(A)
    B_gpu = cuda.to_device(B)
    
    # Allocate memory for the result on GPU
    C_gpu = cuda.device_array((A.shape[0], B.shape[1]))

    # Configure and launch the CUDA kernel
    threads_per_block = (32, 32)
    blocks_per_grid_x = (A.shape[0] + threads_per_block[0] - 1) // threads_per_block[0]
    blocks_per_grid_y = (B.shape[1] + threads_per_block[1] - 1) // threads_per_block[1]
    blocks_per_grid = (blocks_per_grid_x, blocks_per_grid_y)

    matrix_multiply_kernel[blocks_per_grid, threads_per_block](A_gpu, B_gpu, C_gpu)

    # Transfer the result back to the CPU
    C_cpu = C_gpu.copy_to_host()

    return C_cpu

def compare_matrix_multiplication(matrix_size):
    # Generate random matrices
    A = np.random.rand(matrix_size, matrix_size)
    B = np.random.rand(matrix_size, matrix_size)

    # Measure GPU execution time
    ts_gpu = timeit.default_timer()
    C_gpu = matrix_multiply(A, B)
    te_gpu = timeit.default_timer()

    # Measure CPU execution time
    ts_cpu = timeit.default_timer()
    C_cpu = matrix_multiply_cpu(A, B)
    te_cpu = timeit.default_timer()

    print(f"Matrix Size: {matrix_size}x{matrix_size}")
    print(f"Wall time with GPU: {te_gpu - ts_gpu:.5f} seconds")
    print(f"Wall time with CPU: {te_cpu - ts_cpu:.5f} seconds")

# Example usage
matrix_sizes = [500, 1000, 2000, 5000]
for size in matrix_sizes:
    compare_matrix_multiplication(size)
    print("\n")
