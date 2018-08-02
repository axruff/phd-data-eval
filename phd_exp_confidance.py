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

data_0 = np.load(data_path + r"confidance\\hs\\numpy_data.npy")
data_1 = np.load(data_path + r"confidance\\simple\\numpy_data.npy")
data_2 = np.load(data_path + r"confidance\\robust\\numpy_data.npy")
data_3 = np.load(data_path + r"confidance\\advanced\\numpy_data.npy")
data_4 = np.load(data_path + r"confidance\\noise10\\numpy_data.npy")
data_5 = np.load(data_path + r"confidance\\noise20\\numpy_data.npy")

with open(data_path + r"confidance\\hs\\numpy_data.txt", 'r') as f:
    param_names0 = eval(f.readline())
    param_values0 = eval(f.readline())
    metric_names0 = eval(f.readline())
    
with open(data_path + r"confidance\\simple\\numpy_data.txt", 'r') as f:
    param_names1 = eval(f.readline())
    param_values1 = eval(f.readline())
    metric_names1 = eval(f.readline())
    
with open(data_path + r"confidance\\robust\\numpy_data.txt", 'r') as f:
    param_names2 = eval(f.readline())
    param_values2 = eval(f.readline())
    metric_names2 = eval(f.readline())

with open(data_path + r"confidance\\advanced\\numpy_data.txt", 'r') as f:
    param_names3 = eval(f.readline())
    param_values3 = eval(f.readline())
    metric_names3 = eval(f.readline())
    
with open(data_path + r"confidance\\noise10\\numpy_data.txt", 'r') as f:
    param_names4 = eval(f.readline())
    param_values4 = eval(f.readline())
    metric_names4 = eval(f.readline())
    
with open(data_path + r"confidance\\noise20\\numpy_data.txt", 'r') as f:
    param_names5 = eval(f.readline())
    param_values5 = eval(f.readline())
    metric_names5 = eval(f.readline())
    
    

#print grey_param_names
#print grey_param_values
#print grey_metric_names

print ""
aee = metric_names1.index("aee_all")
opp = metric_names1.index("opp")
dev = metric_names1.index("dev")
coll = metric_names1.index("coll_avg")
fbd = metric_names1.index("fbd")
bd = metric_names1.index("bd")
occ = metric_names1.index("occ_avg")

plt.rc('font', family='sans-serif')

title_font_size = 20
label_font_size = 20
ticks_font_size = 16

plt.rc('xtick', labelsize=ticks_font_size) 
plt.rc('ytick', labelsize=ticks_font_size)


line_width = 2.5


blue = (57 / 255.0, 106 / 255.0, 177 / 255.0)
red = (204/ 255.0, 37/ 255.0, 41/ 255.0 )
green = (62/ 255.0, 150/ 255.0, 81/ 255.0 )  
grey = (128/ 255.0, 133/ 255.0, 133/ 255.0 )
gold = (237/ 255.0, 218/ 255.0, 116/ 255.0 )

orange = (218/ 255.0, 124/ 255.0, 48/ 255.0 )


#fig, ((ax1, ax2)) = plt.subplots(1, 2)

start = 8
end = 100
data_0 = data_0[start:end]
values_0 = map(lambda x: float(x), param_values0[0][start:end])

start = 8
end = 80
data_1 = data_1[start:end]
values_1 = map(lambda x: float(x), param_values1[0][start:end])

start = 2
end = 50
data_2 = data_2[start:end]
values_2 = map(lambda x: float(x), param_values2[0][start:end])

start = 0
end = 50
data_3 = data_3[start:end]
values_3 = map(lambda x: float(x), param_values3[0][start:end])

start = 0
end = 140
data_4 = data_4[start:end]
values_4 = map(lambda x: float(x), param_values4[0][start:end])

start = 0
end = 140
data_5 = data_5[start:end]
values_5 = map(lambda x: float(x), param_values5[0][start:end])


print data_2[:,aee]
print values_2
v = min(data_2[:,aee])
minIndex = np.argmin(data_2[:,aee])
print minIndex
print values_2[minIndex]

print values_2[np.argmin(data_2[:,aee])]



print "Automated paramters. Closest methods"

values = values_0
data = data_0
print "HS ", "\t", values[np.argmin(data[:,aee])], "\t", values[np.argmin(data[:,dev])], "\t", values[np.argmin(data[:,opp])], "\t", values[np.argmin(data[:,fbd])]

