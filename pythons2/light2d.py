import sys
import matplotlib.pyplot as plt

#f2 = open('emissionSpectrum2D-line.txt','r')
f2 = open('./tmp/tempP','r')
lines = f2.readlines()
f2.close()

if sys.argv[3]=='Thickness':
	xExtraLegend=' (nm)'
if sys.argv[3]=='Q.Y':
	xExtraLegend=' (%)'
if sys.argv[3]=='D.O':
	xExtraLegend=' (%)'
if sys.argv[3]=='Emission':
	xExtraLegend=' (nm)'

x=[]
y=[]

xAxisN=sys.argv[1]+' ('+sys.argv[2]+")"

for line in lines:
    p=line.split(' ')
    x.append(int(p[0]))
    y.append(float(p[1]))

#fig=plt.figure(figsize=(7.4,5.7),dpi=200)
fig=plt.figure(figsize=(6.85,6.7),dpi=200)
ax1=fig.add_subplot(111)

xx=sys.argv[3]+' '+sys.argv[4]+' '+sys.argv[5]+' '+xExtraLegend

ax1.set_title("Current efficiency",size=15)    
ax1.set_xlabel(xx,size=15)
ax1.set_ylabel(xAxisN,size=15)
ax1.plot(x,y, c='r')

leg=ax1.legend()
plt.savefig("./tmp/plot")
#plt.show()


