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

data_01 = np.load(data_path + r"smooth3\\1_alpha\\numpy_data.npy")
data_02 = np.load(data_path + r"smooth3\\1_sigma\\numpy_data.npy")
data_03 = np.load(data_path + r"smooth3\\1_rho\\numpy_data.npy")

data_1 = np.load(data_path + r"smooth3\\2_alpha_sigma\\numpy_data.npy")
data_2 = np.load(data_path + r"smooth3\\2_alpha_rho\\numpy_data.npy")
data_3 = np.load(data_path + r"smooth3\\2_sigma_rho\\numpy_data.npy")

data_4 = np.load(data_path + r"smooth3\\3_all_full\\numpy_data.npy")



with open(data_path + r"smooth3\\2_alpha_sigma\\numpy_data.txt", 'r') as f:
#with open(data_path + r"smooth3\\3_all_full\\numpy_data.txt", 'r') as f:
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



#fig, ((ax1, ax2)) = plt.subplots(1, 2)

plt.figure()

plt.subplot(1,3,1)
plt.imshow(data_1[4:50,:,aee_all], cmap="RdYlGn_r", interpolation='bicubic')
plt.title("alpha vs sigma")
plt.colorbar()
plt.grid(False)

#plt.xlabel(grey_param_names[0])
#plt.xticks(range(0, len(grey_param_values[0]), 2), grey_param_values[0][::2])

#plt.ylabel(grey_param_names[1])
#plt.yticks(grey_param_values[1])


plt.subplot(1,3,2)
plt.imshow(data_2[4:50,:,aee_all], cmap="RdYlGn_r", interpolation='bicubic')
plt.title("alpha vs rho")
plt.colorbar()
plt.grid(False)

plt.subplot(1,3,3)
plt.imshow(data_3[:,:,aee_all], cmap="RdYlGn_r", interpolation='bicubic')
plt.title("sigma vs rho")
plt.colorbar()
plt.grid(False)





# Set data precision
data_01 = np.around(data_01, decimals=3)
data_02 = np.around(data_02, decimals=3)
data_03 = np.around(data_03, decimals=3)

data_1 = np.around(data_1, decimals=3)
data_2 = np.around(data_2, decimals=3)
data_3 = np.around(data_3, decimals=3)

data_4 = np.around(data_4, decimals=3)

grey = 0
grad = 1


print "alpha       ", "\t", np.min(data_01[0, :, :,:,aee_all]), "\t", np.min(data_01[0,:, :,:,aee_disc]), "\t", np.min(data_01[0,:, :,:,aee_untext])
print "sigma       ", "\t", np.min(data_02[0, :, :,:,aee_all]), "\t", np.min(data_02[0,:, :,:,aee_disc]), "\t", np.min(data_02[0,:, :,:,aee_untext])
print "rho         ", "\t",   np.min(data_03[0, :, :,:,aee_all]), "\t", np.min(data_03[0,:, :,:,aee_disc]), "\t", np.min(data_03[0,:, :,:,aee_untext])


print "alpha, sigma", "\t",   np.min(data_1[:,:,aee_all]), "\t", np.min(data_1[:,:,aee_disc]), "\t", np.min(data_1[:,:,aee_untext])
print "alpha, rho  ", "\t",     np.min(data_2[:,:,aee_all]), "\t", np.min(data_2[:,:,aee_disc]), "\t", np.min(data_2[:,:,aee_untext])
print "sigma, rho  ", "\t",     np.min(data_3[:,:,aee_all]), "\t", np.min(data_3[:,:,aee_disc]), "\t", np.min(data_3[:,:,aee_untext])

print "all         ", "\t", np.min(data_4[:, :,:,12]), "\t", np.min(data_4[:, :,:,14]), "\t", np.min(data_4[:, :,:,15])















