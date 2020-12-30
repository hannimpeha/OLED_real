import sys
import matplotlib.pyplot as plt

#f2 = open('emissionSpectrum2D-line.txt','r')
f2 = open('./tmp/tempP','r')
lines = f2.readlines()
f2.close()

x=[]
y=[]

for line in lines:
    p=line.split(' ')
    x.append(int(p[0]))
    y.append(float(p[1]))

#fig=plt.figure(figsize=(7.4,5.7),dpi=200)
fig = plt.figure(figsize=(6.85,6.7),dpi=200)
ax1=fig.add_subplot(111)

ax1.set_title("Emission spectrum",size=15)    
ax1.set_xlabel('Angle (degree)',size=15)
ax1.set_ylabel('Intensity',size=15)

ax1.plot(x,y, c='r', label=sys.argv[1]+' (nm)')

leg=ax1.legend()
plt.savefig("./tmp/plot")


