# Exercises for Simlab cluster

## Exercise 1: Basic Job Submission

 - Create a simple Slurm script to run a basic job. Include information such as the job name, requested resources (nodes=1 (node03), tasks=1), and run `ex1.py`. 
 - Submit the job using the sbatch command.
 - Add this script to your batch file

```shell
# Run the python script
python -c "  
import os
import socket

print('Hello from ex1.py!')
# Check the allocated resources
nodes = int(os.environ.get('SLURM_JOB_NUM_NODES', 1))
tasks_per_node = int(os.environ.get('SLURM_CPUS_PER_TASK', 1))
hostname = socket.gethostname()

assert nodes==1
assert tasks_per_node==1
assert hostname=='node03'
print('Resource allocation checks passed.')
"
```
- Output:
```shell
Hello from ex1.py!
Resource allocation checks passed.
```

## Exercise 2: 

- Create a Slurm script (`slurm_script_gpu.sh`) to submit a job that requires GPU resources. Include information such as the job name, requested resources (tasks=10, GPUs=2), and run `ex2.py`.
- Run the python file `ex2.py`

- Output:
```shell
Hello from ex2.py!
Resource allocation checks passed.
```

### Exercise 3:
- Run the batch file below:
```shell
#!/bin/bash

#SBATCH --job-name=my_job
#SBATCH --partition=shortq
#SBATCH --ntasks=1
#SBATCH --time=00:10:00

python3 ex3.py
```
1. Was the job completed successfully? 
2. If not, what type of problem(s) did you encounter?

3. If the job was not completed successfully, fix the problem by requesting more resources as needed (CPU and/or memory). Then submit your script to the cluster again.
		- how many resources (CPU and memory) did you request to run your job successfully?

4. Inspect the resource usage of the job you just completed with the following command. Verify whether you are using all the CPU and memory that you requested:  
    `sacct -j <jobid> --format=jobid,jobname%15,partition,account%30,alloctres%40,cputime,totalcpu,maxrss,submit,state%15,exitcode,elapsed`
    
5. Are the resources requested for your job adequate, or is it possible to make them fit better to the actual requirements of the job?  
		- If needed, adapt the resource requirements of your job and run it again.

### Exercise 4:
- Install numba using `pip install numba`
- Run the code `ex4.py` to observe the performance comparison for different matrix sizes.
- Analyze the results and observe how the execution times change with the matrix size.
- Connect to the node requested and analyze the gpu usage using the command `nvitop`

```shell
nvitop
Thu Dec 14 00:34:36 2023
╒═════════════════════════════════════════════════════════════════════════════╕
│ NVIDIA-SMI 515.65.01    Driver Version: 515.65.01    CUDA Version: 11.7     │
├───────────────────────────────┬──────────────────────┬──────────────────────┤
│ GPU  Name        Persistence-M│ Bus-Id        Disp.A │ Volatile Uncorr. ECC │
│ Fan  Temp  Perf  Pwr:Usage/Cap│         Memory-Usage │ GPU-Util  Compute M. │
╞═══════════════════════════════╪══════════════════════╪══════════════════════╪════════════════════╕
│   0  Tesla V100-PCIE...  On   │ 00000000:3B:00.0 Off │                    0 │ MEM: ▍ 4.4%        │
│ MAX   32C    P0    41W / 250W │    724MiB / 16384MiB │      0%      Default │ UTL: ▏ 0%          │
╘═══════════════════════════════╧══════════════════════╧══════════════════════╧════════════════════╛
[ CPU: ██ 3.9%                                                ]  ( Load Average:  0.68  0.45  0.27 )
[ MEM: █▍ 2.7%                                                ]  [ SWP: █▊ 7.9%                    ]

╒══════════════════════════════════════════════════════════════════════════════════════════════════╕
│ Processes:                                                                       ikissami@node16 │
│ GPU     PID      USER  GPU-MEM %SM  %CPU  %MEM  TIME  COMMAND                                    │
╞══════════════════════════════════════════════════════════════════════════════════════════════════╡
│   0  205220 C ikissa+   497MiB   0   0.0   0.3  0:42  python3 ex4.py                             │
╘══════════════════════════════════════════════════════════════════════════════════════════════════╛
```

### Exercise 5:
- Run Jupyter Notebook on simlab
- Run the cells of `pandas-timeseries.ipynb`

