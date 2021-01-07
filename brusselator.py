from scipy import linspace
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

A, B = 1, 3

def brusselator(t, z):
    x, y = z
    return [A + x*x*y - (B+1)*x, B*x - x*x*y]

a, b = 0, 10
t = linspace(a, b, 1000)

for x0 in range(0, 6):
    for y0 in [0, 3]:
        sol = solve_ivp(brusselator, [a, b], [x0, y0], t_eval=t)
        plt.plot(sol.y[0], sol.y[1], ":", color="tab:red")
plt.xlabel('y0')
plt.ylabel('y1')
plt.show()