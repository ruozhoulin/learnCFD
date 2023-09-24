#one-dimensional convection and diffusion -hybrid differencing scheme
import numpy as np
import matplotlib.pyplot as plt


# ========================================
# basic conditions
# ========================================
length = 1.0 # unit:m
rho = 1.0    # unit:kg/m^3
gamma = 0.1 # unit:kg/m*s
phiA = 1
phiB = 0 # boundary condition

nx = 5
deltaX = length / nx

# =========================================
# ex5.1 Case2:u = 2.5 m/s
# ========================================= 
u = 2.5
#F and D to represent the convective mass flux per unit area and diffusion conductance at cell faces
nx = 5
deltaX = length / nx
F = rho * u
D = gamma / deltaX

A1 = np.zeros((nx, nx))
B1 = np.zeros(nx)

for i in range(nx):
    if i == 0:
        A1[i, i] = 2*D + F 
        B1[i] = (2 * D + F) * phiA
    elif i == nx - 1:
        A1[i, i - 1] = -F
        A1[i, i] = F +2*D 
        B1[i] = 2 * D  * phiB
    else:
        A1[i, i - 1] = -F
        A1[i,i] = F

ResultValue1 = np.linalg.solve(A1,B1)


# =========================================
# ex5.1 Case3:u = 2.5 m/s  grid 20
# ========================================= 

u = 2.5
nx = 20
deltaX = length / nx

F = rho * u
D = gamma / deltaX

A2 = np.zeros((nx, nx))
B2 = np.zeros(nx)

for i in range(nx):
    if i == 0:
        A2[i, i + 1] = 0.5 * F -D
        A2[i, i] = 3*D + 0.5*F 
        B2[i] = (2 * D + F) * phiA
    elif i == nx - 1:
        A2[i, i - 1] = -D -0.5*F
        A2[i, i] = 3*D-0.5*F 
        B2[i] = (2 * D - F) * phiB
    else:
        A2[i, i - 1] = -D - 0.5*F
        A2[i, i + 1] = 0.5*F -D  
        A2[i, i] = 2 * D

ResultValue2 = np.linalg.inv(A2).dot(B2)


############          plot  picture          #################################################################
x1 = np.array([0.1, 0.3, 0.5,0.7,0.9])
x2 = np.arange(0.025,1.0,0.05)
plt.scatter(x1, ResultValue1, marker='o', facecolors='r', label='Numerical Solution 5 cells')
plt.scatter(x2, ResultValue2, marker='s', facecolors='y', label='Numerical Solution 20 cells')
plt.title('5.3 Comparison of the numerical result with the analytical solution ', fontname='Arial', fontsize=12)
x_range = np.arange(0, 1.0, 0.001)
# define
y = 1+((1 - np.exp(25*x_range))/(7.2*10**10)) # math.np只能单个数字，矩阵用np
plt.plot(x_range, y, label='Analytical Solution')
plt.grid(True)
plt.ylabel('φ')
max_y = np.max(ResultValue1) + 0.2
plt.ylim(0, max_y)
plt.yticks(np.arange(0, max_y , 0.2))
plt.gca().yaxis.set_minor_locator(plt.MultipleLocator(50))
plt.xlabel('Distance X (m)')
max_x = 1.2
plt.xlim(0, max_x)
plt.xticks(np.arange(0, max_x + 0.01, 0.2))
plt.tick_params(axis='x', length=5, width=1)
plt.gca().xaxis.set_minor_locator(plt.MultipleLocator(0.1))
plt.box(True)
plt.legend(loc='best')
plt.show()


############      这不对！！！    plot  table  !!!!!不对        #################################################################
# 创建表头和数据数组
header = ['Node', 'Distance', 'Volume ','Analytical','Difference','PercError%']
cell_style = {'fontweight': 'bold', 'fontsize': 12} 
fig, axes = plt.subplots(2, 1)
plt.subplots_adjust(hspace=0.1)
data = np.zeros((6, 6), dtype=np.dtype('U20'))
node=np.array([])
node = np.append(node, header[0])
for i in range(1, 6):
    node = np.append(node, i)
data[:,0]=node
Distance=np.array([])
Distance = np.append(Distance, header[1])
for i in range(1, 10,2):
    value = round(i / 10 , 2)
    Distance = np.append(Distance, value)
data[:,1]=Distance
Volume=np.array([])
Volume = np.append(Volume, header[2])
for i in range(0, 5):
    value = round(ResultValue1[i], 2)
    Volume = np.append(Volume, value)
data[:,2]=Volume
xRange =np.array([0.1, 0.3, 0.5, 0.7,0.9])
yRange = 20 + 80* np.cosh(5*(1-xRange))/np.cosh(5) 
analyt=np.array([])
analyt = np.append(analyt, header[3])
for i in range(0, 5):
    value = round(yRange[i], 2)
    analyt = np.append(analyt, value)
data[:,3]=analyt
Diffence=np.array([])
Diffence = np.append(Diffence, header[4])
for i in range(0, 5):
    value = round(yRange[i]-ResultValue1[i], 2)
    Diffence = np.append(Diffence, value)
data[:,4]=Diffence
PercError=np.array([])
PercError = np.append(PercError, header[5])
for i in range(0, 5):
    value = round(100*(yRange[i]-ResultValue1[i])/yRange[i], 2)
    PercError = np.append(PercError, value)
data[:,5]=PercError


axes[0].axis('off')
table =axes[0].table(cellText=data, cellLoc='center', loc='center')
 
axes[0].set_title('4.3 The numerical values of the volume integral for five partitioned regions',fontdict={'fontsize':10, 'fontweight': 'bold'})

