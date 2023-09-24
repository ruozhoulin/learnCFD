# %%
import pandas as pd

phi = [1, 2, 3, 4, 6, 1, 2, 9]
df = pd.DataFrame()
df["asdfasdf"] = phi
df["ad"] = phi

df
# %%
df.to_csv("exp5_1.csv")

# %%
# Add a header including author, date, and sources.

# one-dimensional convection and diffusion -central differencing scheme
import numpy as np
import matplotlib.pyplot as plt
from functions import center_difference

# ========================================
# basic conditions
# ========================================
length = 1.0  # unit:m
RHO = 1.0  # unit:kg/m^3
GAMMA = 0.1  # unit:kg/m*s
phiA = 1
phiB = 0  # boundary condition

nx = 5


# =========================================
# Case1:u = 0.1 m/s
# =========================================
u = 0.1
# F = rho * u
# D is ...

ResultValue = center_difference(RHO, GAMMA, nx, length, u, phiA, phiB)

############          plot  picture           #################################################################
x = np.array([0, 0.1, 0.3, 0.5, 0.7, 0.9, 1.0])
ResultValue = np.concatenate(([1.0], ResultValue, [0]))
plt.scatter(x, ResultValue, marker="s", facecolors="r", label="Numerical Solution")
plt.title(
    "5.1 Comparison of the numerical result with the analytical solution for Case1",
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
# plt.show()


# =========================================
# Case2:u = 2.5 m/s
# =========================================

u = 2.5
ResultValue = center_difference(RHO, GAMMA, nx, length, u, phiA, phiB)

############          plot   picture         #################################################################
x = np.array([0.1, 0.3, 0.5, 0.7, 0.9])
plt.scatter(x, ResultValue, marker="s", facecolors="r", label="Numerical Solution")
plt.plot(x, ResultValue, color="r")
plt.title(
    "5.1 Comparison of the numerical result with the analytical solution for Case2",
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
# plt.show()


# =========================================
# Case3:u = 2.5 m/s  grid 20
# =========================================

nx = 20
u = 2.5
ResultValue = center_difference(RHO, GAMMA, nx, length, u, phiA, phiB)

# --
x = np.arange(0.025, 1.0, 0.05)
# plot numerical solution
plt.figure()  # create a new figure
plt.plot(x, ResultValue, marker="s", label="Numerical Solution")

# plot analitical solution
x_range = np.arange(0, 1.0, 0.001)
# define
y = 1 + ((1 - np.exp(25 * x_range)) / (7.2 * 10**10))  # math.np只能单个数字，矩阵用np
plt.plot(x_range, y, label="Analytical Solution")


plt.legend(loc="best")
plt.show()

# ############          plot  picture          #################################################################
# x = np.arange(0.025, 1.0, 0.05)
# plt.scatter(x, ResultValue, marker="s", facecolors="r", label="Numerical Solution")
# plt.title(
#     "5.1 Comparison of the numerical result with the analytical solution for Case3",
#     fontname="Arial",
#     fontsize=12,
# )
# x_range = np.arange(0, 1.0, 0.001)
# # define
# y = 1 + ((1 - np.exp(25 * x_range)) / (7.2 * 10**10))  # math.np只能单个数字，矩阵用np
# plt.plot(x_range, y, label="Analytical Solution")
# plt.grid(True)
# plt.ylabel("φ")
# max_y = np.max(ResultValue) + 0.2
# plt.ylim(0, max_y)
# plt.yticks(np.arange(0, max_y, 0.2))
# plt.gca().yaxis.set_minor_locator(plt.MultipleLocator(50))
# plt.xlabel("Distance X (m)")
# max_x = 1.2
# plt.xlim(0, max_x)
# plt.xticks(np.arange(0, max_x + 0.01, 0.2))
# plt.tick_params(axis="x", length=5, width=1)
# plt.gca().xaxis.set_minor_locator(plt.MultipleLocator(0.1))
# plt.box(True)
# plt.legend(loc="best")
# plt.show()
