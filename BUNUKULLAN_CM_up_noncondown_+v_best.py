#!/usr/bin/env python
# coding: utf-8

# In[14]:


import numpy as np
import numpy.linalg
import MDAnalysis
import MDAnalysis.analysis.distances
from numpy import *
from scipy.spatial import distance


# In[2]:


Path = "/media/user1/3f01b061-6b30-485c-8565-c41ef5a79485/8tb/trek2/trek2brohawn-alignment/new-trek2brohawn-mutatetrek1/trek2up/compel/prod/hlrndoneextend1microsecond/trjcat"
u = MDAnalysis.Universe(Path+"/v+centerilk.pdb",Path+"/trjcat_v+center.xtc")
timestep = 1
n_frames = len(u.trajectory)-1
start = 1


Path_down = "/media/user1/3f01b061-6b30-485c-8565-c41ef5a79485/8tb/trek2/trek2brohawn-alignment/new-trek2brohawn-mutatetrek1/trek2down/compel/prod/hlrndoneextend1microsecond/trjcat"
u_down = MDAnalysis.Universe(Path_down+"/v+centerilk.pdb",Path_down+"/down_noncond_+v_trjcat.xtc")
timestep = 1
n_frames_down = len(u_down.trajectory)-1
start = 1




# In[3]:


#Lengths to measure in the protein
length1 = u.select_atoms('(index 0:9733) and ((resname ACE and name CH3) or (resname NME and name CH3) or (resname ARG and name CZ) or (resname HIS and name CG) or (resname LYS and name NZ) or (resname ASP and name CG) or (resname GLU and name CD) or (resname SER and name OG) or (resname THR and name CB) or (resname ASN and name CG) or (resname GLN and name CD) or (resname CYS and name SG) or (resname GLY and name CA) or (resname PRO and name CG) or (resname ALA and name CB) or (resname VAL and name CB) or (resname ILE and name CB) or (resname LEU and name CG) or (resname MET and name CE) or (resname PHE and name CZ) or (resname TYR and name OH) or (resname TRP and name CE2))')
length2 = u.select_atoms('(index 0:9733) and ((resname ACE and name CH3) or (resname NME and name CH3) or (resname ARG and name CZ) or (resname HIS and name CG) or (resname LYS and name NZ) or (resname ASP and name CG) or (resname GLU and name CD) or (resname SER and name OG) or (resname THR and name CB) or (resname ASN and name CG) or (resname GLN and name CD) or (resname CYS and name SG) or (resname GLY and name CA) or (resname PRO and name CG) or (resname ALA and name CB) or (resname VAL and name CB) or (resname ILE and name CB) or (resname LEU and name CG) or (resname MET and name CE) or (resname PHE and name CZ) or (resname TYR and name OH) or (resname TRP and name CE2))')


#Lengths to measure in the protein
length3 = u_down.select_atoms('(index 0:9733) and ((resname ACE and name CH3) or (resname NME and name CH3) or (resname ARG and name CZ) or (resname HIS and name CG) or (resname LYS and name NZ) or (resname ASP and name CG) or (resname GLU and name CD) or (resname SER and name OG) or (resname THR and name CB) or (resname ASN and name CG) or (resname GLN and name CD) or (resname CYS and name SG) or (resname GLY and name CA) or (resname PRO and name CG) or (resname ALA and name CB) or (resname VAL and name CB) or (resname ILE and name CB) or (resname LEU and name CG) or (resname MET and name CE) or (resname PHE and name CZ) or (resname TYR and name OH) or (resname TRP and name CE2))')
length4 = u_down.select_atoms('(index 0:9733) and ((resname ACE and name CH3) or (resname NME and name CH3) or (resname ARG and name CZ) or (resname HIS and name CG) or (resname LYS and name NZ) or (resname ASP and name CG) or (resname GLU and name CD) or (resname SER and name OG) or (resname THR and name CB) or (resname ASN and name CG) or (resname GLN and name CD) or (resname CYS and name SG) or (resname GLY and name CA) or (resname PRO and name CG) or (resname ALA and name CB) or (resname VAL and name CB) or (resname ILE and name CB) or (resname LEU and name CG) or (resname MET and name CE) or (resname PHE and name CZ) or (resname TYR and name OH) or (resname TRP and name CE2))')








#Dimensions of matrix
dim1 = len(length1)
dim2 = len(length2)

#initialize array with zeros
contact_sum = numpy.zeros((dim1, dim2))


#Dimensions of matrix
dim3 = len(length3)
dim4 = len(length4)

#initialize array with zeros
contact_sum_down = numpy.zeros((dim3, dim4))


#Define the cut_off
cut_off = 5.0

#Above 1, Below 0 for cut_off in each timesteps
for ts in u.trajectory[start::timestep]:
	ch1 = length1.positions
	ch2 = length2.positions
	ts_dist = distance.cdist(ch1, ch2, 'euclidean')
	ts_dist[ts_dist < cut_off] = 1
	ts_dist[ts_dist > cut_off] = 0
	contact_sum = ts_dist + contact_sum	
						
contact_ratio_up = contact_sum/n_frames

for ts in u_down.trajectory[start::timestep]:
	ch3 = length3.positions
	ch4 = length4.positions
	ts_dist_down = distance.cdist(ch3, ch4, 'euclidean')
	ts_dist_down[ts_dist_down < cut_off] = 1
	ts_dist_down[ts_dist_down > cut_off] = 0
	contact_sum_down = ts_dist_down + contact_sum_down	
						
contact_ratio_down = contact_sum_down/n_frames_down

contact_ratio = contact_ratio_up - contact_ratio_down

# File to write the results
output_file = "residue_interactions.txt"

# Open the file in write mode
with open(output_file, 'w') as f:
    # Write the residue-residue interactions to the file
    for i in range(dim1):
        for j in range(dim2):
            f.write(f"Residue {i+7}-{j+7}: {contact_ratio[i, j]}\n")
        
from pylab import imshow, xlabel, ylabel, xlim, ylim, colorbar, cm, clf
import matplotlib.pyplot as plt

class Formatter(object):
    def __init__(self, im):
        self.im = im
    def __call__(self, x, y):
        z = self.im.get_array()[int(y), int(x)]
        return 'x={:.01f}, y={:.01f}, z={:.01f}'.format(x, y, z)

#set x_min and y_min to the lowest residue index (example residue 50)
cr_shape = contact_ratio.shape
x_shift = cr_shape[1]
y_shift = cr_shape[0]
x_min = 7
y_min = 7
x_max = x_min + x_shift
y_max = y_min + y_shift

#had aspect= equal
im = plt.imshow(contact_ratio, vmin=-1, vmax=1, aspect='equal', origin='lower', extent=[x_min, x_max, y_min, y_max] )

im.set_cmap('bwr')
plt.grid(b=True, color='#737373')

im.set_interpolation('nearest')
plt.format_coord = Formatter(im)
delta = 1



plt.xticks( fontsize = 20)
plt.yticks( fontsize = 20)

colorbar()
plt.show()
