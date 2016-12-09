#!coding: utf-8
# Python&HDF5 的多进程编程demo，程序用一个仅一条语句的函数计算距离，一个拥有4个工作进程的进程池来处理1000次运算
#Author: Jiahui Tang
#Time: 2016-12-07

#import the necessary packages
import numpy as np
from multiprocessing import Pool
import h5py

def distance(arr):
	#compute distance from origin to the point
	return np.sqrt(np.sum(arr ** 2))

#load data and close the input file
with h5py.File('coords.hdf5', 'r') as f:
	data = f['coords'][...]

#create a 4-process pool
p = Pool(4)

#carry out parallel computation
result = np.array(p.map(distance, data))

#write the result into a new dataset in the file
with h5py.File('coords.hdf5') as f:
	f['distances'] = result
