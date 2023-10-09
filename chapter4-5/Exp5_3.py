# ******************************************************************
# Filename: Exp5_3.py
# Author: Lin Ruozhou； Lu Shuyuan
# Creation Date : 20230926
# Introdution: An Introduction to Computational Fluid Dynamics THE FINITE VOLUME METHOD Second Edition 2007；H K Versteeg and W Malalasekera
#              Exercise of example 5.3 in P152
#              The hybrid differencing scheme of one-dimensional convection and diffusion
#              !Pe < 2, the scheme reverts to central differencing or  |Pe| > = 2 it is equivalent to upwinding for convection and setting the diffusion to zero.
# ******************************************************************
#%%
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from functions import hybrid_difference 

# ========================================
# basic conditions
# ========================================
length = 1.0  # unit:m
RHO = 1.0  # unit:kg/m^3
GAMMA = 0.1  # unit:kg/m*s
phiA = 1
phiB = 0  # boundary condition

# %%
# =========================================
# ex5.1 Case2:u = 2.5 m/s  grid 5
# =========================================
# input conditions
u = 2.5
nx = 5
# solve problem
resultValue1 = hybrid_difference(length,RHO, GAMMA, phiA, phiB,nx, u)

# %%
# =========================================
# ex5.1 Case3:u = 2.5 m/s  grid 25
# =========================================
# input conditions
u = 2.5
nx = 25
# solve problem
resultValue2 = hybrid_difference(length,RHO, GAMMA, phiA, phiB,nx, u)


# %%
############          plot  picture          ######################
x1 = np.array([0.1, 0.3, 0.5, 0.7, 0.9])
x2 = np.arange(0.02, 1.0, 0.04)
plt.figure()
plt.scatter(x2, resultValue2, marker="s", facecolors="y", label="Numerical Solution 25 cells")
plt.scatter(x1, resultValue1, marker="o", facecolors="r", label="Numerical Solution 5 cells")
plt.title("5.3 Comparison of the numerical result with the analytical solution ")
x_range = np.arange(0, 1.0, 0.001)
# define
y = 1 + ((1 - np.exp(25 * x_range)) / (7.2 * 10**10))  # math.np只能单个数字，矩阵用np
plt.plot(x_range, y, label="Analytical Solution")
plt.ylabel("φ")

plt.xlabel("Distance X (m)")
plt.legend(loc="best")
plt.show()

############          plot  table          ######################
# %%
df = pd.DataFrame()
df['Node'] = np.arange(1,6)
df['Distance'] = x1
df['Dinite volume solution'] = np.round(resultValue1,4)
df['Analytical solution'] = np.round(1 + ((1 - np.exp(25 * x1)) / (7.2 * 10**10)),4)
df['Difference'] =  np.round(df['Analytical solution']-df['Dinite volume solution'],4)
df['Percentage error']= 100*(df['Difference']/df['Analytical solution'])
#df.to_csv("exp5_3.csv")
print(df)
# %%
