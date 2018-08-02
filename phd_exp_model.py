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



data_hs = np.load(data_path + r"model_comp\\1_hs\\numpy_data.npy")
data_flow = np.load(data_path + r"model_comp\\2_flow\\numpy_data.npy")
data_warp = np.load(data_path + r"model_comp\\3_warp\\numpy_data.npy")
data_robust = np.load(data_path + r"model_comp\\4_robust\\numpy_data.npy")
data_clg = np.load(data_path + r"model_comp\\5_clg\\numpy_data.npy")
data_median = np.load(data_path + r"model_comp\\6_median\\numpy_data.npy")
data_refine = np.load(data_path + r"model_comp\\7_refine\\numpy_data.npy")
##data_log = np.load(data_path + r"brightness\\data_terms2\\numpy_data.npy")
#
#
with open(data_path + r"model_comp\\7_refine\\numpy_data.txt", 'r') as f:
    grey_param_names = eval(f.readline())
    grey_param_values = eval(f.readline())
    grey_metric_names = eval(f.readline())
    
#
##print grey_param_names
##print grey_param_values
##print grey_metric_names
#
#
#print ""
aee_all = grey_metric_names.index("aee_all")
aee_disc = grey_metric_names.index("aee_disc")
aee_untext = grey_metric_names.index("aee_untext")
aee_art = grey_metric_names.index("aee_art")



r_all = grey_metric_names.index("R1.0_all")
r_disc = grey_metric_names.index("R1.0_disc")
r_untext = grey_metric_names.index("R1.0_untext")
r_art = grey_metric_names.index("R1.0_art")
#
print aee_all, aee_disc, aee_untext, aee_art

print r_all, r_disc, r_untext, r_art 
#
## Set data precision
data_hs= np.around(data_hs, decimals=1)
data_flow= np.around(data_flow, decimals=1)
data_warp= np.around(data_warp, decimals=1)
data_robust= np.around(data_robust, decimals=1)
data_clg= np.around(data_clg, decimals=1)
data_median= np.around(data_median, decimals=1)
data_refine= np.around(data_refine, decimals=1)

print np.min(data_hs[:,:, aee_all])



data = data_hs
print "hs", "\t", np.min(data[:,:, aee_all]), "\t", np.min(data[:,:, aee_disc]), "\t", np.min(data[:,:, aee_untext]), "\t", np.min(data[:,:, aee_art]), "\t", np.min(data[:,:, r_all]), "\t", np.min(data[:,:, r_disc]), "\t", np.min(data[:,:, r_untext]), "\t", np.min(data[:,:, r_art])

data = data_flow
print "flow", "\t", np.min(data[:,:, aee_all]), "\t", np.min(data[:,:, aee_disc]), "\t", np.min(data[:,:, aee_untext]), "\t", np.min(data[:,:, aee_art]), "\t", np.min(data[:,:, r_all]), "\t", np.min(data[:,:, r_disc]), "\t", np.min(data[:,:, r_untext]), "\t", np.min(data[:,:, r_art])

data = data_warp
print "warp", "\t", np.min(data[:,:, aee_all]), "\t", np.min(data[:,:, aee_disc]), "\t", np.min(data[:,:, aee_untext]), "\t", np.min(data[:,:, aee_art]), "\t", np.min(data[:,:, r_all]), "\t", np.min(data[:,:, r_disc]), "\t", np.min(data[:,:, r_untext]), "\t", np.min(data[:,:, r_art])

data = data_robust
print "robust", "\t", np.min(data[:,:, aee_all]), "\t", np.min(data[:,:, aee_disc]), "\t", np.min(data[:,:, aee_untext]), "\t", np.min(data[:,:, aee_art]), "\t", np.min(data[:,:, r_all]), "\t", np.min(data[:,:, r_disc]), "\t", np.min(data[:,:, r_untext]), "\t", np.min(data[:,:, r_art])

data = data_clg
print "clg", "\t", np.min(data[:,:,:, aee_all]), "\t", np.min(data[:,:,:, aee_disc]), "\t", np.min(data[:,:,:, aee_untext]), "\t", np.min(data[:,:,:, aee_art]), "\t", np.min(data[:,:,:, r_all]), "\t", np.min(data[:,:,:, r_disc]), "\t", np.min(data[:,:,:, r_untext]), "\t", np.min(data[:,:,:, r_art])

data = data_median
print "median", "\t", np.min(data[:,:,:, aee_all]), "\t", np.min(data[:,:,:, aee_disc]), "\t", np.min(data[:,:,:, aee_untext]), "\t", np.min(data[:,:,:, aee_art]), "\t", np.min(data[:,:,:, r_all]), "\t", np.min(data[:,:,:, r_disc]), "\t", np.min(data[:,:,:, r_untext]), "\t", np.min(data[:,:,:, r_art])

data = data_refine
print "refine", "\t", np.min(data[:,:,:, aee_all]), "\t", np.min(data[:,:,:, aee_disc]), "\t", np.min(data[:,:,:, aee_untext]), "\t", np.min(data[:,:,:, aee_art]), "\t", np.min(data[:,:,:, r_all]), "\t", np.min(data[:,:,:, r_disc]), "\t", np.min(data[:,:,:, r_untext]), "\t", np.min(data[:,:,:, r_art])


