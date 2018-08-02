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

# Gaussian Noise
data_grey = np.load(data_path + r"noise_data_terms\\rub\\grey\\numpy_data.npy")
data_grad = np.load(data_path + r"noise_data_terms\\rub\\grad\\numpy_data.npy")
data_lapl = np.load(data_path + r"noise_data_terms\\rub\\lapl\\numpy_data.npy")
data_norm = np.load(data_path + r"noise_data_terms\\rub\\norm\\numpy_data.npy")

# Spike (Salt and Pepper) Noise
data_grey_s = np.load(data_path + r"noise_data_terms\\rub_spike\\grey\\numpy_data.npy")
data_grad_s = np.load(data_path + r"noise_data_terms\\rub_spike\\grad\\numpy_data.npy")
data_lapl_s = np.load(data_path + r"noise_data_terms\\rub_spike\\lapl\\numpy_data.npy")
data_norm_s = np.load(data_path + r"noise_data_terms\\rub_spike\\norm\\numpy_data.npy")

# Poisson Noise
data_p = np.load(data_path + r"noise_data_terms\\rub_poisson2\\numpy_data.npy")

with open(data_path + r"noise_data_terms\\rub\\grey\\numpy_data.txt", 'r') as f:
#with open(data_path + r"noise_data_terms\\rub_poisson\\numpy_data.txt", 'r') as f:
    grey_param_names = eval(f.readline())
    grey_param_values = eval(f.readline())
    grey_metric_names = eval(f.readline())
    

print grey_param_names
print grey_param_values
print grey_metric_names

print ""
print "------------ aee_all ---------------------"
measure = grey_metric_names.index("aee_all")
print "grey |", np.min(data_grey[0,:,:,measure]), np.min(data_grey[1,:,:,measure]), np.min(data_grey[2,:,:,measure]), np.min(data_grey[3,:,:,measure])
print "grad |", np.min(data_grad[0,:,:,measure]), np.min(data_grad[1,:,:,measure]), np.min(data_grad[2,:,:,measure]), np.min(data_grad[3,:,:,measure])
print "lapl |", np.min(data_lapl[0,:,:,measure]), np.min(data_lapl[1,:,:,measure]), np.min(data_lapl[2,:,:,measure]), np.min(data_lapl[3,:,:,measure])
print "norm |", np.min(data_norm[0,:,:,measure]), np.min(data_norm[1,:,:,measure]), np.min(data_norm[2,:,:,measure]), np.min(data_norm[3,:,:,measure])


print ""
print "------------ aee_disc ---------------------"
measure = grey_metric_names.index("aee_disc")
print "grey |", np.min(data_grey[0,:,:,measure]), np.min(data_grey[1,:,:,measure]), np.min(data_grey[2,:,:,measure]), np.min(data_grey[3,:,:,measure])
print "grad |", np.min(data_grad[0,:,:,measure]), np.min(data_grad[1,:,:,measure]), np.min(data_grad[2,:,:,measure]), np.min(data_grad[3,:,:,measure])
print "lapl |", np.min(data_lapl[0,:,:,measure]), np.min(data_lapl[1,:,:,measure]), np.min(data_lapl[2,:,:,measure]), np.min(data_lapl[3,:,:,measure])
print "norm |", np.min(data_norm[0,:,:,measure]), np.min(data_norm[1,:,:,measure]), np.min(data_norm[2,:,:,measure]), np.min(data_norm[3,:,:,measure])

print ""
print "------------ aee_untext ---------------------"
measure = grey_metric_names.index("aee_untext")
print "grey |", np.min(data_grey[0,:,:,measure]), np.min(data_grey[1,:,:,measure]), np.min(data_grey[2,:,:,measure]), np.min(data_grey[3,:,:,measure])
print "grad |", np.min(data_grad[0,:,:,measure]), np.min(data_grad[1,:,:,measure]), np.min(data_grad[2,:,:,measure]), np.min(data_grad[3,:,:,measure])
print "lapl |", np.min(data_lapl[0,:,:,measure]), np.min(data_lapl[1,:,:,measure]), np.min(data_lapl[2,:,:,measure]), np.min(data_lapl[3,:,:,measure])
print "norm |", np.min(data_norm[0,:,:,measure]), np.min(data_norm[1,:,:,measure]), np.min(data_norm[2,:,:,measure]), np.min(data_norm[3,:,:,measure])


