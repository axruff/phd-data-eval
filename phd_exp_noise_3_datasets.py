# -*- coding: utf-8 -*-
"""

Copyright 2008-2016. Karlsruhe Institute of Technology

Data evaluation scripts for benchmarking of optical flow methods on X-ray data

PhD thesis: "Automated Analysis of Time-resolved X-ray Data using Optical Flow Methods"
Author: Alexey Ershov

Fulltext link: https://publikationen.bibliothek.kit.edu/1000055519

"""

from numpy import *
from pylab import load           # warning, the load() function of numpy will be shadowed
from pylab import save
import matplotlib.pyplot as plt
import numpy as np
from pylab import *
from numpy import loadtxt


path = r"o:\\DATA\\of_experiments\\noise\\"

data_rub = loadtxt(path + r"\\rub\\phd_exp_noise_rub_table.txt")
data_hyd = loadtxt(path + r"\\hyd\\phd_exp_noise_hyd_table.txt")
data_mar = loadtxt(path + r"\\mar\\phd_exp_noise_mar_table.txt")

# Rub
aae_all1     = data_rub[:,11]
aae_disc1    = data_rub[:,12]
aae_untext1  = data_rub[:,13]

print len(aae_all1)

r05_all1     = data_rub[:,2]
r05_disc1   = data_rub[:,3]
r05_untext1  = data_rub[:,4]

r1_all1     = data_rub[:,5]
r1_disc1    = data_rub[:,6]
r1_untext1  = data_rub[:,7]

r2_all1     = data_rub[:,8]
r2_disc1    = data_rub[:,9]
r2_untext1  = data_rub[:,10]

# Hyd
aae_all2     = data_hyd[:,11]
aae_disc2    = data_hyd[:,12]
aae_untext2  = data_hyd[:,13]

r05_all2     = data_hyd[:,2]
r05_disc2   = data_hyd[:,3]
r05_untext2  = data_hyd[:,4]

r1_all2     = data_hyd[:,5]
r1_disc2    = data_hyd[:,6]
r1_untext2  = data_hyd[:,7]

r2_all2     = data_hyd[:,8]
r2_disc2    = data_hyd[:,9]
r2_untext2  = data_hyd[:,10]

# Mar
aae_all3     = data_mar[:,11]
aae_disc3    = data_mar[:,12]
aae_untext3  = data_mar[:,13]

r05_all3     = data_mar[:,2]
r05_disc3   = data_mar[:,3]
r05_untext3  = data_mar[:,4]

r1_all3     = data_mar[:,5]
r1_disc3    = data_mar[:,6]
r1_untext3  = data_mar[:,7]

r2_all3     = data_mar[:,8]
r2_disc3    = data_mar[:,9]
r2_untext3  = data_mar[:,10]


#part3 = loadtxt(path + "stat_"+ exp +"_part3_mean.txt")
#part3_mask= loadtxt(path + "stat_"+ exp +"_part3_masked_mean.txt")


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
fig, ((ax1, ax3, ax5)) = plt.subplots(1, 3)

# Figure size
fig.set_size_inches(18, 5, forward=True)

plt.subplots_adjust(bottom=0.15, top=0.9, wspace=0.275, hspace=0.3, left=0.045, right=0.989)

# Figure size


# Noise distribution sigma = 0..20 with step 0.2
t = arange(0,101)*0.2

# contrast
#t = arange(0,510,10)


ax1.grid(True, color=grey, linewidth=0.2)
ax1.plot(t, aae_all1,  color=blue, linewidth=line_width+1.0)
ax1.plot(t, aae_disc1, color=red, linestyle='--', linewidth=line_width)
ax1.plot(t, aae_disc1, color=red, linestyle='-',  linewidth=0.4)
ax1.plot(t, aae_untext1, color=green, linewidth=line_width-1.0)
ax1.set_xlabel('noise level, $\sigma$', size=label_font_size)

ax1.set_ylabel('average endpoint error, pixels', size=label_font_size)
ax1.set_title('$\mathit{RubberWhale}$', size=title_font_size)
ax1.yaxis.set_label_coords(-0.1, 0.5) # Fix spacing between label and axis


y_lables = ['{:.1f}'.format(x) for x in arange(0, 0.91, 0.1)]
y_lables[0] = ''
ax1.set_yticks(arange(0, 0.91, 0.1))
ax1.set_yticklabels(y_lables)

