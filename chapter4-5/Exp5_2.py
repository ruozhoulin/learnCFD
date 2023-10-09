# ******************************************************************
# Filename: Exp5_2.py
# Author: Lin Ruozhou； Lu Shuyuan
# Creation Date : 20230926
# Introdution: An Introduction to Computational Fluid Dynamics THE FINITE VOLUME METHOD Second Edition 2007；H K Versteeg and W Malalasekera
#              Exercise of example 5.2 in P147
#              The upwind differencing scheme of one-dimensional convection and diffusion
# ******************************************************************
#%%
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from functions import upwind_difference 
from functions import plot_figure_Ch5 

# ========================================
# basic conditions
# ========================================
length = 1.0  # unit:m
RHO = 1.0  # unit:kg/m^3
GAMMA = 0.1  # unit:kg/m*s
phiA = 1
phiB = 0  # boundary condition

#%%
# =========================================
# Case1:u = 0.1 m/s
# =========================================
# input conditions
nx=5
u = 0.1
# solve problem
resultValue = upwind_difference(length, RHO, GAMMA, phiA, phiB, nx, u)

############### plot   picture ##############
# Numerical Solution
x = np.array([0, 0.1, 0.3, 0.5, 0.7, 0.9, 1.0])
resultValue = np.concatenate(([phiA], resultValue, [phiB]))
# Analytical Solution
x_range = np.arange(0, 1.1, 0.1)
y = (2.7183 - np.exp(x_range)) / 1.7183  # math.np只能单个数字，矩阵用np

plot_figure_Ch5(x, resultValue, x_range, y)
plt.title("5.2 Comparison of the numerical result with the analytical solution for Case1")

############          plot  table          ######################
# %%
df = pd.DataFrame()
df['Node'] = np.arange(1,6)
x1 = np.arange(0.1,1.0,0.2)
df['Distance'] = x1
df['Dinite volume solution'] = np.round(resultValue[1:6],4)
df['Analytical solution'] =np.round((2.7183 - np.exp(x1))/ 1.7183,4)
df['Difference'] =  np.round(df['Analytical solution']-df['Dinite volume solution'],4)
df['Percentage error']= 100*(df['Difference']/df['Analytical solution'])
#df.to_csv("exp5_2.csv")
print(df)

#%%
# =========================================
# Case2:u = 2.5 m/s
# =========================================
# input conditions
u = 2.5
nx = 5
# solve problem
resultValue = upwind_difference(length, RHO, GAMMA, phiA, phiB, nx, u)

############          plot            ################################
# Numerical Solution
x = np.array([0.1, 0.3, 0.5, 0.7, 0.9])
# Analytical Solution
x_range = np.arange(0, 1.0, 0.001)
y = 1 + ((1 - np.exp(25 * x_range)) / (7.2 * 10**10))

plot_figure_Ch5(x, resultValue, x_range, y)
plt.title("5.2 Comparison of the numerical result with the analytical solution for Case2")
plt.show()

############          plot  table          ######################
# %%
df = pd.DataFrame()
df['Node'] = np.arange(1,6)
df['Distance'] = x
df['Dinite volume solution'] = np.round(resultValue,4)
df['Analytical solution'] = np.round(1 + ((1 - np.exp(25 * x)) / (7.2 * 10**10)),4)
df['Difference'] =  np.round(df['Analytical solution']-df['Dinite volume solution'],4)
df['Percentage error']= 100*(df['Difference']/df['Analytical solution'])
#df.to_csv("exp5_2.csv")
print(df)
# %%
