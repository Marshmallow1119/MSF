import numpy as np
import matplotlib.pyplot as plt

P = 283*735.4975
x0 = 0
v0 = 1
cres = 0.9
u = 0.1
A = 1.80*1.30
m = 1500

ti = 0
tf = 3*60*60+2000
dt = 0.001
n = int((tf-ti)/dt)

t = np.linspace(ti,tf,n+1)

def planoInclinado_res_1D(x0,v0,n,dt,cres,u,A,m,P,ang=0):
    x=np.empty(n+1)
    vx=np.empty(n+1)
    ax=np.empty(n+1)
    
    p_ar=1.225
    g=9.8
    
    x[0]=x0
    vx[0]=v0
    ax[0]=0
    
    for i in range(n):
        if t[i] <= 3*60*60:
            vv=np.abs(vx[i])
            ax[i]=-u*g*np.cos(ang) -(0.5*cres*A*p_ar*vx[i]*vv)/m + P/(m*vx[i])
            vx[i+1]=vx[i]+ax[i]*dt
            x[i+1]=x[i]+vx[i]*dt
        else:
            vv=np.abs(vx[i])
            ax[i]=-u*g -(0.5*cres*A*p_ar*vx[i]*vv)/m
            vx[i+1]=vx[i]+ax[i]*dt
            x[i+1]=x[i]+vx[i]*dt
    return x,vx,ax

values = planoInclinado_res_1D(x0,v0,n,dt,cres,u,A,m,P)
x = values[0]
vx = values[1]

for i in range(n):
    if (3*60*60-0.0001)<t[i]<(3*60*60+0.0001):
        xi = x[i]
        break

for i in range(n):
    if vx[i]<=0:
        xf = x[i]
        break
    
dist_percorrida = xf-xi

print("Distância percorrida:", dist_percorrida, "m")