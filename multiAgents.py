import numpy as np
import matplotlib.pyplot as plt

#Step Factor Initializations

rho = 0.01
eta = 0.01
lamda = 1
mu = 1

epsilon = 10**(-5)

#Define phi as arrays

phi = np.zeros((1000, 1))
phi[0] = 1
phi[1] = 1

#Input initializations
u1 = np.zeros((1000, 1))
u1[0] = 1
u1[1] = 1

u2 = np.zeros((1000, 1))
u2[0] = 1
u2[1] = 1

u3 = np.zeros((1000, 1))
u3[0] = 1
u3[1] = 1

u4 = np.zeros((1000, 1))
u4[0] = 1
u4[1] = 1

# Definition of  yd and y  as arrays

yd = np.zeros((1001, 1))
y = np.zeros((1001, 1))
y[0] = 0
y[1] = 0

y1 = np.zeros((1001, 1))
y1[0] = 0
y1[1] = 0

y2 = np.zeros((1001, 1))
y2[0] = 0
y2[1] = 0

y3 = np.zeros((1001, 1))
y3[0] = 0
y3[1] = 0

y4 = np.zeros((1001, 1))
y4[0] = 0
y4[1] = 0

si1 = np.zeros((1000, 1))
si1[0] = 0
si1[1] = 0

si2 = np.zeros((1000, 1))
si2[0] = 0
si2[1] = 0

si3 = np.zeros((1000, 1))
si3[0] = 0
si3[1] = 0

si4 = np.zeros((1000, 1))
si4[0] = 0
si4[1] = 0



for k in range(1000):

    #definition of si

    if k==0:
        si1[0] = 1
        si2[0] = 1

    else:
        si1[k] = 2*yd[k] - 2*y1[k] - yd[k] + y4[k]
        
        si1[k] = 2*yd[k] - 2*y1[k] - yd[k] + y4[k]

    #Input 

    if k == 0:
        u[0] = 1

    else:
        u[k] = 