print "Gaussian Noise"
print ""
aee_all = grey_metric_names.index("aee_all")
aee_disc = grey_metric_names.index("aee_disc")
aee_untext = grey_metric_names.index("aee_untext")

print aee_all, aee_disc, aee_untext

# Set data precision
data_grey = np.around(data_grey, decimals=3)
data_grad = np.around(data_grad, decimals=3)
data_lapl = np.around(data_lapl, decimals=3)
data_norm = np.around(data_norm, decimals=3)

sigma  = 0
print "0", "\t", "grey", "\t", np.min(data_grey[sigma,:,:,aee_all]), "\t", np.min(data_grey[sigma,:,:,aee_disc]), "\t", np.min(data_grey[sigma,:,:,aee_untext])
print "0", "\t", "grad", "\t", np.min(data_grad[sigma,:,:,aee_all]), "\t", np.min(data_grad[sigma,:,:,aee_disc]), "\t", np.min(data_grad[sigma,:,:,aee_untext])
print "0", "\t", "lapl", "\t", np.min(data_lapl[sigma,:,:,aee_all]), "\t", np.min(data_lapl[sigma,:,:,aee_disc]), "\t", np.min(data_lapl[sigma,:,:,aee_untext])
print "0", "\t", "norm", "\t", np.min(data_norm[sigma,:,:,aee_all]), "\t", np.min(data_norm[sigma,:,:,aee_disc]), "\t", np.min(data_norm[sigma,:,:,aee_untext])

sigma  = 1
print "5", "\t", "grey", "\t", np.min(data_grey[sigma,:,:,aee_all]), "\t", np.min(data_grey[sigma,:,:,aee_disc]), "\t", np.min(data_grey[sigma,:,:,aee_untext])
print "5", "\t", "grad", "\t", np.min(data_grad[sigma,:,:,aee_all]), "\t", np.min(data_grad[sigma,:,:,aee_disc]), "\t", np.min(data_grad[sigma,:,:,aee_untext])
print "5", "\t", "lapl", "\t", np.min(data_lapl[sigma,:,:,aee_all]), "\t", np.min(data_lapl[sigma,:,:,aee_disc]), "\t", np.min(data_lapl[sigma,:,:,aee_untext])
print "5", "\t", "norm", "\t", np.min(data_norm[sigma,:,:,aee_all]), "\t", np.min(data_norm[sigma,:,:,aee_disc]), "\t", np.min(data_norm[sigma,:,:,aee_untext])

sigma  = 2
print "10", "\t", "grey", "\t", np.min(data_grey[sigma,:,:,aee_all]), "\t", np.min(data_grey[sigma,:,:,aee_disc]), "\t", np.min(data_grey[sigma,:,:,aee_untext])
print "10", "\t", "grad", "\t", np.min(data_grad[sigma,:,:,aee_all]), "\t", np.min(data_grad[sigma,:,:,aee_disc]), "\t", np.min(data_grad[sigma,:,:,aee_untext])
print "10", "\t", "lapl", "\t", np.min(data_lapl[sigma,:,:,aee_all]), "\t", np.min(data_lapl[sigma,:,:,aee_disc]), "\t", np.min(data_lapl[sigma,:,:,aee_untext])
print "10", "\t", "norm", "\t", np.min(data_norm[sigma,:,:,aee_all]), "\t", np.min(data_norm[sigma,:,:,aee_disc]), "\t", np.min(data_norm[sigma,:,:,aee_untext])

sigma  = 3
print "20", "\t", "grey", "\t", np.min(data_grey[sigma,:,:,aee_all]), "\t", np.min(data_grey[sigma,:,:,aee_disc]), "\t", np.min(data_grey[sigma,:,:,aee_untext])
print "20", "\t", "grad", "\t", np.min(data_grad[sigma,:,:,aee_all]), "\t", np.min(data_grad[sigma,:,:,aee_disc]), "\t", np.min(data_grad[sigma,:,:,aee_untext])
print "20", "\t", "lapl", "\t", np.min(data_lapl[sigma,:,:,aee_all]), "\t", np.min(data_lapl[sigma,:,:,aee_disc]), "\t", np.min(data_lapl[sigma,:,:,aee_untext])
print "20", "\t", "norm", "\t", np.min(data_norm[sigma,:,:,aee_all]), "\t", np.min(data_norm[sigma,:,:,aee_disc]), "\t", np.min(data_norm[sigma,:,:,aee_untext])


print "Spike Noise"
print ""


