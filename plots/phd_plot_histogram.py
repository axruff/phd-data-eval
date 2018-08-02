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

#path='/Users/aleksejersov/projects/phdthesis/figures/hyd1_c_200_hist.txt'
path = r'c:\Users\fe0968\Documents\phdthesis\figures\egg_hist1.txt'

data = np.loadtxt(path)

x = np.arange(0,256)

blue = (57 / 255.0, 106 / 255.0, 177 / 255.0)
lightblue = (186 / 255.0, 201 / 255.0, 227 / 255.0)
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
fig.set_size_inches(9, 5, forward=True)

plt.subplots_adjust(bottom=0.0, top=1.0, left=0.0, right=1.0)

#ax1.grid(False, color=grey, linewidth=0.2)
ax1.plot(x, data[::1,1],  color=blue, linewidth=line_width+1.0)

ax1.fill_between(x, 0, data[::1,1], color=lightblue)

ax1.get_xaxis().set_ticks([])
ax1.get_yaxis().set_ticks([])


#ax1.vlines(data[::1,0], 0, data[::1,1], colors=blue, linestyles=u'solid')
#ax1.set_xlabel('$x$', size=label_font_size)
#ax1.set_ylabel('penalizer function $\Psi(x)$', size=label_font_size)

ax1.set_ylim(0, max(data[:,1]) + 10)
ax1.set_xlim(0, 255)

#ax1.set_title('$\mathit{RubberWhale}$', size=title_font_size)
#ax1.yaxis.set_label_coords(-0.1, 0.5) # Fix spacing between label and axis
#y_lables = ['{:.1f}'.format(x) for x in arange(0.15, 0.21, 0.01)]
#y_lables[0] = ''


#ax1.set_yticks(arange(0.15, 0.21, 0.01))
#ax1.set_yticklabels(y_lables)
#ax1.set_xticklabels(['{:.1f}'.format(x) for x in arange(0.5, 1.1, 0.1)])
#legend((line1, line2, line3), ('quadratic', 'Charbonnier', 'Lorentzian'), loc='upper center', fontsize=label_font_size, framealpha = 1.0)

plt.savefig('egg1_hist.pdf')

show()