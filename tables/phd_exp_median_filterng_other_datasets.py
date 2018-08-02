# -*- coding: utf-8 -*-
"""

Copyright 2008-2016. Karlsruhe Institute of Technology

Data evaluation scripts for benchmarking of optical flow methods on X-ray data

PhD thesis: "Automated Analysis of Time-resolved X-ray Data using Optical Flow Methods"
Author: Alexey Ershov

Fulltext link: https://publikationen.bibliothek.kit.edu/1000055519

"""

from numpy import *
import matplotlib.pyplot as plt
import numpy as np
from pylab import *


#data_rub = r"O:\\DATA\\of_experiments\\clg\\noise_rub_grey\\numpy_data.npy"
#meta_rub = r"O:\\DATA\\of_experiments\\clg\\noise_rub_grey\\numpy_data.txt"

data_path = r"O:\\DATA\\of_experiments\\"

data0 = np.load(data_path + r"robust_median\\hyd_new\\nofilter\\numpy_data.npy")
data = np.load(data_path + r"robust_median\\hyd_new\\a0\\numpy_data.npy")
data2 = np.load(data_path + r"robust_median\\hyd_new\\numpy_data.npy")


#with open(data_path + r"robust_median\\hyd\\numpy_data.txt", 'r') as f:
#    grey_param_names = eval(f.readline())
#    grey_param_values = eval(f.readline())
#    grey_metric_names = eval(f.readline())
    
with open(data_path + r"robust_median\\hyd_new\\numpy_data.txt", 'r') as f2:
    grey_param_names2 = eval(f2.readline())
    grey_param_values2 = eval(f2.readline())
    grey_metric_names2 = eval(f2.readline())
    
print grey_param_names
print grey_param_values
print grey_metric_names



#print ""
#aee_all = grey_metric_names.index("aee_all")
#aee_disc = grey_metric_names.index("aee_disc")
#aee_untext = grey_metric_names.index("aee_untext")
#aee_art = grey_metric_names.index("aee_art")


aee_all2 = grey_metric_names2.index("aee_all")
aee_disc2 = grey_metric_names2.index("aee_disc")
aee_untext2 = grey_metric_names2.index("aee_untext")
aee_art2 = grey_metric_names2.index("aee_art")

#print aee_all, aee_disc, aee_untext
#print aee_all2, aee_disc2, aee_untext2

# Set data precision
#data0= np.around(data0, decimals=3)
#data= np.around(data, decimals=3)
#data2= np.around(data2, decimals=3)


print "A0 - no artifacts"
sigma  = 0
mode = 0
print "0", "\t", "no filter    ", "\t", np.min(data0[sigma, mode, :,:, aee_all2]), "\t", np.min(data0[sigma, mode, :,:, aee_disc2]), "\t", np.min(data0[sigma, mode, :,:, aee_untext2]), "\t", np.min(data0[sigma, mode, :,:, aee_art2])

mode = 0
print "0", "\t", "median3     ", "\t", np.min(data[sigma, mode, :,:, aee_all2]), "\t", np.min(data[sigma, mode, :,:, aee_disc2]), "\t", np.min(data[sigma, mode, :,:, aee_untext2]), "\t", np.min(data[sigma, mode, :,:, aee_art2])
mode = 1
print "0", "\t", "median5     ", "\t", np.min(data[sigma, mode, :,:, aee_all2]), "\t", np.min(data[sigma, mode, :,:, aee_disc2]), "\t", np.min(data[sigma, mode, :,:, aee_untext2]), "\t", np.min(data[sigma, mode, :,:, aee_art2])
mode = 2
print "0", "\t", "median7     ", "\t", np.min(data[sigma, mode, :,:, aee_all2]), "\t", np.min(data[sigma, mode, :,:, aee_disc2]), "\t", np.min(data[sigma, mode, :,:, aee_untext2]), "\t", np.min(data[sigma, mode, :,:, aee_art2])
mode = 3
print "0", "\t", "median9     ", "\t", np.min(data[sigma, mode, :,:, aee_all2]), "\t", np.min(data[sigma, mode, :,:, aee_disc2]), "\t", np.min(data[sigma, mode, :,:, aee_untext2]), "\t", np.min(data[sigma, mode, :,:, aee_art2])





sigma  = 1
mode = 0
print "1", "\t", "no filter    ", "\t", np.min(data0[sigma, mode, :,:, aee_all2]), "\t", np.min(data0[sigma, mode, :,:, aee_disc2]), "\t", np.min(data0[sigma, mode, :,:, aee_untext2]), "\t", np.min(data0[sigma, mode, :,:, aee_art2])

