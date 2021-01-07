import math
import numpy as np
import matplotlib.colors as colors
import matplotlib.pyplot as plt
from scipy.integrate import odeint
def Lorenz_High_Order(x,t):
    d = x0
    d[0] = sigma*x[1]
    d[1] = -x[0]*x[2]+r*x[0]
    d[N-1] = ((N-1)/2)*(x[0]*x[N-2])
    for i in range(2,N-1):
        if i%2==0:
            d[i] = ((i)/2)*x[0]*(x[i-1]-x[i+1])
        if i%2==1:
            d[i] = ((i-1)/2)*x[0]*x[i-1]-((i-1)/2+1)*x[0]*x[i+1]
    return d
N = 203
sigma=10.0
r=25.0
x0 = np.zeros(N)
x0[0] = 100
dt = 0.0001
L = 10000*dt
t = np.arange(0.0, L, dt)
x = odeint(Lorenz_High_Order, x0, t)
plt.plot(x[150], label = x)
plt.legend(loc = 0)
plt.show()