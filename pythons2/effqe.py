import sys
import matplotlib.pyplot as plt

#f2 = open('emissionSpectrum2D-line.txt','r')
f2 = open('./tmp/tempP','r')
lines = f2.readlines()
f2.close()

x=[]
y=[]
y2=[]
y2=[]

for line in lines:
    p=line.split(' ')
    x.append(int(p[0]))
    y.append(float(p[1]))
    y2.append(float(sys.argv[1]))

#fig=plt.figure(figsize=(7.4,5.7),dpi=200)
#fig=plt.figure(figsize=(6.7,6.7),dpi=200)
fig=plt.figure(figsize=(6.85,6.7),dpi=200)
ax1=fig.add_subplot(111)

ax1.set_title("Microcavity effect",size=15)    
ax1.set_xlabel('Wavelength (nm)',size=15)
ax1.set_ylabel('Quantum efficiency',size=15)

if sys.argv[2]=='1':
	ax1.plot(x,y, c='r', label="Effective quantum efficiency")
	ax1.plot(x,y2, c='b', label="Intrinsic quantum efficiency")
if sys.argv[2]=='2':
	ax1.plot(x,y, c='r')
	ax1.plot(x,y2, c='b')

plt.ylim(float(sys.argv[1])-0.001,)

leg=ax1.legend()
plt.savefig("./tmp/plot")


