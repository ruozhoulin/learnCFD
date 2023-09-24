# improve this according to suggestions for previous example.
# one-dimensional convection and diffusion - using the upwind differencing scheme
import numpy as np
import matplotlib.pyplot as plt


# ========================================
# basic conditions
# ========================================
length = 1.0  # unit:m
rho = 1.0  # unit:kg/m^3
gamma = 0.1  # unit:kg/m*s
phiA = 1
phiB = 0  # boundary condition

nx = 5
deltaX = length / nx

# =========================================
# Case1:u = 0.1 m/s
# =========================================
u = 0.1
# F and D to represent the convective mass flux per unit area and diffusion conductance at cell faces
F = rho * u
D = gamma / deltaX

A = np.zeros((nx, nx))
B = np.zeros(nx)

for i in range(nx):
    if i == 0:
        A[i, i + 1] = -D
        A[i, i] = 3 * D + F
        B[i] = (2 * D + F) * phiA
    elif i == nx - 1:
        A[i, i - 1] = -D - F
        A[i, i] = 3 * D + F
        B[i] = 2 * D * phiB
    else:
        A[i, i - 1] = -D - F
        A[i, i + 1] = -D
        A[i, i] = 2 * D + F

ResultValue = np.linalg.inv(A).dot(B)

############          plot            #################################################################
x = np.array([0, 0.1, 0.3, 0.5, 0.7, 0.9, 1.0])
ResultValue = np.concatenate(([1.0], ResultValue, [0]))
plt.scatter(x, ResultValue, marker="s", facecolors="r", label="Numerical Solution 20")
plt.title(
    "5.2 Comparison of the numerical result with the analytical solution for Case1",
    fontname="Arial",
    fontsize=12,
)
x_range = np.arange(0, 1.1, 0.1)
# define
y = (2.7183 - np.exp(x_range)) / 1.7183  # math.np只能单个数字，矩阵用np
plt.plot(x_range, y, label="Analytical Solution")
plt.grid(True)
plt.ylabel("φ")
max_y = np.max(y) + 0.2
plt.ylim(0, max_y)
plt.yticks(np.arange(0, max_y, 0.2))
plt.gca().yaxis.set_minor_locator(plt.MultipleLocator(50))
plt.xlabel("Distance X (m)")
max_x = np.max(x)
plt.xlim(0, max_x)
plt.xticks(np.arange(0, max_x + 0.01, 0.2))
plt.tick_params(axis="x", length=5, width=1)
plt.gca().xaxis.set_minor_locator(plt.MultipleLocator(0.1))
plt.box(True)
plt.legend(loc="best")
plt.show()


# =========================================
# Case2:u = 2.5 m/s
# =========================================
u = 2.5
# F and D to represent the convective mass flux per unit area and diffusion conductance at cell faces
F = rho * u
D = gamma / deltaX

A = np.zeros((nx, nx))
B = np.zeros(nx)

for i in range(nx):
    if i == 0:
        A[i, i + 1] = -D
        A[i, i] = 3 * D + F
        B[i] = (2 * D + F) * phiA
    elif i == nx - 1:
        A[i, i - 1] = -D - F
        A[i, i] = 3 * D + F
        B[i] = 2 * D * phiB
    else:
        A[i, i - 1] = -D - F
        A[i, i + 1] = -D
        A[i, i] = 2 * D + F

ResultValue = np.linalg.inv(A).dot(B)

############          plot            #################################################################
x = np.array([0.1, 0.3, 0.5, 0.7, 0.9])
plt.scatter(x, ResultValue, marker="s", facecolors="r", label="Numerical Solution")

plt.title(
    "5.2 Comparison of the numerical result with the analytical solution for Case2",
    fontname="Arial",
    fontsize=12,
)
x_range = np.arange(0, 1.0, 0.001)
# define
y = 1 + ((1 - np.exp(25 * x_range)) / (7.2 * 10**10))  # math.np只能单个数字，矩阵用np
plt.plot(x_range, y, label="Analytical Solution")
plt.grid(True)
plt.ylabel("φ")
max_y = np.max(ResultValue) + 0.2
plt.ylim(0, max_y)
plt.yticks(np.arange(0, max_y, 0.2))
plt.gca().yaxis.set_minor_locator(plt.MultipleLocator(50))
plt.xlabel("Distance X (m)")
max_x = 1.2
plt.xlim(0, max_x)
plt.xticks(np.arange(0, max_x + 0.01, 0.2))
plt.tick_params(axis="x", length=5, width=1)
plt.gca().xaxis.set_minor_locator(plt.MultipleLocator(0.1))
plt.box(True)
plt.legend(loc="best")
plt.show()
