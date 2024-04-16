import numpy as np

y0 = 800
vy0 = 0
vT = 60
g = 9.8
D = g/(vT**2)
ti = 0
tf = 100
dt = 0.001
n = int((tf-ti)/dt)

t = np.linspace(ti,tf,n+1)

def euler(t,y0,vy0,dt,n):
    y=np.empty(n+1)
    y[0]=y0
    vy=np.empty(n+1)
    vy[0]=vy0
    for i in range(n):
        a=-g-D*abs(vy[i])*vy[i]
        vy[i+1]=vy[i]+a*dt
        y[i+1]=y[i]+vy[i]*dt
    return y,vy

values = euler(t,y0,vy0,dt,n)
y = values[0]
vy = values[1]

for i in range(n):
    if y[i]*y[i+1]<0:
        print("Tempo:", t[i])
        print("Velocidade:", vy[i])
        break