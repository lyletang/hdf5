#!coding: utf-8
# Python&HDF5 的多进程编程demo，基于MPI的距离计算，通过进程的rank隐式分派，而不是之前的多进程例子中那样通过map（）显式分派
#Author: Jiahui Tang
#Time: 2016-12-07

#import the necessary packages
import numpy as np
import h5py
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.rank

f = h5py.File('coords.hdf5', driver = 'mpio', comm = comm)

coords_dset = f['coords']
distances_dset = f.create_dataset('distances', (1000,), dtype = 'f4')

idx = rank * 250

#load process-specific data
coords = coords_dset[idx : idx + 250]

#compute distances
result = np.sqrt(np.sum(coords ** 2, axis = 1))

#write process-specific data
distances_dset[idx : idx + 250] = result

f.close()
