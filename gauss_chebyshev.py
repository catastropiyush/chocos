#Gauss Chebyshev quadrature
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    #return 1/(2+x**2)
    return 1+0.25*x*np.sin(3.14*x)
a = 0.5
b = 1.5
x_2 = [-0.7071068,0.7071068]                       ; w_2 = [1.5707963,1.5707963]
x_3 = [0.0000,0.8660254,-0.8660254]                ; w_3 = [1.0471976,1.0471976,1.047196]  
x_4 = [0.3826834,-0.3826834,0.9238795,-0.9238795]  ; w_4 = [0.7853982,0.7853982,0.7853982,0.7853982]
integral=0
N=4
if N == 1:
    integral += w_1[0]*(b-a)*0.5*(f((0.5*((b-a)*x_1[0]+(b+a)))))
elif N == 2:
  for i in range(len(x_2)):
      integral += +w_2[i]*(b-a)*0.5*(f((0.5*((b-a)*x_2[i]+(b+a)))))
elif N == 3:
  for i in range(len(x_3)):
      integral += w_3[i]*(b-a)*0.5*(f((0.5*((b-a)*x_3[i]+(b+a)))))
elif N == 4:
    for i in range(len(x_4)):
      integral += w_4[i]*(b-a)*0.5*(f((0.5*((b-a)*x_4[i]+(b+a)))))
else :
    for i in range(len(x_5)):
      integral += w_5[i]*(b-a)*0.5*(f((0.5*((b-a)*x_5[i]+(b+a)))))
print(integral)