ax1.set_xticklabels(['{:d}'.format(x) for x in arange(0, 21, 5)])




ax3.grid(True, color=grey, linewidth=0.2)
ax3.plot(t, aae_all2,  color=blue, linewidth=line_width+1.0)
ax3.plot(t, aae_disc2, color=red, linestyle='--', linewidth=line_width)
ax3.plot(t, aae_disc2, color=red, linestyle='-',  linewidth=0.4)
ax3.plot(t, aae_untext2, color=green, linewidth=line_width-1.0)
ax3.set_xlabel(r'noise level, $\sigma$', size=label_font_size)
ax3.set_ylabel('average endpoint error, pixels', size=label_font_size)
ax3.set_title('$\mathit{Hydrangea}$', size=title_font_size)
ax3.yaxis.set_label_coords(-0.1, 0.5) # Fix spacing between label and axis

y_lables = ['{:.1f}'.format(x) for x in arange(0, 1.61, 0.2)]
y_lables[0] = ''
ax3.set_yticks(arange(0, 1.61, 0.2))
ax3.set_yticklabels(y_lables)

ax3.set_xticklabels(['{:d}'.format(x) for x in arange(0, 21, 5)])



ax5.grid(True, color=grey, linewidth=0.2)
line1, = ax5.plot(t, aae_all3,  color=blue, linewidth=line_width+1.0)
line2, = ax5.plot(t, aae_disc3, color=red, linestyle='--',  linewidth=line_width)
ax5.plot(t, aae_disc3, color=red, linestyle='-',  linewidth=0.4)
line3, = ax5.plot(t, aae_untext3, color=green, linewidth=line_width-1.0)
ax5.set_xlabel(r'noise level, $\sigma$', size=label_font_size)
ax5.set_ylabel('average endpoint error, pixels', size=label_font_size)
ax5.set_title('$\mathit{New Marble}$', size=title_font_size)
ax5.yaxis.set_label_coords(-0.1, 0.5) # Fix spacing between label and axis

y_lables = ['{:.1f}'.format(x) for x in arange(0, 0.61, 0.1)]
y_lables[0] = ''
ax5.set_yticks(arange(0, 0.61, 0.1))
ax5.set_yticklabels(y_lables)

ax5.set_xticklabels(['{:d}'.format(x) for x in arange(0, 21, 5)])


#fig.legend((ax1, ax3, ax5), ('Line 1', 'Line 2', 'Line 2'), 'upper left')

legend((line1, line2, line3), ('All', 'Disc', 'Untext'), loc='center right', fontsize=label_font_size, framealpha = 1.0)


#plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
#           ncol=2, mode="expand", borderaxespad=0.)




#ax1.set_xlim(0, 93)

#ax3.grid(True, color=grey, linewidth=0.2)
#ax3.plot(r1, color="g", linewidth=line_width)
#ax3.set_xlim(0, 93)
#ax3.set_ylim(-0.01, 0.07)

#ax2.grid(True, color=grey, linewidth=0.2)
#ax2.plot(t, r1_all1, "b", t, r1_disc1, "r", t, r1_untext1, "g", linewidth=line_width)
#ax2.set_xlabel(r'contrast level')
#ax2.set_ylabel('robust statistics % (RX 1.0)')
#
#ax4.grid(True, color=grey, linewidth=0.2)
#ax4.plot(t, r1_all2, "b", t, r1_disc2, "r", t, r1_untext2, "g", linewidth=line_width)
#ax4.set_xlabel(r'contrast level')
#ax4.set_ylabel('robust statistics % (RX 1.0)')
#
#ax6.grid(True, color=grey, linewidth=0.2)
#ax6.plot(t, r1_all3, "b", t, r1_disc3, "r", t, r1_untext3, "g", linewidth=line_width)
#ax6.set_xlabel(r'contrast level')
#ax6.set_ylabel('robust statistics % (RX 1.0)')



#ax4.grid(True, color=grey, linewidth=0.2)
#ax4.plot(r2, color="g", linewidth=line_width)
#ax4.set_xlim(0, 42)
#ax4.set_ylim(-0.01, 0.07)



plt.savefig('test.pdf')



show()