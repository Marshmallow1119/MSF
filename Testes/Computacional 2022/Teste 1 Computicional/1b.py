import numpy as np
import matplotlib.pyplot as plt

t = np.array([0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5])
s = np.array([0.1, 1.4, 1.7, 6.5, 7.7, 10.4, 19.5, 26.1, 26.5, 45.9, 52.5])

logT = np.log(t)
logS = np.log(s)

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

values = regLin(logT,logS)
m = values[0]
b = values[1]
r2 = values[2]
varM = values[3]
varB = values[4]

print("m = {} +/- {}".format(m,varM))
print("b = {} +/- {}".format(b,varB))
print("r^2 =", r2)

plt.xlabel("log(t)")
plt.ylabel("log(s)")
plt.plot(logT, logS, "o")
plt.plot(logT, m*logT+b)
plt.grid()
plt.show()