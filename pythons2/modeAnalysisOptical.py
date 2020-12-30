import sys
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches

x,y0,y10,y20,y30,y40,y50,y60,y70,y80,y90=[],[],[],[],[],[],[],[],[],[],[]

f2 = open('./tmp/tempP','r')
lines = f2.readlines()
f2.close()

if sys.argv[1]=='Thickness':
	xExtraLegend=' (nm)'
if sys.argv[1]=='Q.Y':
	xExtraLegend=' (%)'
if sys.argv[1]=='D.O':
	xExtraLegend=' (%)'
if sys.argv[1]=='Emission':
	xExtraLegend=' (nm)'
if sys.argv[1]=='EMZ':
	xExtraLegend=' (nm)'

xLegend=sys.argv[1]+' '+sys.argv[2]+' '+sys.argv[3]+xExtraLegend

for line in lines:
	p = line.split()
	x.append(float(p[0]))
	y0.append(float(p[1])*100)
	y10.append(float(p[2])*100)
	y20.append(float(p[3])*100)
	y30.append(float(p[4])*100)
	y40.append(float(p[5])*100)
	y50.append(float(p[6])*100)
	y60.append(float(p[7])*100)

fig = plt.figure(figsize=(6.85,6.7),dpi=200)
ax = fig.add_subplot(111)

ax.stackplot(x,y60,y0,y10,y20,y30,y40,y50,colors=['#FF7DFF','#FF0000','#00EAEA','#00FF00','#0000BE','#252420','#FF8000']
,edgecolors=['none','none','none','none','none','none','none'])
ax.set_title('Optical modes',size=15)
ax.set_xlabel(xLegend,size=15)
ax.set_ylabel('Power coupling ratio (%)',size=15)
ax.margins(0, 0)

if sys.argv[4]=='1':
	plt.legend([mpatches.Patch(color='#FF8000'),mpatches.Patch(color='#252420'),mpatches.Patch(color='#0000BE'),mpatches.Patch(color='#00FF00'),
	mpatches.Patch(color='#00EAEA'),mpatches.Patch(color='#FF0000'),mpatches.Patch(color='#FF7DDD')], 
           ['NR Losses','Absorption','Spp','Wave-guided','Subs-guided','Air','Air-back'])

plt.savefig("./tmp/plot")













