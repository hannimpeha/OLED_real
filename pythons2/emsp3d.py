import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as ml

ny, nx = 449,449 
x=[]
y=[]
z=[]
# Read the file. 
f2 = open('./tmp/tempP','r')
lines = f2.readlines()
f2.close()

for line in lines:
    p = line.split()
    x.append(int(p[0]))
    y.append(int(p[1]))
    z.append(float(p[2]))

xmin,xmax=x[0],x[-1]
ymin,ymax=y[0],y[-1]

x = np.r_[x,xmin,xmax]
y = np.r_[y,ymax,ymin]
z = np.r_[z,z[0],z[-1]]

xi = np.linspace(xmin, xmax, nx)
yi = np.linspace(ymin, ymax, ny)
# Requires installation of natgrid
zi = ml.griddata(x, y, z, xi, yi, interp='linear')

plt.figure(figsize=(7.8,6.6),dpi=200)
plt.contour(xi, yi, zi, linewidths = 0.5, colors = 'k')
plt.pcolormesh(xi, yi, zi)

plt.colorbar() 
plt.xlim(xmin, xmax)
plt.ylim(ymin, ymax)
plt.xlabel('Angle (degree)',size=15)        
plt.ylabel('Wavelength (nm)',size=15)    
plt.title('Emission spectrum',size=15)
plt.savefig("./tmp/plot")
#plt.show()
