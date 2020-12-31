import numpy as np
import matplotlib.pyplot as plt

data_path = "../../output/#3-2/angular_intensity/output_angular_intensity_bottom.txt"
data = np.genfromtxt(data_path, unpack=True)

theta = np.linspace(0,np.pi/2, 10)
r = np.cos(theta)
r_data = data
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)
ax.set_thetamin(0)
ax.set_thetamax(90)

ax.scatter(theta, r)
ax.scatter(theta, r_data)
plt.show()
