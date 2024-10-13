import cupy as cp

arr_g1= cp.random.rand(10000,10000)
arr_g2= cp.random.rand(10000,10000)
r1 = arr_g1 * arr_g2
