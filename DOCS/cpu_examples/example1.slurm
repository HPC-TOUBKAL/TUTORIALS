#!/bin/bash                                                                           

#SBATCH --partition=compute      # partition name   
#SBATCH --job-name=mpi           # name of the job
#SBATCH --nodes=2                # number of nodes
#SBATCH --ntasks-per-node=4      # number of MPI processes per node

#SBATCH --time=00:01:00          # maximum execution time requested (HH:MM:SS)
#SBATCH --output=mpi-%j.out      # name of output file
#SBATCH --error=mpi-%j.out       # name of error file (here, in common with output)                          

# cleans out the modules loaded in interactive and inherited by default
module purge

# load modules
module load slurm Python/3.8.2-GCCcore-9.3.0 OpenMPI/4.0.3-GCC-9.3.0

module list

mpirun python3 hello_mpi.py 
