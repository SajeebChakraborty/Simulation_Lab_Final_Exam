import matplotlib.pyplot as plt
import numpy as np

dt=0.1
t=0
n=100
a=[0]*n
b=[0]*n
c=[0]*n
a[0]=100
b[0]=50
c[0]=0
k1=0.008
k2=0.002

for i in range(n-1):

    da=(k2*c[i]-k1*a[i]*b[i])*dt
    db=(k2*c[i]-k1*a[i]*b[i])*dt
    dc=(2*k1*a[i]*b[i]-2*k2*c[i])*dt

    a[i+1]= a[i] + da
    b[i+1]= b[i] + db
    c[i+1]= c[i] + dc

for i in range(n):

    print("t = {} a = {:.2f} b= {:.2f} c= {:.2f} ".format(t,a[i],b[i],c[i]))

x=np.arange(0,dt*n,dt)

plt.plot(x,a,label="a",color="red")
plt.plot(x,b,label="b",color="red")
plt.plot(x,c,label="c",color="blue")

plt.legend()

plt.show()