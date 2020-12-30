import sys
import matplotlib.pyplot as plt

#f2 = open('./tmp/emissionSpectrum2D.txt','r')
f2 = open('./tmp/tempP','r')
lines = f2.readlines()
f2.close()

x=[]
y=[]
xx=[]

waveStart=int(sys.argv[1])
waveEnd=int(sys.argv[2])
waveStep=int(sys.argv[3])

angleStart=int(sys.argv[4])
angleEnd=int(sys.argv[5])
angleStep=int(sys.argv[6])



width,height=151,10
matrix=[[0 for col in range(width)]for row in range(height)]

for line in lines:
    p=line.split()
    x.append(float(p[0]))
    y.append(float(p[2]))

for col2 in range(width):
	xx.append(x[col2])

i=0
for row in range(height):
	for col in range(width):
		matrix[row][col]=y[i]
		i=i+1

#fig=plt.figure(figsize=(7.4,5.7),dpi=200)
fig = plt.figure(figsize=(6.85,6.7),dpi=200)
ax1=fig.add_subplot(111)

ax1.set_title("Emission spectrum",size=15)    
ax1.set_xlabel('Wavelength (nm)',size=15)
ax1.set_ylabel('Intensity',size=15)

color=['b','g','r','c','m','y','k']

cc=0
for row2 in range(height):
	ax1.plot(xx,matrix[row2], c=color[cc], label=angleStart)
	angleStart=angleStart+angleStep
	cc=cc+1
	if cc==7:
		cc=0
if sys.argv[7]=='1':
	leg=ax1.legend()
plt.savefig("./tmp/plot")
















