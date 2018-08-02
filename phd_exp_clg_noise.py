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



data_path = r"O:\\DATA\\of_experiments\\"

data_grey = np.load(data_path + r"clg\\rub\\grey\\numpy_data.npy")
data_grad = np.load(data_path + r"clg\\rub\\grad\\numpy_data.npy")
data_grey_spike = np.load(data_path + r"clg\\rub\\grey_spike\\numpy_data.npy")
data_grad_spike = np.load(data_path + r"clg\\rub\\grad_spike\\numpy_data.npy")

#data_norm = np.load(data_path + r"normalize\\rub\\grey2\\numpy_data.npy")
#data_norm2 = np.load(data_path + r"normalize\\rub\\grey3\\numpy_data.npy")
#data_norm3 = np.load(data_path + r"normalize\\rub\\grey4\\numpy_data.npy")


with open(data_path + r"clg\\rub\\grey\\numpy_data.txt", 'r') as f:
    param_names = eval(f.readline())
    param_values = eval(f.readline())
    metric_names = eval(f.readline())
    

print param_names
print param_values
print metric_names

#print np.min(data_grey[0,:,:,:,measure]),


#print ""
#print "------------ aee_all ---------------------"
#measure = metric_names.index("aee_all")

#print "grey |",       np.min(data_grey[0,:,:,:,measure]), np.min(data_grey[1,:,:,:,measure]), np.min(data_grey[2,:,:,:,measure]), np.min(data_grey[3,:,:,:,measure])
#print "grad |",       np.min(data_grad[0,:,:,:,measure]), np.min(data_grad[1,:,:,:,measure]), np.min(data_grad[2,:,:,:,measure]), np.min(data_grad[3,:,:,:,measure])
#print "grey spike |", np.min(data_grey_spike[0,:,:,:,measure]), np.min(data_grey_spike[1,:,:,:,measure]), np.min(data_grey_spike[2,:,:,:,measure]), np.min(data_grey_spike[3,:,:,:,measure])
#print "grad spike |", np.min(data_grad_spike[0,:,:,:,measure]), np.min(data_grad_spike[1,:,:,:,measure]), np.min(data_grad_spike[2,:,:,:,measure]), np.min(data_grad_spike[3,:,:,:,measure])

#print "norm |", np.min(data_norm[0,:,:,:,measure]), np.min(data_norm[1,:,:,:,measure]), np.min(data_norm[2,:,:,:,measure]), np.min(data_norm[3,:,:,:,measure])
#print "norm |", np.min(data_norm2[0,:,:,:,measure]), np.min(data_norm2[1,:,:,:,measure]), np.min(data_norm2[2,:,:,:,measure]), np.min(data_norm2[3,:,:,:,measure])

#print "norm |", np.min(data_norm3[0,:,:,:,measure]), np.min(data_norm3[1,:,:,:,measure])



print "CLG - Gaussian Noise"
print ""
aee_all = grey_metric_names.index("aee_all")
aee_disc = grey_metric_names.index("aee_disc")
aee_untext = grey_metric_names.index("aee_untext")

# Set data precision
data_grey = np.around(data_grey, decimals=3)
data_grad = np.around(data_grad, decimals=3)
data_grey_spike = np.around(data_grey_spike, decimals=3)
data_grad_spike = np.around(data_grad_spike, decimals=3)

sigma  = 0
print "0", "\t", "grey+CLG", "\t", np.min(data_grey[sigma,:,:,:,aee_all]), "\t", np.min(data_grey[sigma,:,:,:,aee_disc]), "\t", np.min(data_grey[sigma,:,:,:,aee_untext])
print "0", "\t", "grad+CLG", "\t", np.min(data_grad[sigma,:,:,:,aee_all]), "\t", np.min(data_grad[sigma,:,:,:,aee_disc]), "\t", np.min(data_grad[sigma,:,:,:,aee_untext])

sigma  = 1
print "5", "\t", "grey+CLG", "\t", np.min(data_grey[sigma,:,:,:,aee_all]), "\t", np.min(data_grey[sigma,:,:,:,aee_disc]), "\t", np.min(data_grey[sigma,:,:,:,aee_untext])
print "5", "\t", "grad+CLG", "\t", np.min(data_grad[sigma,:,:,:,aee_all]), "\t", np.min(data_grad[sigma,:,:,:,aee_disc]), "\t", np.min(data_grad[sigma,:,:,:,aee_untext])


sigma  = 2
print "10", "\t", "grey+CLG", "\t", np.min(data_grey[sigma,:,:,:,aee_all]), "\t", np.min(data_grey[sigma,:,:,:,aee_disc]), "\t", np.min(data_grey[sigma,:,:,:,aee_untext])
print "10", "\t", "grad+CLG", "\t", np.min(data_grad[sigma,:,:,:,aee_all]), "\t", np.min(data_grad[sigma,:,:,:,aee_disc]), "\t", np.min(data_grad[sigma,:,:,:,aee_untext])


sigma  = 3
print "20", "\t", "grey+CLG", "\t", np.min(data_grey[sigma,:,:,:,aee_all]), "\t", np.min(data_grey[sigma,:,:,:,aee_disc]), "\t", np.min(data_grey[sigma,:,:,:,aee_untext])
print "20", "\t", "grad+CLG", "\t", np.min(data_grad[sigma,:,:,:,aee_all]), "\t", np.min(data_grad[sigma,:,:,:,aee_disc]), "\t", np.min(data_grad[sigma,:,:,:,aee_untext])

print "CLG - Spike noise"
print ""

sigma  = 1
print "1", "\t", "grey+CLG", "\t", np.min(data_grey_spike[sigma,:,:,:,aee_all]), "\t", np.min(data_grey_spike[sigma,:,:,:,aee_disc]), "\t", np.min(data_grey_spike[sigma,:,:,:,aee_untext])
print "1", "\t", "grad+CLG", "\t", np.min(data_grad_spike[sigma,:,:,:,aee_all]), "\t", np.min(data_grad_spike[sigma,:,:,:,aee_disc]), "\t", np.min(data_grad_spike[sigma,:,:,:,aee_untext])

sigma  = 2
print "2", "\t", "grey+CLG", "\t", np.min(data_grey_spike[sigma,:,:,:,aee_all]), "\t", np.min(data_grey_spike[sigma,:,:,:,aee_disc]), "\t", np.min(data_grey_spike[sigma,:,:,:,aee_untext])
print "2", "\t", "grad+CLG", "\t", np.min(data_grad_spike[sigma,:,:,:,aee_all]), "\t", np.min(data_grad_spike[sigma,:,:,:,aee_disc]), "\t", np.min(data_grad_spike[sigma,:,:,:,aee_untext])

sigma  = 3
print "3", "\t", "grey+CLG", "\t", np.min(data_grey_spike[sigma,:,:,:,aee_all]), "\t", np.min(data_grey_spike[sigma,:,:,:,aee_disc]), "\t", np.min(data_grey_spike[sigma,:,:,:,aee_untext])
print "3", "\t", "grad+CLG", "\t", np.min(data_grad_spike[sigma,:,:,:,aee_all]), "\t", np.min(data_grad_spike[sigma,:,:,:,aee_disc]), "\t", np.min(data_grad_spike[sigma,:,:,:,aee_untext])






