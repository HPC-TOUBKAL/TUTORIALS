#!/bin/bash

# If your job will need to use the gpu ressource, add this two lines
#SBATCH -p gpu                             # partition name
#SBATCH --gres=gpu:1                       # Necessary to activate the gpu card (The number of GPUs allowed by node is 1)
#SBATCH --nodes=1
#SBATCH --account=<GPU-ACCOUNT>
#SBATCH --time=00:10:00                      # wall time to finish the job
#SBATCH --job-name=kerasgpu                # job name
#SBATCH --output=kerasgpu-%j.log           # output file

# Unload all modules
module purge

# load modules or conda environments here (you can use your own conda environment)
 module load Anaconda3 CUDA/11.1.1
source $ANACONDA_HOME/etc/profile.d/conda.sh
conda activate tensorflow-gpu

python3 keras_example.py