values = values_1
data = data_1
print "Flow", "\t", values[np.argmin(data[:,aee])], "\t", values[np.argmin(data[:,dev])], "\t", values[np.argmin(data[:,opp])], "\t", values[np.argmin(data[:,fbd])]

values = values_2
data = data_2
print "baseline", "\t", values[np.argmin(data[:,aee])], "\t", values[np.argmin(data[:,dev])], "\t", values[np.argmin(data[:,opp])], "\t", values[np.argmin(data[:,fbd])]

values = values_3
data = data_3
print "median", "\t",  values[np.argmin(data[:,aee])], "\t", values[np.argmin(data[:,dev])], "\t", values[np.argmin(data[:,opp])], "\t", values[np.argmin(data[:,fbd])]

values = values_4
data = data_4
print "noise10", "\t",  values[np.argmin(data[:,aee])], "\t", values[np.argmin(data[:,dev])], "\t", values[np.argmin(data[:,opp])], "\t", values[np.argmin(data[:,fbd])]

values = values_5
data = data_5
print "noise20", "\t",  values[np.argmin(data[:,aee])], "\t", values[np.argmin(data[:,dev])], "\t", values[np.argmin(data[:,opp])], "\t", values[np.argmin(data[:,fbd])]



#values = range(0, end-start)
#print len(data_1), len(values)
#print values

plt.figure( figsize=(15, 10), facecolor='w')

plt.subplots_adjust(bottom=0.03, top=0.97, wspace=0.25, hspace=0.3, left=0.05, right=0.989)

n = 4
m = 4

i = 1

#-----------------------------------------------------------
# Horn-Schunk
#-----------------------------------------------------------
#data = data_0
#values = values_0
#plt.subplot(n,m,i)
#plt.plot(values, data[:,aee])
#plt.title("aee")
#plt.grid(False)
#plt.ylim(ymin=0.17)
#i = i + 1
#
#plt.subplot(n,m,i)
#plt.plot(values, data[:,dev])
#plt.title("dev")
#plt.grid(False)
#i = i + 1
#
#plt.subplot(n,m,i)
#plt.plot(values, data[:,opp])
#plt.title("opp")
#plt.grid(False)
#i = i + 1
#
#plt.subplot(n,m,i)
#plt.plot(values, data[:,fbd])
#plt.title("fbd")
#plt.grid(False)
#i = i + 1

#plt.subplot(n,m,i)
#plt.plot(values, data[:,coll])
#plt.title("coll")
#plt.grid(False)
#i = i + 1
#-----------------------------------------------------------
# Simple
#-----------------------------------------------------------
#data = data_1
#values = values_1
#plt.subplot(n,m,i)
#plt.plot(values, data[:,aee])
##plt.title("aee")
#plt.grid(False)
##plt.ylim(ymin=0.14)
#i = i + 1
#
#
#plt.subplot(n,m,i)
#plt.plot(values, data[:,dev])
##plt.title("dev")
#plt.grid(False)
#i = i + 1
#
#plt.subplot(n,m,i)
#plt.plot(values, data[:,opp])
##plt.title("opp")
#plt.ylim(ymin=2.05)
#plt.grid(False)
#i = i + 1
#
#plt.subplot(n,m,i)
#plt.plot(values, data[:,fbd])
##plt.title("fbd")
#plt.grid(False)
#i = i + 1

#plt.subplot(n,m,i)
#plt.plot(values, data[:,coll])
##plt.title("fbd")
#plt.grid(False)
#i = i + 1

#-----------------------------------------------------------
# Robust
#-----------------------------------------------------------
data = data_2
values = values_2
plt.subplot(n,m,i)
plt.plot(values, data[:,aee], color=blue, linewidth=line_width)
plt.title('aee (optimal)', size=title_font_size)
ylabel('baseline', size=title_font_size)
plt.grid(False)
#plt.ylim(ymin=0.14)
i = i + 1

plt.subplot(n,m,i)
plt.plot(values, data[:,dev], color=orange, linewidth=line_width)
plt.title('dev', size=title_font_size)
plt.grid(False)
i = i + 1

