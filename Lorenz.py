import numpy as np
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
def dmove (Point, t, sets):
    p, r, b = sets
    x, y, z = Point
    return np.array([p*(y-x), x*(r-z)-y, x*y-b*z])
t = np.arange(0, 30, 0.001)
P1 = odeint(dmove, (0., 1., 0.), t, args=([10., 28., 2.67],))
P2 = odeint(dmove, (0., 1.01, 0.), t, args=([10., 28., 2.67],))

fig = plt.figure()
ax = Axes3D(fig)
ax.plot(P1[:,0], P1[:,1], P1[:,2], label = 'p1')
ax.plot(P2[:,0], P2[:,1], P2[:,2], label = 'p2')
plt.legend(loc = 0)
plt.show()