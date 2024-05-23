import mdtraj
import numpy as np
import sys

#insert the name of the system under investigation
target=mdtraj.load(sys.argv[1])

output= open('plumed_CA_SC.dat', 'w')

output.write("MOLINFO MOLTYPE=protein STRUCTURE="+sys.argv[1])
output.write('\n')
output.write('\n')

#to save the amount of residues forming the protein
numres=target.topology.select("name CA").shape

#to calculate the geometric center of the side chains (SC)
#the line p.shape[0] is needed in order to remove GLY
resID_nogly=[]
for i in range(0,numres[0]):
    p=target.topology.select("resid "+str(i)+" and not backbone and not (type H)")+1
    if p.shape[0]!=0:
        s="SC"+str(i+1)+": GROUP ATOMS="+str(list(p))
        output.write(s.replace("]"," ").replace("["," "))
        output.write('\n')
        resID_nogly.append(i+1)
output.write('\n')

#CV of the distances between the SCs (adjacent SC are not taken into account)
#the list resID_nogly is needed to take into account the removal of GLYs
for i in range(0,len(resID_nogly)):
    for j in range(i+2,len(resID_nogly)):
        output.write("COORDINATION GROUPA=SC"+str(resID_nogly[i])+" GROUPB=SC"+str(resID_nogly[j])+"  SWITCH={RATIONAL D_0=0.0 R_0=0.80 NN=4 MM=8}")
        output.write('\n')
output.write('\n')

#CV of the distances betwen the CAs (the 3 adjacent atoms are not taken into account)
for i in range(0,numres[0]):
    for j in range(i+4,numres[0]):
        if i!=j:
            p=target.topology.select("resid "+str(i)+" and name CA")+1
            b=target.topology.select("resid "+str(j)+" and name CA")+1
            output.write(("COORDINATION GROUPA="+str(p)+" GROUPB="+str(b)+"  SWITCH={RATIONAL D_0=0.0 R_0=0.80 NN=4 MM=8}").replace("]"," ").replace("["," "))
            output.write('\n')
