from __future__ import division
from __future__ import print_function

import numpy as np
import matplotlib.pyplot as plt

from matplotlib.transforms import Affine2D
from matplotlib.projections import PolarAxes
from mpl_toolkits.axisartist import angle_helper
from mpl_toolkits.axisartist.grid_finder import MaxNLocator, DictFormatter
from mpl_toolkits.axisartist.floating_axes import GridHelperCurveLinear, FloatingSubplot

r=[]
r2=[]
f2 = open('./tmp/tempP','r')
lines = f2.readlines()
f2.close()
ii=0
for line in lines:
	p = line.split()
	r.append(float(p[1]))
	r2.append(float(p[2]))
	ii=ii+1
jj=0
kk=ii
iii=0
rmax=0
for iii in range(ii):
	if int(rmax)<int(r[iii]+1):
		rmax=r[iii];

def fractional_polar_axes(f, thlim=(0, 180), rlim=(0,int(rmax+1)), step=(30, 0.5),thlabel='Angle (degree)', rlabel='Normalized intensity', ticklabels=True, theta_offset=0, rlabels = None):
    th0, th1 = thlim # deg
    r0, r1 = rlim
    thstep, rstep = step

		############################
    tr_rotate = Affine2D().translate(theta_offset, 0)
		############################
    tr_scale = Affine2D().scale(np.pi/-180., 1.)
    pa = PolarAxes
    tr = tr_rotate + tr_scale + pa.PolarTransform()
    theta_grid_locator = angle_helper.LocatorDMS((th1-th0)//thstep)
    r_grid_locator = MaxNLocator((r1-r0)//rstep)
    theta_tick_formatter = angle_helper.FormatterDMS()
		############################
    if rlabels:
        rlabels = DictFormatter(rlabels)
		############################
    grid_helper = GridHelperCurveLinear(tr,extremes=(th0, th1, r0, r1),grid_locator1=theta_grid_locator,grid_locator2=r_grid_locator,tick_formatter1=theta_tick_formatter,tick_formatter2=None)
		############################
    a = FloatingSubplot(f, 111, grid_helper=grid_helper)
    f.add_subplot(a)
		############################
    a.axis["bottom"].set_visible(False)
    a.axis["top"].set_axis_direction("top") # tick direction
    a.axis["top"].toggle(ticklabels=ticklabels, label=bool(thlabel))
    a.axis["top"].major_ticklabels.set_axis_direction("top")
    a.axis["top"].label.set_axis_direction("top")
    a.axis["top"].major_ticklabels.set_pad(5)

    a.axis["right"].set_axis_direction("bottom") # tick direction #intencity
    a.axis["left"].set_axis_direction("top") # tick direction
    a.axis["right"].toggle(ticklabels=ticklabels, label=bool(rlabel))
    # add labels:
    a.axis["top"].label.set_text(thlabel)
#    a.axis["top"].set_axis_direction("bottom")
    a.axis["right"].label.set_text(rlabel)
    auxa = a.get_aux_axes(tr)
		############################

    auxa.patch = a.patch 
    a.patch.zorder = -2

    thticks = grid_helper.grid_info['lon_info'][0]
    rticks = grid_helper.grid_info['lat_info'][0]
    #print(grid_helper.grid_info['lat_info'])
    for th in thticks[1:-1]:
        auxa.plot([th, th], [r0, r1], '--', c='grey', zorder=-1)
    for ri, r in enumerate(rticks):
        if ri == 0 and r != 0:
            ls, lw, color = 'solid', 2, 'black'
        else:
            ls, lw, color = 'dashed', 1, 'grey'
        auxa.add_artist(plt.Circle([0, 0], radius=r, ls=ls, lw=lw, color=color, fill=False,
                    transform=auxa.transData._b, zorder=-1))
    return auxa

if __name__ == '__main__':
		

		f1 = plt.figure(facecolor='white',figsize=(6.85,6.7),dpi=200)
		r_locs = [0, 2, 4, 6, 8,10]
		r_labels = ['5', '10', '15', '20', '25']
		a1 = fractional_polar_axes(f1,thlim=(0, 90),theta_offset=-90)
		#a1 = fractional_polar_axes(f1,thlim=(-90, 90),step=(10, 0.2),theta_offset=90)
		thstep = ii
		th = np.arange(0, 90+thstep, thstep)
		a1.plot(th, r, '-or',label='Intensity')
		#a1.plot(th, r, 'o')
		a1.plot(th, r2, 'b',label='Lambertion')
		a1.legend(bbox_to_anchor=(1.15, 1), loc=1, borderaxespad=0.)
		plt.savefig("./tmp/plot")
		#plt.show()



















