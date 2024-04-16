import numpy as np
import matplotlib.pyplot as plt

k = 2
alpha = -0.1
beta = 0.02

x = np.linspace(-3,3,100)

Ep = 0.5*k*(x**2) + alpha*(x**3) - beta*(x**4)

plt.xlabel("x (m)")
plt.ylabel("Ep (J)")
plt.plot(x,Ep)
plt.grid()
plt.show()