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


data_all = np.load(data_path + r"robust_noise\\hyd\\numpy_data.npy")



with open(data_path + r"robust_noise\\hyd\\numpy_data.txt", 'r') as f:
    grey_param_names = eval(f.readline())
    grey_param_values = eval(f.readline())
    grey_metric_names = eval(f.readline())
    

print grey_param_names
print grey_param_values
print grey_metric_names



print ""
aee_all = grey_metric_names.index("aee_all")
aee_disc = grey_metric_names.index("aee_disc")
aee_untext = grey_metric_names.index("aee_untext")

print aee_all, aee_disc, aee_untext

# Set data precision
data_all = np.around(data_all, decimals=3)

grey = 0
grad = 1



sigma  = 0
data = grey
print "0", "\t", "grey", "\t", "simple", "\t", np.min(data_all[sigma, data, 0, :,:,aee_all]), "\t", np.min(data_all[sigma, data, 0, :,:,aee_disc]), "\t", np.min(data_all[sigma, data, 0, :,:,aee_untext])
print "0", "\t", "grey", "\t", "robust", "\t",  np.min(data_all[sigma, data, 1, :,:,aee_all]), "\t", np.min(data_all[sigma, data, 1, :,:,aee_disc]), "\t", np.min(data_all[sigma, data, 1, :,:,aee_untext])

data = grad
print "0", "\t", "grad", "\t", "simple", "\t", np.min(data_all[sigma, data, 0, :,:,aee_all]), "\t", np.min(data_all[sigma, data, 0, :,:,aee_disc]), "\t", np.min(data_all[sigma, data, 0, :,:,aee_untext])
print "0", "\t", "grad", "\t", "robust", "\t",  np.min(data_all[sigma, data, 1, :,:,aee_all]), "\t", np.min(data_all[sigma, data, 1, :,:,aee_disc]), "\t", np.min(data_all[sigma, data, 1, :,:,aee_untext])


sigma  = 1
data = grey
print "5", "\t", "grey", "\t", "simple", "\t", np.min(data_all[sigma, data, 0, :,:,aee_all]), "\t", np.min(data_all[sigma, data, 0, :,:,aee_disc]), "\t", np.min(data_all[sigma, data, 0, :,:,aee_untext])
print "5", "\t", "grey", "\t", "robust", "\t",  np.min(data_all[sigma, data, 1, :,:,aee_all]), "\t", np.min(data_all[sigma, data, 1, :,:,aee_disc]), "\t", np.min(data_all[sigma, data, 1, :,:,aee_untext])

data = grad
print "5", "\t", "grad", "\t", "simple", "\t", np.min(data_all[sigma, data, 0, :,:,aee_all]), "\t", np.min(data_all[sigma, data, 0, :,:,aee_disc]), "\t", np.min(data_all[sigma, data, 0, :,:,aee_untext])
print "5", "\t", "grad", "\t", "robust", "\t",  np.min(data_all[sigma, data, 1, :,:,aee_all]), "\t", np.min(data_all[sigma, data, 1, :,:,aee_disc]), "\t", np.min(data_all[sigma, data, 1, :,:,aee_untext])

sigma  = 2
data = grey
print "10", "\t", "grey", "\t", "simple", "\t", np.min(data_all[sigma, data, 0, :,:,aee_all]), "\t", np.min(data_all[sigma, data, 0, :,:,aee_disc]), "\t", np.min(data_all[sigma, data, 0, :,:,aee_untext])
print "10", "\t", "grey", "\t", "robust", "\t",  np.min(data_all[sigma, data, 1, :,:,aee_all]), "\t", np.min(data_all[sigma, data, 1, :,:,aee_disc]), "\t", np.min(data_all[sigma, data, 1, :,:,aee_untext])

data = grad
print "10", "\t", "grad", "\t", "simple", "\t", np.min(data_all[sigma, data, 0, :,:,aee_all]), "\t", np.min(data_all[sigma, data, 0, :,:,aee_disc]), "\t", np.min(data_all[sigma, data, 0, :,:,aee_untext])
print "10", "\t", "grad", "\t", "robust", "\t",  np.min(data_all[sigma, data, 1, :,:,aee_all]), "\t", np.min(data_all[sigma, data, 1, :,:,aee_disc]), "\t", np.min(data_all[sigma, data, 1, :,:,aee_untext])

sigma  = 3
data = grey
print "20", "\t", "grey", "\t", "simple", "\t", np.min(data_all[sigma, data, 0, :,:,aee_all]), "\t", np.min(data_all[sigma, data, 0, :,:,aee_disc]), "\t", np.min(data_all[sigma, data, 0, :,:,aee_untext])
print "20", "\t", "grey", "\t", "robust", "\t",  np.min(data_all[sigma, data, 1, :,:,aee_all]), "\t", np.min(data_all[sigma, data, 1, :,:,aee_disc]), "\t", np.min(data_all[sigma, data, 1, :,:,aee_untext])

data = grad
print "20", "\t", "grad", "\t", "simple", "\t", np.min(data_all[sigma, data, 0, :,:,aee_all]), "\t", np.min(data_all[sigma, data, 0, :,:,aee_disc]), "\t", np.min(data_all[sigma, data, 0, :,:,aee_untext])
print "20", "\t", "grad", "\t", "robust", "\t",  np.min(data_all[sigma, data, 1, :,:,aee_all]), "\t", np.min(data_all[sigma, data, 1, :,:,aee_disc]), "\t", np.min(data_all[sigma, data, 1, :,:,aee_untext])













