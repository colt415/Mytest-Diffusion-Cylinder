#postprocessing for diffusion problem

from boutdata import collect
from scipy.special import jn
#from boutdata import *
#from boututils import *

import os
import subprocess

import matplotlib.pyplot as plt
from matplotlib import *
from matplotlib.backends.backend_pdf import PdfPages

import numpy as np
from numpy import *

def theoryfunction(t,r,theta):
  Ak=[2.51013,1.02088,0.639568,0.486254,0.386676,0.324663,0.278079,0.244412,0.217304,0.196143]
  Alphak=[1.69678,3.72561,6.30328,7.31689,9.08194,10.8405,12.5953,14.3478,16.0987,17.8485]
  result=0.0
  for i in range(len(Ak)):
    result=result+Ak[i]*jn(2,Alphak[i]*r)*cos(2*theta)*exp(-Alphak[i]**2*t)

  return result


T=collect('temperature', path="/home/colt/Research/BOUT/examples/Mytest-diffusion2D-Cylinder/data")

#print T.shape

#showdata(T[:,:,2,:])

#subprocess.Popen('rm *.png',shell=True)
#print T[50,33,2,:]
"""
r=np.arange(0.05,1.85,0.05)
delta=2*pi/64
theta=np.linspace(0,2*pi,64)

[R,Theta]=meshgrid(r,theta)
"""
t=np.arange(0,1.01,0.01)
print theoryfunction(0,1.0,pi)

plt.figure()

r0=0.5
theta0=0.0
plt.subplot(2,2,1)
plt.plot(t,T[:,9,2,0],'ro',t,theoryfunction(t,r0,theta0),'b',linewidth=1.5)
plt.title(r'$r_0=0.5, \theta_0=0$',fontsize=18)
plt.xlabel(r't(s)',fontsize=15)
plt.ylabel(r'$T(r_0,\theta_0,t)$',fontsize=15)
plt.legend((r'BOUT++',r'Theory'),'best',shadow=True)
plt.grid(True)

r0=0.6
theta0=pi/8
plt.subplot(2,2,2)
plt.plot(t,T[:,11,2,3],'ro',t,theoryfunction(t,r0,theta0),'b',linewidth=1.5)
plt.title(r'$r_0=0.6, \theta_0=\pi/8$',fontsize=18)
plt.xlabel(r't(s)',fontsize=15)
plt.ylabel(r'$T(r_0,\theta_0,t)$',fontsize=15)
plt.legend((r'BOUT++',r'Theory'),'best',shadow=True)
plt.grid(True)

r0=1.0
theta0=3*pi/8
plt.subplot(2,2,3)
plt.plot(t,T[:,19,2,11],'ro',t,theoryfunction(t,r0,theta0),'b',linewidth=1.5)
plt.title(r'$r_0=1.0, \theta_0=3\pi/8$',fontsize=18)
plt.xlabel(r't(s)',fontsize=15)
plt.ylabel(r'$T(r_0,\theta_0,t)$',fontsize=15)
plt.legend((r'BOUT++',r'Theory'),'best',shadow=True)
plt.grid(True)

r0=1.5
theta0=5*pi/8
plt.subplot(2,2,4)
plt.plot(t,T[:,29,2,19],'ro',t,theoryfunction(t,r0,theta0),'b',linewidth=1.5)
plt.title(r'$r_0=1.5, \theta_0=5\pi/8$',fontsize=18)
plt.xlabel(r't(s)',fontsize=15)
plt.ylabel(r'$T(r_0,\theta_0,t)$',fontsize=15)
plt.legend((r'BOUT++',r'Theory'),'best',shadow=True)
plt.grid(True)


plt.show()
"""
def theoryfunction(t,r,theta):
  Ak=[3.3438,10.459,1.25488,20.5924,25.4563]
  Alphak=[1.69678,3.72561,6.30328,7.31689,9.08194]
  result=0.0
  for i in range(len(Ak)):
    result=result+Ak[i]*jn(2,Alphak[i]*r)*cos(2*theta)*exp(-Alphak[i]**2*t)

  return result
  """
"""
plt.figure()
plt.plot(r,T[0,:,2,10])
plt.grid(True)
plt.show()
"""
"""
fig,ax=plt.subplots(subplot_kw=dict(projection='polar'))

ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)

CS=ax.contourf(Theta,R,T[0,:,2,:].T,20)
CB=fig.colorbar(CS,shrink=0.8,extend='both')
plt.title(r'Initial condition $T(r,\theta,0)=cos(2\theta)$',fontsize=18)
plt.show()
"""
"""
pp=PdfPages('Diffusion_SingleMode.pdf')

for i in range(101):
  number=str(i+1).zfill(3)
  fig,ax=plt.subplots(subplot_kw=dict(projection='polar'))

  ax.set_theta_zero_location("N")
  ax.set_theta_direction(-1)

  CS=ax.contourf(Theta,R,T[i,:,2,:].T,20)
  CB=fig.colorbar(CS,shrink=0.8,extend='both')
  plt.title(r'Initial condition $T(r,\theta,0)=cos(2\theta)  $'+ number,fontsize=15)
  plt.savefig(pp,format='pdf')

pp.close()
"""
