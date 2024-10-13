#!/bin/bash

# If your job will need to use the gpu ressource, add this two lines
#SBATCH -p gpu                             # partition name
#SBATCH --export=NONE
#SBATCH --gres=gpu:1                       # Necessary to activate the gpu card (The number of GPUs allowed by node is 1)
#SBATCH --nodes=1
#SBATCH -n 1                               # number of cores ( max 44 per node)
#SBATCH --account=<GPU-ACCOUNT>
#SBATCH --time=01:00:00                      # wall time to finish the job
#SBATCH --job-name=jupyter-lab             # job name
#SBATCH --output=jupyterlab-%j.log         # output file

# get tunneling info
XDG_RUNTIME_DIR=""
node=$(hostname -s)
user=$(whoami)
cluster="toubkal.hpc"
port=$(( 9889 ))


# print tunneling instructions jupyter-log
echo -e "
Command to create ssh tunnel:
ssh -N -f -L ${port}:${node}:${port} ${user}@${cluster}.um6p.ma
"

# load modules or conda environments here (you can use your own conda environment)
module purge 
module load Anaconda3 CUDA/11.1.1

# Run Jupyter lab
jupyter-lab --no-browser --port=${port} --ip=${node}
