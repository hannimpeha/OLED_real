import numpy as np
import sys
import matplotlib.pyplot as plt
import matplotlib.mlab as ml

if sys.argv[1]=='Thickness':
	xExtraLegend=' (nm)'
if sys.argv[1]=='Q.Y':
	xExtraLegend=' (%)'
if sys.argv[1]=='D.O':
	xExtraLegend=' (%)'
if sys.argv[1]=='EMZ':
	xExtraLegend=' (nm)'

if sys.argv[4]=='Thickness':
	yExtraLegend=' (nm)'
if sys.argv[4]=='Q.Y':
	yExtraLegend=' (%)'
if sys.argv[4]=='D.O':
	yExtraLegend=' (%)'
if sys.argv[4]=='EMZ':
	yExtraLegend=' (nm)'

ny, nx = 500,500 
x=[]
y=[]
z=[]
# Read the file. 
f2 = open('./tmp/tempP','r')
lines = f2.readlines()
f2.close()

for line in lines:
    p = line.split()
    x.append(float(p[0]))
    y.append(float(p[1]))
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

plt.figure(figsize=(7.7,6.6),dpi=200)
plt.contour(xi, yi, zi, linewidths = 0.5, colors = 'k')


plt.pcolormesh(xi, yi, zi)

plt.colorbar() 
plt.xlim(xmin, xmax)
plt.ylim(ymin, ymax)

xx=sys.argv[1]+' '+sys.argv[2]+' '+sys.argv[3]+' '+xExtraLegend
yy=sys.argv[4]+' '+sys.argv[5]+' '+sys.argv[6]+' '+yExtraLegend

if sys.argv[7]=='Absorption':
	zz=sys.argv[4]
else :
	zz=sys.argv[7]+' '+sys.argv[8]

plt.xlabel(xx,size=15)        
plt.ylabel(yy,size=15)    
plt.title(zz,size=15)
plt.savefig("./tmp/plot")









