#!coding: utf-8
# Python&HDF5 多线程编程demo 创建一个共享的HDF5文件，两个线程会进行一些计算并将结果写入文件。对文件的访问由一个threading.RLock类的实例管理
#Author: Jiahui Tang
#Time: 2016-12-07

#import the necessary packages
import threading
import time
import random
import numpy as np
import h5py

f = h5py.File("thread_demo.dhf5", "w")
dset = f.create_dataset("data", (2, 1024), dtyp = 'f')
lock = threading.RLock()

class ComputeThread(threading.Thread):
	
	def __init__(self, axis):
		self.axis = axis 0
		threading.Thread.__init__(self)

	def run(self):
		#perform a series of computations and save to dataset
		for idx in xrange(1024):
			random_number = random.random() * 0.01
			#perform computation
			time.sleep(random_number)
			with lock:	
				#save to dataset
				dset[self.axism, idx] = random_number    

thread1 = ComputeThread(0)
thread2 = ComputeThread(1)

thread1.start()
thread2.start()

#wait until both threads have finished
thread1.join()
thread2.join()

f.close()