sigma  = 0
mode = 0
print "1", "\t", "median3     ", "\t", np.min(data2[sigma, mode, :,:, aee_all2]), "\t", np.min(data2[sigma, mode, :,:, aee_disc2]), "\t", np.min(data2[sigma, mode, :,:, aee_untext2]), "\t", np.min(data2[sigma, mode, :,:, aee_art2])
mode = 1
print "1", "\t", "median5     ", "\t", np.min(data2[sigma, mode, :,:, aee_all2]), "\t", np.min(data2[sigma, mode, :,:, aee_disc2]), "\t", np.min(data2[sigma, mode, :,:, aee_untext2]), "\t", np.min(data2[sigma, mode, :,:, aee_art2])
mode = 2
print "1", "\t", "median7     ", "\t", np.min(data2[sigma, mode, :,:, aee_all2]), "\t", np.min(data2[sigma, mode, :,:, aee_disc2]), "\t", np.min(data2[sigma, mode, :,:, aee_untext2]), "\t", np.min(data2[sigma, mode, :,:, aee_art2])
mode = 3
print "1", "\t", "median9     ", "\t", np.min(data2[sigma, mode, :,:, aee_all2]), "\t", np.min(data2[sigma, mode, :,:, aee_disc2]), "\t", np.min(data2[sigma, mode, :,:, aee_untext2]), "\t", np.min(data2[sigma, mode, :,:, aee_art2])


sigma  = 2
mode = 0
print "2", "\t", "no filter    ", "\t", np.min(data0[sigma, mode, :,:, aee_all2]), "\t", np.min(data0[sigma, mode, :,:, aee_disc2]), "\t", np.min(data0[sigma, mode, :,:, aee_untext2]), "\t", np.min(data0[sigma, mode, :,:, aee_art2])

sigma  = 1
mode = 0
print "2", "\t", "median3    ", "\t", np.min(data2[sigma, mode, :,:, aee_all2]), "\t", np.min(data2[sigma, mode, :,:, aee_disc2]), "\t", np.min(data2[sigma, mode, :,:, aee_untext2]), "\t", np.min(data2[sigma, mode, :,:, aee_art2])
mode = 1
print "2", "\t", "median5     ", "\t", np.min(data2[sigma, mode, :,:, aee_all2]), "\t", np.min(data2[sigma, mode, :,:, aee_disc2]), "\t", np.min(data2[sigma, mode, :,:, aee_untext2]), "\t", np.min(data2[sigma, mode, :,:, aee_art2])
mode = 2
print "2", "\t", "median7     ", "\t", np.min(data2[sigma, mode, :,:, aee_all2]), "\t", np.min(data2[sigma, mode, :,:, aee_disc2]), "\t", np.min(data2[sigma, mode, :,:, aee_untext2]), "\t", np.min(data2[sigma, mode, :,:, aee_art2])
mode = 3
print "2", "\t", "median9    ", "\t", np.min(data2[sigma, mode, :,:, aee_all2]), "\t", np.min(data2[sigma, mode, :,:, aee_disc2]), "\t", np.min(data2[sigma, mode, :,:, aee_untext2]), "\t", np.min(data2[sigma, mode, :,:, aee_art2])

sigma  = 3
mode = 0
print "3", "\t", "no filter    ", "\t", np.min(data0[sigma, mode, :,:, aee_all2]), "\t", np.min(data0[sigma, mode, :,:, aee_disc2]), "\t", np.min(data0[sigma, mode, :,:, aee_untext2]), "\t", np.min(data0[sigma, mode, :,:, aee_art2])

sigma  = 2
mode = 0
print "3", "\t", "median3     ", "\t", np.min(data2[sigma, mode, :,:, aee_all2]), "\t", np.min(data2[sigma, mode, :,:, aee_disc2]), "\t", np.min(data2[sigma, mode, :,:, aee_untext2]), "\t", np.min(data2[sigma, mode, :,:, aee_art2])
mode = 1
print "3", "\t", "median5     ", "\t", np.min(data2[sigma, mode, :,:, aee_all2]), "\t", np.min(data2[sigma, mode, :,:, aee_disc2]), "\t", np.min(data2[sigma, mode, :,:, aee_untext2]), "\t", np.min(data2[sigma, mode, :,:, aee_art2])
mode = 2
print "3", "\t", "median7     ", "\t", np.min(data2[sigma, mode, :,:, aee_all2]), "\t", np.min(data2[sigma, mode, :,:, aee_disc2]), "\t", np.min(data2[sigma, mode, :,:, aee_untext2]), "\t", np.min(data2[sigma, mode, :,:, aee_art2])
mode = 3
print "3", "\t", "median9     ", "\t", np.min(data2[sigma, mode, :,:, aee_all2]), "\t", np.min(data2[sigma, mode, :,:, aee_disc2]), "\t", np.min(data2[sigma, mode, :,:, aee_untext2]), "\t", np.min(data2[sigma, mode, :,:, aee_art2])










