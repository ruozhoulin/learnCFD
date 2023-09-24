#one-dimensional source-free heat conduction
import numpy as np
import matplotlib.pyplot as plt

# use more readable variable names
# add unit of each variable
# ========================================
# basic conditions
# ========================================
nx = 5
length = 0.5  #unit: meter
k = 1000  #Thermal conductivity, unit:W/(m*k)
areaOfPipe = 0.01  # unit: m^2
temperatureA = 100  # unit: °C
temperatureB = 500  # at both ends

deltaX = length / nx

# =========================================
# Solve equations AT=B, we need T 
# ========================================= 
A = np.zeros((nx, nx))
B = np.zeros(nx)

#Q is a calculated variable for convenience
Q = k * areaOfPipe / deltaX 

for i in range(nx):
    if i == 0:
        A[i, i + 1] = -Q
        A[i, i] = 3 * Q
        B[i] = 2 * Q * temperatureA
    elif i == nx - 1:
        A[i, i - 1] = -Q
        A[i, i] = 3 * Q
        B[i] = 2 * Q * temperatureB
    else:
        A[i, i - 1] = -Q
        A[i, i + 1] = -Q
        A[i, i] = 2 * Q

T = np.linalg.inv(A).dot(B)

# =========================================================
# Plot results
# =========================================================

x = np.array([0, 0.05, 0.15, 0.25, 0.35, 0.45, 0.5])

T = np.vstack((np.array([100]), T))
T = np.vstack((T, np.array([500])))

plt.figure()
plt.scatter(x, T, marker='s', color='b')  # 绘制散点图

plt.title('4.1 Comparison of the numerical result with the analytical solution', fontname='Arial', fontsize=12)

x = np.arange(0, 0.51, 0.01)
y = 800 * x + 100

plt.plot(x, y, 'r')

plt.grid(True)

plt.ylabel('Temperature (°C)')

maxY = np.max(y) + 100
plt.ylim([0, maxY])
plt.yticks(np.arange(0, maxY + 1, 100))

ax = plt.gca()
ax.yaxis.set_tick_params(width=0.02)
ax.yaxis.set_tick_params(which='minor', width=0.02)

plt.xlabel('Distance X (m)')
maxx = np.max(x)
plt.xlim([0, maxx])
plt.xticks(np.arange(0, maxx + 0.05, 0.05))
ax.xaxis.set_tick_params(width=0.02)
ax.xaxis.set_tick_params(which='minor', width=0.02)

plt.box(True)

plt.legend(loc='lower right')
plt.show()