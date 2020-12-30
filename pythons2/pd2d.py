import sys
import matplotlib.pyplot as plt

f2 = open('./tmp/tempP','r')
lines = f2.readlines()
f2.close()

x=[]
y=[]

for line in lines:
    p=line.split(' ')
    x.append(float(p[0]))
    y.append(float(p[1]))

#fig=plt.figure(figsize=(7.4,5.7),dpi=200)
fig=plt.figure(figsize=(6.85,6.7),dpi=200)
ax1=fig.add_subplot(111)

ax1.set_title("Power Dissipation curve",size=15)
ax1.set_xlabel('Normalized in-plane wavevector ($k$$_{||}$/$k$$_{0}$)',size=15)

ax1.set_ylabel('Dissipated power',size=15)
ax1.plot(x,y, c='r', label=sys.argv[1]+' (nm)')

leg=ax1.legend()
plt.savefig("./tmp/plot")


