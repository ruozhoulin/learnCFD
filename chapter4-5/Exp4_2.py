# ******************************************************************
# Filename: Exp4_2.py
# Author: Lin Ruozhou； Lu Shuyuan
# Creation Date : 20230917
# Introdution: An Introduction to Computational Fluid Dynamics THE FINITE VOLUME METHOD Second Edition 2007；H K Versteeg and W Malalasekera
#              Exercise of example 4.2 in P121
#              sources other than those arising from boundary conditions.
# ******************************************************************
#%%
import numpy as np
import matplotlib.pyplot as plt
from functions import plot_figure_Ch4
from functions import other_sources_heat_conduction 


# ========================================
# basic conditions
# ========================================
nx = 5
thickness = 0.02  # unit: meter
k = 0.5  # Thermal conductivity, unit:W/(m*k)
q = 10**6  # uniform heat generation, unit: W/m^3
areaOfPlate = 1
temperatureA = 100  # unit: °C
temperatureB = 200  # at both faces

deltaX = thickness / nx

# R1&R2 are calculated variables for convenience
R1 = k * areaOfPlate / deltaX
R2 = q * areaOfPlate * deltaX

resultValue = other_sources_heat_conduction(nx,R1,R2,temperatureA,temperatureB)

############### plot picture ###################
x = np.array([0.2, 0.6, 1, 1.4, 1.8])
x_range = np.arange(0, 2.1, 0.1)
y = (50 + 100 * (2 - x_range)) * x_range + 100

plot_figure_Ch4(x,resultValue, x_range, y)
plt.title("4.2 Comparison of the numerical result with the analytical solution")



plt.show()

# %%
