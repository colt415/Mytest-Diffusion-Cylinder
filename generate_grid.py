#generate 2-d cylindrical grid 32*65*2

from netCDF4 import Dataset
import numpy as np
from numpy import *

grid=Dataset('diffusion_cylinder.nc','w')

grid.createDimension('x',36)
grid.createDimension('y',5)

grid.createVariable('nx','i4',())
grid.createVariable('ny','i4',())
grid.variables['nx'][:]=36
grid.variables['ny'][:]=5

dx=grid.createVariable('dx','f4',('x','y',))
dy=grid.createVariable('dy','f4',('x','y',))
dx[:,:]=0.05
dy[:,:]=0.05

T=grid.createVariable('temperature','f4',('x','y',))
T[:,:]=0.0

#contravariant metric tensor

g11=grid.createVariable('g11','f4',('x','y',))
g22=grid.createVariable('g22','f4',('x','y',))
g33=grid.createVariable('g33','f4',('x','y',))
g12=grid.createVariable('g12','f4',('x','y',))
g13=grid.createVariable('g13','f4',('x','y',))
g23=grid.createVariable('g23','f4',('x','y',))

g12[:,:]=0.0
g13[:,:]=0.0
g23[:,:]=0.0

g11[:,:]=1.0
g22[:,:]=1.0

r=np.arange(0.05,1.85,0.05)
for i in range(36):
  g33[i,:]=r[i]**(-2)

grid.close()