# Set data precision
data_grey_s = np.around(data_grey_s, decimals=3)
data_grad_s = np.around(data_grad_s, decimals=3)
data_lapl_s = np.around(data_lapl_s, decimals=3)
data_norm_s = np.around(data_norm_s, decimals=3)

level  = 0
print "0", "\t", "grey", "\t", np.min(data_grey_s[level,:,:,aee_all]), "\t", np.min(data_grey_s[level,:,:,aee_disc]), "\t", np.min(data_grey_s[level,:,:,aee_untext])
print "0", "\t", "grad", "\t", np.min(data_grad_s[level,:,:,aee_all]), "\t", np.min(data_grad_s[level,:,:,aee_disc]), "\t", np.min(data_grad_s[level,:,:,aee_untext])
print "0", "\t", "lapl", "\t", np.min(data_lapl_s[level,:,:,aee_all]), "\t", np.min(data_lapl_s[level,:,:,aee_disc]), "\t", np.min(data_lapl_s[level,:,:,aee_untext])
print "0", "\t", "norm", "\t", np.min(data_norm_s[level,:,:,aee_all]), "\t", np.min(data_norm_s[level,:,:,aee_disc]), "\t", np.min(data_norm_s[level,:,:,aee_untext])

level  = 1
print "1", "\t", "grey", "\t", np.min(data_grey_s[level,:,:,aee_all]), "\t", np.min(data_grey_s[level,:,:,aee_disc]), "\t", np.min(data_grey_s[level,:,:,aee_untext])
print "1", "\t", "grad", "\t", np.min(data_grad_s[level,:,:,aee_all]), "\t", np.min(data_grad_s[level,:,:,aee_disc]), "\t", np.min(data_grad_s[level,:,:,aee_untext])
print "1", "\t", "lapl", "\t", np.min(data_lapl_s[level,:,:,aee_all]), "\t", np.min(data_lapl_s[level,:,:,aee_disc]), "\t", np.min(data_lapl_s[level,:,:,aee_untext])
print "1", "\t", "norm", "\t", np.min(data_norm_s[level,:,:,aee_all]), "\t", np.min(data_norm_s[level,:,:,aee_disc]), "\t", np.min(data_norm_s[level,:,:,aee_untext])

level  = 2
print "2", "\t", "grey", "\t", np.min(data_grey_s[level,:,:,aee_all]), "\t", np.min(data_grey_s[level,:,:,aee_disc]), "\t", np.min(data_grey_s[level,:,:,aee_untext])
print "2", "\t", "grad", "\t", np.min(data_grad_s[level,:,:,aee_all]), "\t", np.min(data_grad_s[level,:,:,aee_disc]), "\t", np.min(data_grad_s[level,:,:,aee_untext])
print "2", "\t", "lapl", "\t", np.min(data_lapl_s[level,:,:,aee_all]), "\t", np.min(data_lapl_s[level,:,:,aee_disc]), "\t", np.min(data_lapl_s[level,:,:,aee_untext])
print "2", "\t", "norm", "\t", np.min(data_norm_s[level,:,:,aee_all]), "\t", np.min(data_norm_s[level,:,:,aee_disc]), "\t", np.min(data_norm_s[level,:,:,aee_untext])

level  = 3
print "3", "\t", "grey", "\t", np.min(data_grey_s[level,:,:,aee_all]), "\t", np.min(data_grey_s[level,:,:,aee_disc]), "\t", np.min(data_grey_s[level,:,:,aee_untext])
print "3", "\t", "grad", "\t", np.min(data_grad_s[level,:,:,aee_all]), "\t", np.min(data_grad_s[level,:,:,aee_disc]), "\t", np.min(data_grad_s[level,:,:,aee_untext])
print "3", "\t", "lapl", "\t", np.min(data_lapl_s[level,:,:,aee_all]), "\t", np.min(data_lapl_s[level,:,:,aee_disc]), "\t", np.min(data_lapl_s[level,:,:,aee_untext])
print "3", "\t", "norm", "\t", np.min(data_norm_s[level,:,:,aee_all]), "\t", np.min(data_norm_s[level,:,:,aee_disc]), "\t", np.min(data_norm_s[level,:,:,aee_untext])


print "Poisson Noise"
print ""

with open(data_path + r"noise_data_terms\\rub_poisson2\\numpy_data.txt", 'r') as f:
    grey_param_names = eval(f.readline())
    grey_param_values = eval(f.readline())
    grey_metric_names = eval(f.readline())

data_grey_s = np.around(data_p, decimals=3)

