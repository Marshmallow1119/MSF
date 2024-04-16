import numpy as np
import matplotlib.pyplot as plt

ang = np.radians(10)
r0 = [0,2.5]
vi = 230000/3600
vx0 = vi*np.cos(ang)
vy0 = vi*np.sin(ang)
v0 = [vx0,vy0]
vT = 6.80

ti = 0
tf = 1.5
dt = 0.001
n = int((tf-ti)/dt)

t = np.linspace(ti,tf,n+1)

def resAr_2D(r0,v0,n,dt,vt):
    x=np.empty(n+1)
    y=np.empty(n+1)
    vx=np.empty(n+1)
    vy=np.empty(n+1)
    ax=np.empty(n+1)
    ay=np.empty(n+1)
    
    g=9.80
    x[0]=r0[0]
    y[0]=r0[1]
    vx[0]=v0[0]
    vy[0]=v0[1]
    ax[0]=0
    ay[0]=-g
    dres=g/vt**2
    
    for i in range(n):
        vv=np.sqrt(vx[i]**2 +vy[i]**2)

        ax[i]=-dres*vv*vx[i]
        ay[i]=-g-dres*vv*vy[i]
        
        vx[i+1]=vx[i]+ax[i]*dt
        vy[i+1]=vy[i]+ay[i]*dt
        
        x[i+1]=x[i]+vx[i]*dt
        y[i+1]=y[i]+vy[i]*dt
    return (x,y),(vx,vy),(ax,ay)

values = resAr_2D(r0,v0,n,dt,vT)
x = values[0][0]
y = values[0][1]

plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.plot(x,y)
plt.grid()
plt.show()