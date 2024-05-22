import numpy as np
import matplotlib.pyplot as plt

#Step Factor Initializations

rho = 0.01
eta = 0.01
lamda = 1
mu = 1

epsilon = 10**(-5)

#Define phi as arrays

phi1 = np.zeros((1000, 1))
phi1[0] = 1
phi1[1] = 1

phi2 = np.zeros((1000, 1))
phi2[0] = 1
phi2[1] = 1

phi3 = np.zeros((1000, 1))
phi3[0] = 1
phi3[1] = 1

phi4 = np.zeros((1000, 1))
phi4[0] = 1
phi4[1] = 1

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
        si3[0] = 1

    else:
        si1[k] = 2*yd[k] - 2*y1[k] - yd[k] + y4[k]

        si2[k] = -yd[k] + y1[k] + 2*yd[k] - 2*y2[k] - yd[k] + y3[k]

        si3[k] = -yd[k] + y2[k] + 2*yd[k] -2*y3[k]

        si4[k] = -yd[k] + y1[k] - yd[k] + y3[k] + 2*yd[k] - 2*y4[k]

    #Input 

    if k == 0:
        u1[0] = 1
        u2[0] = 1
        u3[0] = 1
        u4[0] = 1


    else:
        u1[k] = (u1[k-1]) + ((rho*phi1[k]) / (lamda + ((np.linalg.norm(phi1[k]))**2))) * (si1[k])

        u2[k] = (u2[k-1]) + ((rho*phi2[k]) / (lamda + ((np.linalg.norm(phi2[k]))**2))) * (si2[k])

        u3[k] = (u3[k-1]) + ((rho*phi3[k]) / (lamda + ((np.linalg.norm(phi3[k]))**2))) * (si3[k])

        u4[k] = (u4[k-1]) + ((rho*phi4[k]) / (lamda + ((np.linalg.norm(phi4[k]))**2))) * (si4[k])