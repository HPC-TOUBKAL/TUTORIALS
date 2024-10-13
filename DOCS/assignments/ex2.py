import torch
import os

print('Hello from ex2.py!')

# Check if GPU is available
cuda_available = torch.cuda.is_available()
nodes = int(os.environ.get("SLURM_JOB_NUM_NODES", 1))
ntasks = int(os.environ.get("SLURM_NPROCS", 1))


assert cuda_available, 'GPU not available!'
assert nodes==2
assert ntasks==10


print('Resource allocation checks passed.')
