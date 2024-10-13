import os
import socket

print("Hello from ex1.py!")

# Check the allocated resources
nodes = int(os.environ.get("SLURM_JOB_NUM_NODES", 1))
tasks_per_node = int(os.environ.get("SLURM_CPUS_PER_TASK", 1))
hostname = socket.gethostname()

assert nodes==1
assert tasks_per_node==1
assert hostname=="node03"
