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


data_f1 = np.load(data_path + r"filter\\rub_both\\f1\\numpy_data.npy")
data_f2 = np.load(data_path + r"filter\\rub_both\\f2\\numpy_data.npy")
data_f3 = np.load(data_path + r"filter\\rub_both\\f3\\numpy_data.npy")
data_f4 = np.load(data_path + r"filter\\rub_both\\f4\\numpy_data.npy")


with open(data_path + r"filter\\rub_both\\f1\\numpy_data.txt", 'r') as f:
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
aee_art = grey_metric_names.index("aee_art")

print aee_all, aee_disc, aee_untext

# Set data precision
data_f1= np.around(data_f1, decimals=3)
data_f2= np.around(data_f2, decimals=3)
data_f3= np.around(data_f3, decimals=3)
data_f4= np.around(data_f4, decimals=3)




sigma  = 0
data = data_f1
print "025", "\t", "No filter     ", "\t",np.min(data[sigma, 0, 0,:, aee_all]), "\t", np.min(data[sigma, 0, 0,:, aee_disc]), "\t", np.min(data[sigma, 0, 0,:, aee_untext]) # "\t", np.min(data[sigma, 0, 0,:, aee_art])

print "025", "\t", "Gaussian     ", "\t", np.min(data[sigma, 0, :,:, aee_all]), "\t", np.min(data[sigma, 0, :,:, aee_disc]), "\t", np.min(data[sigma, 0, :,:, aee_untext]) #"\t", np.min(data[sigma, 0, 0,:, aee_art])

data = data_f2
print "025", "\t", "Median      ",  "\t", np.min(data[sigma, 0, :,:, aee_all]), "\t", np.min(data[sigma, 0, :,:, aee_disc]), "\t", np.min(data[sigma, 0, :,:, aee_untext]) #"\t", np.min(data[sigma, 0, 0,:, aee_art])

data = data_f3
print "025", "\t", "Bilateral    ", "\t", np.min(data[sigma, 0, :,:, aee_all]), "\t", np.min(data[sigma, 0, :,:, aee_disc]), "\t", np.min(data[sigma, 0, :,:, aee_untext]) #"\t", np.min(data[sigma, 0, 0,:, aee_art])

data = data_f4
print "025", "\t", "Anisotropic  ", "\t", np.min(data[sigma, 0, :,:, aee_all]), "\t", np.min(data[sigma, 0, :,:, aee_disc]), "\t", np.min(data[sigma, 0, :,:, aee_untext]) #"\t", np.min(data[sigma, 0, 0,:, aee_art])



sigma  = 1
data = data_f1
print "050", "\t", "No filter     ", "\t",np.min(data[sigma, 0, 0,:, aee_all]), "\t", np.min(data[sigma, 0, 0,:, aee_disc]), "\t", np.min(data[sigma, 0, 0,:, aee_untext]) #"\t", np.min(data[sigma, 0, 0,:, aee_art])
print "050", "\t", "Gaussian     ", "\t", np.min(data[sigma, 0, :,:, aee_all]), "\t", np.min(data[sigma, 0, :,:, aee_disc]), "\t", np.min(data[sigma, 0, :,:, aee_untext]) #"\t", np.min(data[sigma, 0, 0,:, aee_art])

data = data_f2
print "050", "\t", "Median      ",  "\t", np.min(data[sigma, 0, :,:, aee_all]), "\t", np.min(data[sigma, 0, :,:, aee_disc]), "\t", np.min(data[sigma, 0, :,:, aee_untext]) #"\t", np.min(data[sigma, 0, 0,:, aee_art])

data = data_f3
print "050", "\t", "Bilateral    ", "\t", np.min(data[sigma, 0, :,:, aee_all]), "\t", np.min(data[sigma, 0, :,:, aee_disc]), "\t", np.min(data[sigma, 0, :,:, aee_untext]) #"\t", np.min(data[sigma, 0, 0,:, aee_art])

data = data_f4
print "050", "\t", "Anisotropic  ", "\t", np.min(data[sigma, 0, :,:, aee_all]), "\t", np.min(data[sigma, 0, :,:, aee_disc]), "\t", np.min(data[sigma, 0, :,:, aee_untext]) #"\t", np.min(data[sigma, 0, 0,:, aee_art])


sigma  = 2
data = data_f1
print "100", "\t", "No filter     ", "\t",np.min(data[sigma, 0, 0,:, aee_all]), "\t", np.min(data[sigma, 0, 0,:, aee_disc]), "\t", np.min(data[sigma, 0, 0,:, aee_untext]) #"\t", np.min(data[sigma, 0, 0,:, aee_art])
print "100", "\t", "Gaussian     ", "\t", np.min(data[sigma, 0, :,:, aee_all]), "\t", np.min(data[sigma, 0, :,:, aee_disc]), "\t", np.min(data[sigma, 0, :,:, aee_untext]) #"\t", np.min(data[sigma, 0, 0,:, aee_art])

data = data_f2
print "100", "\t", "Median      ",  "\t", np.min(data[sigma, 0, :,:, aee_all]), "\t", np.min(data[sigma, 0, :,:, aee_disc]), "\t", np.min(data[sigma, 0, :,:, aee_untext]) #"\t", np.min(data[sigma, 0, 0,:, aee_art])

data = data_f3
print "100", "\t", "Bilateral    ", "\t", np.min(data[sigma, 0, :,:, aee_all]), "\t", np.min(data[sigma, 0, :,:, aee_disc]), "\t", np.min(data[sigma, 0, :,:, aee_untext]) #"\t", np.min(data[sigma, 0, 0,:, aee_art])

data = data_f4
print "100", "\t", "Anisotropic  ", "\t", np.min(data[sigma, 0, :,:, aee_all]), "\t", np.min(data[sigma, 0, :,:, aee_disc]), "\t", np.min(data[sigma, 0, :,:, aee_untext]) #"\t", np.min(data[sigma, 0, 0,:, aee_art])


sigma  = 3
data = data_f1
print "200", "\t", "No filter     ", "\t",np.min(data[sigma, 0, 0,:, aee_all]), "\t", np.min(data[sigma, 0, 0,:, aee_disc]), "\t", np.min(data[sigma, 0, 0,:, aee_untext]) #"\t", np.min(data[sigma, 0, 0,:, aee_art])
print "200", "\t", "Gaussian     ", "\t", np.min(data[sigma, 0, :,:, aee_all]), "\t", np.min(data[sigma, 0, :,:, aee_disc]), "\t", np.min(data[sigma, 0, :,:, aee_untext]) #"\t", np.min(data[sigma, 0, 0,:, aee_art])

data = data_f2
print "200", "\t", "Median      ",  "\t", np.min(data[sigma, 0, :,:, aee_all]), "\t", np.min(data[sigma, 0, :,:, aee_disc]), "\t", np.min(data[sigma, 0, :,:, aee_untext]) #"\t", np.min(data[sigma, 0, 0,:, aee_art])

data = data_f3
print "200", "\t", "Bilateral    ", "\t", np.min(data[sigma, 0, :,:, aee_all]), "\t", np.min(data[sigma, 0, :,:, aee_disc]), "\t", np.min(data[sigma, 0, :,:, aee_untext]) #"\t", np.min(data[sigma, 0, 0,:, aee_art])

data = data_f4
print "200", "\t", "Anisotropic  ", "\t", np.min(data[sigma, 0, :,:, aee_all]), "\t", np.min(data[sigma, 0, :,:, aee_disc]), "\t", np.min(data[sigma, 0, :,:, aee_untext]) #"\t", np.min(data[sigma, 0, 0,:, aee_art])



