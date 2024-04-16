import numpy as np
import matplotlib.pyplot as plt

R = np.array([1.765,2.135,2.482,2.900,3.274,3.636,4.057,4.366,4.826,5.257])
a = np.array([1.617,1.081,0.7807,0.5835,0.4591,0.3605,0.3021,0.2502,0.2093,0.1800])

def regLin(x,y):
    x2=x**2
    y2=y**2
    xy=x*y
    n=x.size

    sx=x.sum()
    sy=y.sum()
    sxy=xy.sum()
    sx2=x2.sum()
    sy2=y2.sum()

    m=(n*sxy-sx*sy)/(n*sx2-(sx**2))
    b=(sx2*sy-sx*sxy)/(n*sx2-(sx**2))
    
    r2n=n*sxy-sx*sy
    r2d1=n*sx2-(sx**2)
    r2d2=n*sy2-(sy**2)
    r2=(r2n**2) / (r2d1*r2d2)
    
    varM=abs(m)*np.sqrt( ((1/r2)-1)/(n-2) )
    varB = varM*np.sqrt(sx2/n)
    return m,b,r2,varM,varB

values = regLin(R,a)
m = values[0]
b = values[1]
r2 = values[2]
varM = values[3]
varB = values[4]

print("m = {} +/- {}".format(m,varM))
print("b = {} +/- {}".format(b,varB))
print("r^2 =", r2)

plt.xlabel("R (10^6 m)")
plt.ylabel("a (m/s^2)")
plt.plot(R,a,"o")
plt.plot(R,m*R+b)
plt.grid()
plt.show()