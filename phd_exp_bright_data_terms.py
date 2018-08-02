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


data = np.load(data_path + r"brightness\\data_terms3\\numpy_data.npy")
#data_log = np.load(data_path + r"brightness\\data_terms2\\numpy_data.npy")


with open(data_path + r"brightness\\data_terms3\\numpy_data.txt", 'r') as f:
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
#aee_art = grey_metric_names.index("aee_art")

print aee_all, aee_disc, aee_untext

# Set data precision
data= np.around(data, decimals=3)
#data_log= np.around(data_log, decimals=3)

sigma  = 0
print "orig", "\t", "grey     ", "\t", np.min(data[sigma, 0, :,:, aee_all]), "\t", np.min(data[sigma, 0, :,:, aee_disc]), "\t", np.min(data[sigma, 0, :,:, aee_untext]) #"\t", np.min(data[sigma, 0, 0,:, aee_art])
print "orig", "\t", "grad     ", "\t", np.min(data[sigma, 1, :,:, aee_all]), "\t", np.min(data[sigma, 1, :,:, aee_disc]), "\t", np.min(data[sigma, 1, :,:, aee_untext]) #"\t", np.min(data[sigma, 0, 0,:, aee_art])
print "orig", "\t", "log     ", "\t",  np.min(data[sigma, 2, :,:, aee_all]), "\t", np.min(data[sigma, 2, :,:, aee_disc]), "\t", np.min(data[sigma, 2, :,:, aee_untext]) #"\t", np.min(data[sigma, 0, 0,:, aee_art])

sigma  = 1

print "add", "\t", "grey     ", "\t", np.min(data[sigma, 0, :,:, aee_all]), "\t", np.min(data[sigma, 0, :,:, aee_disc]), "\t", np.min(data[sigma, 0, :,:, aee_untext]) #"\t", np.min(data[sigma, 0, 0,:, aee_art])
print "add", "\t", "grad     ", "\t", np.min(data[sigma, 1, :,:, aee_all]), "\t", np.min(data[sigma, 1, :,:, aee_disc]), "\t", np.min(data[sigma, 1, :,:, aee_untext]) #"\t", np.min(data[sigma, 0, 0,:, aee_art])
print "add", "\t", "log     ", "\t",  np.min(data[sigma, 2, :,:, aee_all]), "\t", np.min(data[sigma, 2, :,:, aee_disc]), "\t", np.min(data[sigma, 2, :,:, aee_untext]) #"\t", np.min(data[sigma, 0, 0,:, aee_art])

sigma  = 2
print "mult", "\t", "grey     ", "\t", np.min(data[sigma, 0, :,:, aee_all]), "\t", np.min(data[sigma, 0, :,:, aee_disc]), "\t", np.min(data[sigma, 0, :,:, aee_untext]) #"\t", np.min(data[sigma, 0, 0,:, aee_art])
print "mult", "\t", "grad     ", "\t", np.min(data[sigma, 1, :,:, aee_all]), "\t", np.min(data[sigma, 1, :,:, aee_disc]), "\t", np.min(data[sigma, 1, :,:, aee_untext]) #"\t", np.min(data[sigma, 0, 0,:, aee_art])
print "mult", "\t", "log     ", "\t",  np.min(data[sigma, 2, :,:, aee_all]), "\t", np.min(data[sigma, 2, :,:, aee_disc]), "\t", np.min(data[sigma, 2, :,:, aee_untext]) #"\t", np.min(data[sigma, 0, 0,:, aee_art])
sigma  = 3
print "p1", "\t", "grey     ", "\t", np.min(data[sigma, 0, :,:, aee_all]), "\t", np.min(data[sigma, 0, :,:, aee_disc]), "\t", np.min(data[sigma, 0, :,:, aee_untext]) #"\t", np.min(data[sigma, 0, 0,:, aee_art])
print "p1", "\t", "grad     ", "\t", np.min(data[sigma, 1, :,:, aee_all]), "\t", np.min(data[sigma, 1, :,:, aee_disc]), "\t", np.min(data[sigma, 1, :,:, aee_untext]) #"\t", np.min(data[sigma, 0, 0,:, aee_art])
print "p1", "\t", "log     ", "\t",  np.min(data[sigma, 2, :,:, aee_all]), "\t", np.min(data[sigma, 2, :,:, aee_disc]), "\t", np.min(data[sigma, 2, :,:, aee_untext]) #"\t", np.min(data[sigma, 0, 0,:, aee_art])
sigma  = 4
print "p2", "\t", "grey     ", "\t", np.min(data[sigma, 0, :,:, aee_all]), "\t", np.min(data[sigma, 0, :,:, aee_disc]), "\t", np.min(data[sigma, 0, :,:, aee_untext]) #"\t", np.min(data[sigma, 0, 0,:, aee_art])
print "p2", "\t", "grad     ", "\t", np.min(data[sigma, 1, :,:, aee_all]), "\t", np.min(data[sigma, 1, :,:, aee_disc]), "\t", np.min(data[sigma, 1, :,:, aee_untext]) #"\t", np.min(data[sigma, 0, 0,:, aee_art])
print "p2", "\t", "log     ", "\t",  np.min(data[sigma, 2, :,:, aee_all]), "\t", np.min(data[sigma, 2, :,:, aee_disc]), "\t", np.min(data[sigma, 2, :,:, aee_untext]) #"\t", np.min(data[sigma, 0, 0,:, aee_art])



