import sys
import matplotlib.pyplot as plt

f2 = open('./tmp/tempP','r')
lines = f2.readlines()
f2.close()

x=[]
y=[]

if sys.argv[1]=='Thickness':
	xExtraLegend=' (nm)'

xLegend=sys.argv[1]+' '+sys.argv[2]+' '+sys.argv[3]+xExtraLegend


if sys.argv[4]=='Absorption':
	titleT=sys.argv[4]
else :
	titleT=sys.argv[4]+' '+sys.argv[5]

for line in lines:
    p=line.split()
    x.append(float(p[0]))
    y.append(float(p[1])*100)

#fig=plt.figure(figsize=(7.4,5.7),dpi=200)
fig=plt.figure(figsize=(6.85,6.7),dpi=200)
ax1=fig.add_subplot(111)

ax1.set_title(titleT,size=15)    
ax1.set_xlabel(xLegend,size=15)
ax1.set_ylabel('Power coupling ratio (%)',size=15)
ax1.plot(x,y, c='r')

leg=ax1.legend()
plt.savefig("./tmp/plot")
















