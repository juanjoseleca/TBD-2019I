from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

print("Hi im saying hello from node ", rank)
a=0
b=0
while 1:
    a+=1
    b+=1 
comm.Barrier()