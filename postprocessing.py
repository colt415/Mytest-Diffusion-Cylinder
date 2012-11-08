#postprocessing for diffusion problem

from boutdata import collect
#from boutdata import *
#from boututils import *

import os
import subprocess

import matplotlib.pyplot as plt
from matplotlib import *
from matplotlib.backends.backend_pdf import PdfPages

import numpy as np
from numpy import *

T=collect('temperature', path="/home/colt/Research/BOUT/examples/Mytest-diffusion2D-Cylinder/data")

#print T.shape

#showdata(T[:,2,:,:])

#subprocess.Popen('rm *.png',shell=True)

r=np.arange(0.05,1.65,0.05)
delta=2*pi/64
theta=np.linspace(0,2*pi,64)

[R,Theta]=meshgrid(r,theta)

fig,ax=plt.subplots(subplot_kw=dict(projection='polar'))

ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)

ax.contourf(Theta,R,T[0,1,:,:].T,20)

plt.show()