plt.subplot(n,m,i)
plt.plot(values, data[:,opp], color=green, linewidth=line_width)
plt.ylim(ymin=1.85)
plt.title('opp', size=title_font_size)
plt.grid(False)
i = i + 1

plt.subplot(n,m,i)
plt.plot(values, data[:,fbd], color=red, linewidth=line_width)
plt.title('fbd', size=title_font_size)
plt.grid(False)
i = i + 1
#
#plt.subplot(n,m,i)
#plt.plot(values, data[:,coll])
##plt.title("fbd")
#plt.grid(False)
#i = i + 1

#-----------------------------------------------------------
# Advanced
#-----------------------------------------------------------
data = data_3
values = values_3
plt.subplot(n,m,i)
plt.plot(values, data[:,aee], color=blue, linewidth=line_width)
ylabel('robust', size=title_font_size)
#plt.title("aee")
plt.grid(False)
#plt.ylim(ymin=0.14)
i = i + 1

plt.subplot(n,m,i)
plt.plot(values, data[:,dev], color=orange, linewidth=line_width)
#plt.title("dev")
plt.grid(False)
i = i + 1

plt.subplot(n,m,i)
plt.plot(values, data[:,opp], color=green, linewidth=line_width)
plt.ylim(ymin=2.04)
#plt.title("opp")
plt.grid(False)
i = i + 1

plt.subplot(n,m,i)
plt.plot(values, data[:,fbd], color=red, linewidth=line_width)
#plt.title("fbd")
plt.grid(False)
i = i + 1

#plt.subplot(n,m,i)
#plt.plot(values, data[:,coll])
##plt.title("fbd")
#plt.grid(False)
#i = i + 1

#-----------------------------------------------------------
# Noise10
#-----------------------------------------------------------
data = data_4
values = values_4
plt.subplot(n,m,i)
plt.plot(values, data[:,aee], color=blue, linewidth=line_width)
ylabel('noise, $\sigma=10$', size=title_font_size)
#plt.title("aee")
plt.grid(False)
#plt.ylim(ymin=0.14)
i = i + 1

plt.subplot(n,m,i)
plt.plot(values, data[:,dev], color=orange, linewidth=line_width)
#plt.title("dev")
plt.grid(False)
i = i + 1

plt.subplot(n,m,i)
plt.plot(values, data[:,opp], color=green, linewidth=line_width)
plt.ylim(ymin=10.0)
#plt.title("opp")
plt.grid(False)
i = i + 1

plt.subplot(n,m,i)
plt.plot(values, data[:,fbd], color=red, linewidth=line_width)
#plt.title("fbd")
plt.grid(False)
i = i + 1

#plt.subplot(n,m,i)
#plt.plot(values, data[:,coll])
##plt.title("fbd")
#plt.grid(False)
#i = i + 1

#-----------------------------------------------------------
# Noise20
#-----------------------------------------------------------
data = data_5
values = values_5
plt.subplot(n,m,i)
plt.plot(values, data[:,aee], color=blue, linewidth=line_width)
ylabel('noise, $\sigma=20$', size=title_font_size)
#plt.title("aee")
plt.grid(False)
#plt.ylim(ymin=0.14)
i = i + 1

plt.subplot(n,m,i)
plt.plot(values, data[:,dev], color=orange, linewidth=line_width)
#plt.title("dev")
plt.grid(False)
i = i + 1

plt.subplot(n,m,i)
plt.plot(values, data[:,opp], color=green, linewidth=line_width)
plt.ylim(ymin=19.0)
#plt.title("opp")
plt.grid(False)
i = i + 1

plt.subplot(n,m,i)
plt.plot(values, data[:,fbd], color=red, linewidth=line_width)
#plt.title("fbd")
plt.grid(False)
i = i + 1

#plt.subplot(n,m,i)
#plt.plot(values, data[:,coll])
##plt.title("fbd")
#plt.grid(False)
#i = i + 1

#plt.subplot(2,3,5)
#plt.plot(values, data_1[:,bd])
#plt.title("bd")
#plt.grid(False)

#plt.subplot(2,2,4)
#plt.plot(values, data_1[:,coll])
#plt.title("coll")
#plt.grid(False)

#plt.subplot(2,3,5)
#plt.plot(values, data_1[:,occ])
#plt.title("occ")
#plt.grid(False)

plt.savefig('exp_confidance.pdf')
















