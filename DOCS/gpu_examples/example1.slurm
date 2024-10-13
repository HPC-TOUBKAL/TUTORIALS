#!/bin/bash                                                                           

#SBATCH --partition=gpu          # partition name   
#SBATCH --job-name=cupy          # name of the job
#SBATCH --nodes=1                # number of nodes
#SBATCH --gres=gpu:1
#SBATCH --account=<GPU-ACCOUNT>
#SBATCH --time=00:05:00          # maximum execution time requested (HH:MM:SS)
#SBATCH --output=cupy%j.out       # name of output file
#SBATCH --error=cupy%j.out        # name of error file (here, in common with output)                          

# cleans out the modules loaded in interactive and inherited by default
module purge

# load modules
module load slurm Python/3.8.2-GCCcore-9.3.0 CUDA/11.1.1

python3 Cupy_example.py
