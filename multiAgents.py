import numpy as np
import matplotlib.pyplot as plt

#Step Factor Initializations

rho = 1
eta = 0.01
lamda = 0.5
mu = 0.5

epsilon = 10**(-5)

#Define phi as arrays

phi1 = np.zeros((400, 1))
phi1[0] = 1
phi1[1] = 1

phi2 = np.zeros((400, 1))
phi2[0] = 1
phi2[1] = 1

phi3 = np.zeros((400, 1))
phi3[0] = 1
phi3[1] = 1

phi4 = np.zeros((400, 1))
phi4[0] = 1
phi4[1] = 1

#Input initializations
u1 = np.zeros((400, 1))
u1[0] = 1
u1[1] = 0

u2 = np.zeros((400, 1))
u2[0] = 1
u2[1] = 0

u3 = np.zeros((400, 1))
u3[0] = 1
u3[1] = 0

u4 = np.zeros((400, 1))
u4[0] = 1
u4[1] = 0

e1 = np.zeros((401, 1))
e2 = np.zeros((1001, 1))
e3 = np.zeros((1001, 1))
e4 = np.zeros((1001, 1))

# Definition of  yd and y  as arrays



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

si1 = np.zeros((400, 1))
si1[0] = 0
si1[1] = 0

si2 = np.zeros((400, 1))
si2[0] = 0
si2[1] = 0

si3 = np.zeros((400, 1))
si3[0] = 0
si3[1] = 0

si4 = np.zeros((400, 1))
si4[0] = 0
si4[1] = 0


yd = np.zeros(400)
yd[:200] = 2
yd[200:] = 0.5
    

for k in range(400):

    #Estimator
       
    if k==0 :
        phi1[0]=1
        phi2[0]=1
        phi3[0]=1
        phi4[0]=1
    elif k == 1:
       phi1[k] = phi1[k-1] + ((eta*(u1[k-1]-0)) / (mu + (u1[k-1]-0)**2)) * (y1[k]-y1[k-1] - phi1[k-1]*(u1[k-1]-0))

       phi2[k] = phi2[k-1] + ((eta*(u2[k-1]-0)) / (mu + (u2[k-1]-0)**2)) * (y2[k]-y2[k-1] - phi2[k-1]*(u2[k-1]-0))

       phi3[k] = phi3[k-1] + ((eta*(u3[k-1]-0)) / (mu + (u3[k-1]-0)**2)) * (y3[k]-y1[k-1] - phi3[k-1]*(u3[k-1]-0))

       phi1[k] = phi4[k-1] + ((eta*(u4[k-1]-0)) / (mu + (u4[k-1]-0)**2)) * (y4[k]-y4[k-1] - phi4[k-1]*(u4[k-1]-0))
    else:
       phi1[k] = phi1[k-1] + ((eta*(u1[k-1]-u1[k-2])) / (mu + (u1[k-1]-u1[k-2])**2)) * (y1[k]-y1[k-1] - phi1[k-1]*(u1[k-1]-u1[k-2]))

       phi2[k] = phi2[k-1] + ((eta*(u2[k-1]-u2[k-2])) / (mu + (u2[k-1]-u2[k-2])**2)) * (y2[k]-y2[k-1] - phi2[k-1]*(u2[k-1]-u2[k-2]))

       phi3[k] = phi3[k-1] + ((eta*(u3[k-1]-u3[k-2])) / (mu + (u3[k-1]-u3[k-2])**2)) * (y3[k]-y3[k-1] - phi3[k-1]*(u3[k-1]-u3[k-2]))

       phi2[k] = phi4[k-1] + ((eta*(u4[k-1]-u4[k-2])) / (mu + (u4[k-1]-u4[k-2])**2)) * (y4[k]-y4[k-1] - phi4[k-1]*(u4[k-1]-u4[k-2]))

    

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


    #definition of si

    if k==0:
        si1[0] = 1
        si2[0] = 1
        si3[0] = 1
        si4[0] = 1

    else:
        si1[k] = 2*yd[k] - 2*y1[k] - yd[k] + y4[k]

        si2[k] = -yd[k] + y1[k] + 2*yd[k] - 2*y2[k] - yd[k] + y3[k]

        si3[k] = -yd[k] + y2[k] + 2*yd[k] -2*y3[k]

        si4[k] = -yd[k] + y1[k] - yd[k] + y3[k] + 2*yd[k] - 2*y4[k]


    y1[k] = 0.5

    y2[k] = 2.5

    y3[k] = 3.5

    y4[k] = 4





    e1[k] = yd[k] - y1[k];

    e2[k] = yd[k] - y2[k];
    
    e3[k] = yd[k] - y3[k];
     
    e4[k] = yd[k] - y4[k];

    


plt.plot(yd,'-b')
# plt.plot(e2,'--b')
plt.show()