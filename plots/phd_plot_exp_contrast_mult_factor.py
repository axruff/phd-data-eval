# -*- coding: utf-8 -*-
"""

Copyright 2008-2016. Karlsruhe Institute of Technology

Data evaluation scripts for benchmarking of optical flow methods on X-ray data

PhD thesis: "Automated Analysis of Time-resolved X-ray Data using Optical Flow Methods"
Author: Alexey Ershov

Fulltext link: https://publikationen.bibliothek.kit.edu/1000055519

"""

from numpy import *
from pylab import load           
from pylab import save
import matplotlib.pyplot as plt
import numpy as np
from pylab import *
from numpy import loadtxt


path = r"o:\\DATA\\of_experiments\\contrast\\"

data = loadtxt(path + r"exp_contrast_terms_mult_factor.txt")

x_data = data[:,0]
y_data1 = data[:,1]
y_data2 = data[:,2]



blue = (57 / 255.0, 106 / 255.0, 177 / 255.0)
red = (204/ 255.0, 37/ 255.0, 41/ 255.0 )
green = (62/ 255.0, 150/ 255.0, 81/ 255.0 )  
grey = (128/ 255.0, 133/ 255.0, 133/ 255.0 )
gold = (237/ 255.0, 218/ 255.0, 116/ 255.0 )

line_width = 2.5

# Allow LaTeX
#plt.rc('text', usetex=True)
plt.rc('font', family='sans-serif')
#plt.rc('font', size=16)

#---------------------------
#   Fonts
#---------------------------

title_font_size = 22
label_font_size = 20
ticks_font_size = 16

plt.rc('xtick', labelsize=ticks_font_size) 
plt.rc('ytick', labelsize=ticks_font_size)



#fig, ((ax1, ax3, ax5), (ax2, ax4, ax6)) = plt.subplots(2, 3)
fig, ((ax1)) = plt.subplots(1, 1)

# Figure size
fig.set_size_inches(7, 6, forward=True)

#plt.subplots_adjust(bottom=0.15, top=0.9, wspace=0.275, hspace=0.3, left=0.045, right=0.989)



ax1.grid(True, color=grey, linewidth=0.2)
line1, = ax1.plot(x_data, y_data1,  color=blue, linewidth=line_width+1.0)
line2, = ax1.plot(x_data, y_data2,  color=red, linestyle='--', linewidth=line_width+1.0)
ax1.set_xlabel('multiplicative factor', size=label_font_size)

ax1.set_ylabel('average endpoint error, pixels', size=label_font_size)


#ax1.set_title('$\mathit{RubberWhale}$', size=title_font_size)
ax1.yaxis.set_label_coords(-0.11, 0.5) # Fix spacing between label and axis
##
##
y_lables = ['{:.2f}'.format(x) for x in arange(0.1, 0.25, 0.02)]
y_lables[0] = ''
#
#
#
ax1.set_yticks(arange(0.1, 0.25, 0.02))
ax1.set_xticks(arange(1.0, 2.2, 0.2))

ax1.set_yticklabels(y_lables)
ax1.set_xticklabels(['{:.1f}'.format(x) for x in arange(1.0, 2.2, 0.2)])

ax1.set_xlim(1.0, 2.0)

##
legend((line1, line2), ('grad', 'log'), loc='upper left', fontsize=label_font_size, framealpha = 1.0)


plt.savefig('test_scale.pdf')



show()