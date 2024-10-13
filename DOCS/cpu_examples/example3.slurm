#!/bin/bash                                                                           

#SBATCH --partition=compute      # partition name   
#SBATCH --job-name=R             # name of the job
#SBATCH --nodes=1                # number of nodes
#SBATCH --time=00:01:00          # maximum execution time requested (HH:MM:SS)
#SBATCH --output=R-%j.out        # name of output file
#SBATCH --error=R-%j.out         # name of error file (here, in common with output)                          

# cleans out the modules loaded in interactive and inherited by default
module purge

# load modules
module load Anaconda3
source /srv/software/easybuild/software/Anaconda3/2020.11/etc/profile.d/conda.sh
conda activate r_env

Rscript r_example.R
