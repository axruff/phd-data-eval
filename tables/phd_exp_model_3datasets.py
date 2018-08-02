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

data_rub_basic = np.load(data_path + r"model_comp\\4_robust\\numpy_data.npy")
data_rub_robust = np.load(data_path + r"model_comp\\7_refine\\numpy_data.npy")

data_hyd_basic = np.load(data_path + r"model_comp\\hyd\\basic\\numpy_data.npy")
data_hyd_robust = np.load(data_path + r"model_comp\\hyd\\robust\\numpy_data.npy")

data_mar_basic = np.load(data_path + r"model_comp\\mar\\basic\\numpy_data.npy")
data_mar_robust= np.load(data_path + r"model_comp\\mar\\robust\\numpy_data.npy")



#
#
with open(data_path + r"model_comp\\7_refine\\numpy_data.txt", 'r') as f:
    grey_param_names = eval(f.readline())
    grey_param_values = eval(f.readline())
    grey_metric_names = eval(f.readline())
    
with open(data_path + r"model_comp\\hyd\\basic\\numpy_data.txt", 'r') as f:
    grey_param_names2 = eval(f.readline())
    grey_param_value2s = eval(f.readline())
    grey_metric_names2 = eval(f.readline())
    
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

aee_all2 = grey_metric_names2.index("aee_all")
aee_disc2 = grey_metric_names2.index("aee_disc")
aee_untext2 = grey_metric_names2.index("aee_untext")
aee_art2 = grey_metric_names2.index("aee_art")


r_all2 = grey_metric_names2.index("R1.0_all")
r_disc2 = grey_metric_names2.index("R1.0_disc")
r_untext2 = grey_metric_names2.index("R1.0_untext")
r_art2 = grey_metric_names2.index("R1.0_art")
#
print aee_all, aee_disc, aee_untext, aee_art, r_all, r_disc, r_untext, r_art 
print aee_all2, aee_disc2, aee_untext2, aee_art2, r_all2, r_disc2, r_untext2, r_art2 



#
## Set data precision
data_rub_basic= np.around(data_rub_basic, decimals=6)
data_rub_robust= np.around(data_rub_robust, decimals=6)
data_mar_basic= np.around(data_mar_basic, decimals=6)
data_mar_robust = np.around(data_mar_robust, decimals=6)
data_hyd_basic= np.around(data_hyd_basic, decimals=6)
data_hyd_robust= np.around(data_hyd_robust, decimals=6)

data_hyd_robust[np.isnan(data_hyd_robust)] = 100000

data_hyd_robust[data_hyd_robust == 0] = 100000


data = data_rub_basic
print "rub", "\t", "basic", "\t", np.min(data[:,:, aee_all]), "\t", np.min(data[:,:, aee_disc]), "\t", np.min(data[:,:, aee_untext]), "\t", np.min(data[:,:, aee_art]), "\t", np.min(data[:,:, r_all]), "\t", np.min(data[:,:, r_disc]), "\t", np.min(data[:,:, r_untext]), "\t", np.min(data[:,:, r_art])

data = data_rub_robust
print "rub", "\t", "robust", "\t", np.min(data[:,:,:, aee_all]), "\t", np.min(data[:,:,:, aee_disc]), "\t", np.min(data[:,:,:, aee_untext]), "\t", np.min(data[:,:,:, aee_art]), "\t", np.min(data[:,:,:, r_all]), "\t", np.min(data[:,:,:, r_disc]), "\t", np.min(data[:,:,:, r_untext]), "\t", np.min(data[:,:,:, r_art])

data = data_hyd_basic
print "hyd", "\t", "basic", "\t", np.min(data[:,:, aee_all]), "\t", np.min(data[:,:, aee_disc]), "\t", np.min(data[:,:, aee_untext]), "\t", np.min(data[:,:, aee_art]), "\t", np.min(data[:,:, r_all]), "\t", np.min(data[:,:, r_disc]), "\t", np.min(data[:,:, r_untext]), "\t", np.min(data[:,:, r_art])

data = data_hyd_robust
print "hyd", "\t", "robust", "\t", np.min(data[:,:, :,:,aee_all]), "\t", np.min(data[:,:,:,:, aee_disc]), "\t", np.min(data[:,:,:,:, aee_untext]), "\t", np.min(data[:,:,:,:, aee_art]), "\t", np.min(data[:,:,:,:, r_all]), "\t", np.min(data[:,:,:,:, r_disc]), "\t", np.min(data[:,:,:,:, r_untext]), "\t", np.min(data[:,:,:,:, r_art])

data = data_mar_basic
print "mar", "\t", "basic", "\t", np.min(data[:,:, aee_all]), "\t", np.min(data[:,:, aee_disc]), "\t", np.min(data[:,:, aee_untext]), "\t", np.min(data[:,:, aee_art]), "\t", np.min(data[:,:, r_all]), "\t", np.min(data[:,:, r_disc]), "\t", np.min(data[:,:, r_untext]), "\t", np.min(data[:,:, r_art])

data = data_mar_robust
print "mar", "\t", "robust", "\t", np.min(data[:,:, :,:,aee_all]), "\t", np.min(data[:,:,:,:, aee_disc]), "\t", np.min(data[:,:,:,:, aee_untext]), "\t", np.min(data[:,:,:,:, aee_art]), "\t", np.min(data[:,:,:,:, r_all]), "\t", np.min(data[:,:,:,:, r_disc]), "\t", np.min(data[:,:,:,:, r_untext]), "\t", np.min(data[:,:,:,:, r_art])

