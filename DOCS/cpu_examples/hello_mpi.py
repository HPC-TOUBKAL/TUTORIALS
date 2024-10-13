from mpi4py import MPI

COMM = MPI.COMM_WORLD
np = COMM.Get_size()
id = COMM.Get_rank()

print("I am process", id, "of", np);
