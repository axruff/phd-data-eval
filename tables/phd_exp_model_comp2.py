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

print "Hello"


data_hs = np.load(data_path + r"model_comp\\1_hs\\numpy_data.npy")
data_flow = np.load(data_path + r"model_comp\\2_flow\\numpy_data.npy")
#data_log = np.load(data_path + r"brightness\\data_terms2\\numpy_data.npy")


with open(data_path + r"model_comp\\1_hs\\numpy_data.txt", 'r') as f:
    grey_param_names = eval(f.readline())
    grey_param_values = eval(f.readline())
    grey_metric_names = eval(f.readline())
    

#print grey_param_names
#print grey_param_values
#print grey_metric_names


print ""
aee_all = grey_metric_names.index("aee_all")
aee_disc = grey_metric_names.index("aee_disc")
aee_untext = grey_metric_names.index("aee_untext")
aee_art = grey_metric_names.index("aee_art")

#print aee_all, aee_disc, aee_untext

# Set data precision
data_hs= np.around(data_hs, decimals=3)
data_flow= np.around(data_flow, decimals=3)

data = data_hs

print data

print "hs", "\t", np.min(data[:,:, aee_all]), "\t", np.min(data[:,:, aee_disc]), "\t", np.min(data[:,:, aee_untext],  "\t", np.min(data[:,:, aee_art])