aee_all = grey_metric_names.index("aee_all")
aee_disc = grey_metric_names.index("aee_disc")
aee_untext = grey_metric_names.index("aee_untext")

level  = 0
data = 0
print "0", "\t", "grey", "\t", np.min(data_grey_s[data, level,:,:,aee_all]), "\t", np.min(data_grey_s[data, level,:,:,aee_disc]), "\t", np.min(data_grey_s[data, level,:,:,aee_untext])
data = 1
print "0", "\t", "grad", "\t", np.min(data_grey_s[data, level,:,:,aee_all]), "\t", np.min(data_grey_s[data, level,:,:,aee_disc]), "\t", np.min(data_grey_s[data, level,:,:,aee_untext])
data = 3
print "0", "\t", "lapl", "\t", np.min(data_grey_s[data, level,:,:,aee_all]), "\t", np.min(data_grey_s[data, level,:,:,aee_disc]), "\t", np.min(data_grey_s[data, level,:,:,aee_untext])
data = 2
print "0", "\t", "norm", "\t", np.min(data_grey_s[data, level,:,:,aee_all]), "\t", np.min(data_grey_s[data, level,:,:,aee_disc]), "\t", np.min(data_grey_s[data, level,:,:,aee_untext])


level  = 1
data = 0
print "1", "\t", "grey", "\t", np.min(data_grey_s[data, level,:,:,aee_all]), "\t", np.min(data_grey_s[data, level,:,:,aee_disc]), "\t", np.min(data_grey_s[data, level,:,:,aee_untext])
data = 1
print "1", "\t", "grad", "\t", np.min(data_grey_s[data, level,:,:,aee_all]), "\t", np.min(data_grey_s[data, level,:,:,aee_disc]), "\t", np.min(data_grey_s[data, level,:,:,aee_untext])
data = 3
print "1", "\t", "lapl", "\t", np.min(data_grey_s[data, level,:,:,aee_all]), "\t", np.min(data_grey_s[data, level,:,:,aee_disc]), "\t", np.min(data_grey_s[data, level,:,:,aee_untext])
data = 2
print "1", "\t", "norm", "\t", np.min(data_grey_s[data, level,:,:,aee_all]), "\t", np.min(data_grey_s[data, level,:,:,aee_disc]), "\t", np.min(data_grey_s[data, level,:,:,aee_untext])

level  = 2
data = 0
print "2", "\t", "grey", "\t", np.min(data_grey_s[data, level,:,:,aee_all]), "\t", np.min(data_grey_s[data, level,:,:,aee_disc]), "\t", np.min(data_grey_s[data, level,:,:,aee_untext])
data = 1
print "2", "\t", "grad", "\t", np.min(data_grey_s[data, level,:,:,aee_all]), "\t", np.min(data_grey_s[data, level,:,:,aee_disc]), "\t", np.min(data_grey_s[data, level,:,:,aee_untext])
data = 3
print "2", "\t", "lapl", "\t", np.min(data_grey_s[data, level,:,:,aee_all]), "\t", np.min(data_grey_s[data, level,:,:,aee_disc]), "\t", np.min(data_grey_s[data, level,:,:,aee_untext])
data = 2
print "2", "\t", "norm", "\t", np.min(data_grey_s[data, level,:,:,aee_all]), "\t", np.min(data_grey_s[data, level,:,:,aee_disc]), "\t", np.min(data_grey_s[data, level,:,:,aee_untext])

level  = 3
data = 0
print "3", "\t", "grey", "\t", np.min(data_grey_s[data, level,:,:,aee_all]), "\t", np.min(data_grey_s[data, level,:,:,aee_disc]), "\t", np.min(data_grey_s[data, level,:,:,aee_untext])
data = 1
print "3", "\t", "grad", "\t", np.min(data_grey_s[data, level,:,:,aee_all]), "\t", np.min(data_grey_s[data, level,:,:,aee_disc]), "\t", np.min(data_grey_s[data, level,:,:,aee_untext])
data = 3
print "3", "\t", "lapl", "\t", np.min(data_grey_s[data, level,:,:,aee_all]), "\t", np.min(data_grey_s[data, level,:,:,aee_disc]), "\t", np.min(data_grey_s[data, level,:,:,aee_untext])
data = 2
print "3", "\t", "norm", "\t", np.min(data_grey_s[data, level,:,:,aee_all]), "\t", np.min(data_grey_s[data, level,:,:,aee_disc]), "\t", np.min(data_grey_s[data, level,:,:,aee_untext])
