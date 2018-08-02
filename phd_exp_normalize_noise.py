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

data_grey = np.load(data_path + r"noise_data_terms\\rub\\grey\\numpy_data.npy")
data_clg = np.load(data_path + r"clg\\rub\\grey\\numpy_data.npy")
data_norm = np.load(data_path + r"normalize\\rub\\grey\\numpy_data.npy")
data_norm_clg = np.load(data_path + r"normalize\\rub\\grey3\\numpy_data.npy")


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



print "Simple, CLG, Normalized, Normalized + CLG"
print ""
aee_all = grey_metric_names.index("aee_all")
aee_disc = grey_metric_names.index("aee_disc")
aee_untext = grey_metric_names.index("aee_untext")

#print aee_all, aee_disc, aee_untext

# Set data precision
data_grey = np.around(data_grey, decimals=3)
data_clg = np.around(data_clg, decimals=3)
data_norm = np.around(data_norm, decimals=3)
data_norm_clg = np.around(data_norm_clg, decimals=3)

sigma  = 0
print "0", "\t", "grey          ", "\t", np.min(data_grey[sigma,:,:,aee_all+1]), "\t", np.min(data_grey[sigma,:,:,aee_disc+1]), "\t", np.min(data_grey[sigma,:,:,aee_untext+1])
print "0", "\t", "grey+CLG      ", "\t", np.min(data_clg[sigma,:,:,:,aee_all]), "\t", np.min(data_clg[sigma,:,:,:,aee_disc]), "\t", np.min(data_clg[sigma,:,:,:,aee_untext])
print "0", "\t", "grey+norm     ", "\t", np.min(data_norm[sigma,:,:,:,aee_all]), "\t", np.min(data_norm[sigma,:,:,:,aee_disc]), "\t", np.min(data_norm[sigma,:,:,:,aee_untext])
print "0", "\t", "grey+norm+CLG ", "\t", np.min(data_norm_clg[sigma,:,:,:,aee_all]), "\t", np.min(data_norm_clg[sigma,:,:,:,aee_disc]), "\t", np.min(data_norm_clg[sigma,:,:,:,aee_untext])

sigma  = 1
print "5", "\t", "grey          ", "\t", np.min(data_grey[sigma,:,:,aee_all+1]), "\t", np.min(data_grey[sigma,:,:,aee_disc+1]), "\t", np.min(data_grey[sigma,:,:,aee_untext+1])
print "5", "\t", "grey+CLG      ", "\t", np.min(data_clg[sigma,:,:,:,aee_all]), "\t", np.min(data_clg[sigma,:,:,:,aee_disc]), "\t", np.min(data_clg[sigma,:,:,:,aee_untext])
print "5", "\t", "grey+norm     ", "\t", np.min(data_norm[sigma,:,:,:,aee_all]), "\t", np.min(data_norm[sigma,:,:,:,aee_disc]), "\t", np.min(data_norm[sigma,:,:,:,aee_untext])
print "5", "\t", "grey+norm+CLG ", "\t", np.min(data_norm_clg[sigma,:,:,:,aee_all]), "\t", np.min(data_norm_clg[sigma,:,:,:,aee_disc]), "\t", np.min(data_norm_clg[sigma,:,:,:,aee_untext])


sigma  = 2
print "10", "\t", "grey          ", "\t", np.min(data_grey[sigma,:,:,aee_all+1]), "\t", np.min(data_grey[sigma,:,:,aee_disc+1]), "\t", np.min(data_grey[sigma,:,:,aee_untext+1])
print "10", "\t", "grey+CLG      ", "\t", np.min(data_clg[sigma,:,:,:,aee_all]), "\t", np.min(data_clg[sigma,:,:,:,aee_disc]), "\t", np.min(data_clg[sigma,:,:,:,aee_untext])
print "10", "\t", "grey+norm     ", "\t", np.min(data_norm[sigma,:,:,:,aee_all]), "\t", np.min(data_norm[sigma,:,:,:,aee_disc]), "\t", np.min(data_norm[sigma,:,:,:,aee_untext])
print "10", "\t", "grey+norm+CLG ", "\t", np.min(data_norm_clg[sigma,:,:,:,aee_all]), "\t", np.min(data_norm_clg[sigma,:,:,:,aee_disc]), "\t", np.min(data_norm_clg[sigma,:,:,:,aee_untext])


sigma  = 3
print "20", "\t", "grey          ", "\t", np.min(data_grey[sigma,:,:,aee_all+1]), "\t", np.min(data_grey[sigma,:,:,aee_disc+1]), "\t", np.min(data_grey[sigma,:,:,aee_untext+1])
print "20", "\t", "grey+CLG      ", "\t", np.min(data_clg[sigma,:,:,:,aee_all]), "\t", np.min(data_clg[sigma,:,:,:,aee_disc]), "\t", np.min(data_clg[sigma,:,:,:,aee_untext])
print "20", "\t", "grey+norm     ", "\t", np.min(data_norm[sigma,:,:,:,aee_all]), "\t", np.min(data_norm[sigma,:,:,:,aee_disc]), "\t", np.min(data_norm[sigma,:,:,:,aee_untext])
print "20", "\t", "grey+norm+CLG ", "\t", np.min(data_norm_clg[sigma,:,:,:,aee_all]), "\t", np.min(data_norm_clg[sigma,:,:,:,aee_disc]), "\t", np.min(data_norm_clg[sigma,:,:,:,aee_untext])









