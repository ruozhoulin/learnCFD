# ******************************************************************
# **  Filename: Exp4_1.py
# **  Author: Lin Ruozhou； Lu Shuyuan
# **  Creation Date : 20230917
# **  Introdution: An Introduction to Computational Fluid Dynamics THE FINITE VOLUME METHOD Second Edition 2007；H K Versteeg and W Malalasekera
#                  Exercise of example4.1 in P118
#                  one-dimensional source-free heat conduction in an insulated rod
# ******************************************************************
#%%
import numpy as np
import matplotlib.pyplot as plt
from functions import plot_figure_Ch4
from functions import source_free_heat_conduction
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

#Q is a calculated variable for convenience
Q = k * areaOfPipe / deltaX 
resultValue= source_free_heat_conduction(nx, Q, temperatureA, temperatureB)

######  plot  picture #####

x1 = np.array([0.05, 0.15, 0.25, 0.35, 0.45])
x = np.arange(0, 0.51, 0.01)
y = 800 * x + 100

plot_figure_Ch4(x1,resultValue, x, y)
plt.title('4.1 Comparison of the numerical result with the analytical solution')

plt.show()
# %%
