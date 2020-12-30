import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('CIE_background.png')
#imgplot = plt.imshow(img)
#plt


f2 = open('CIE1931_coordinate.dat','r')
lines = f2.readlines()
f2.close()

f3 = open('../pythons2/tmp/tempP','r')
lines2 = f3.readlines()
f3.close()

x=[]
y=[]

t2=[]
x2=[]
y2=[]

for line in lines:
  p=line.split()
  x.append(float(p[0]))
  y.append(float(p[1]))

for line2 in lines2:
  p2=line2.split()
  t2.append(int(p2[0]))
  x2.append(float(p2[1]))
  y2.append(float(p2[2]))


t = np.arange(0.0, 1.0, 0.001)

#fig=plt.figure()

#fig = plt.figure(figsize=(7.4,5.7),dpi=200)
fig = plt.figure(figsize=(6.4,5.8),dpi=200)

ax1=fig.add_subplot(111)


#ax1.set_xscale(0,1)

ax1.set_title("CIE 1931",size=15)    
ax1.set_xlabel('Color coordinate x',size=15)
ax1.set_ylabel('Color coordinate y',size=15)
plt.ylim((0.0,0.9))
plt.xlim((0.0,0.8))


ax1.plot(x,y, c='k',linewidth=1)

colors=['b','g','r','c','m','y','k']
i=0

if sys.argv[1]=='1':
    for line2 in lines2:
        ax1.scatter(x2[i], y2[i], c=y2[i], s=3, color=colors[i%7],linewidth=1,label=t2[i])
        i=i+1

if sys.argv[1]=='2':
    for line2 in lines2:
        ax1.scatter(x2[i], y2[i], c=y2[i], s=3, color=colors[i%7],linewidth=1)
        i=i+1

leg=ax1.legend(bbox_to_anchor=(1.25, 1), loc=1, borderaxespad=0.)
ax1.imshow(img,extent=[0,1,0,1])
#plt.show()
plt.savefig("plot")
















