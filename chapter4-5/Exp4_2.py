# Why do you add these lines?
# We also need a header here.


# one-dimensional heat
import numpy as np
import matplotlib.pyplot as plt


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

# =========================================
# Solve equations AT=B, we need T
# =========================================
A = np.zeros((nx, nx))
B = np.zeros(nx)

# R1&R2 are calculated variables for convenience
R1 = k * areaOfPlate / deltaX
R2 = q * areaOfPlate * deltaX

for i in range(nx):
    if i == 0:
        A[i, i + 1] = -R1
        A[i, i] = 3 * R1
        B[i] = 2 * R1 * temperatureA + R2
    elif i == nx - 1:
        A[i, i - 1] = -R1
        A[i, i] = 3 * R1
        B[i] = 2 * R1 * temperatureB + R2
    else:
        A[i, i - 1] = -R1
        A[i, i + 1] = -R1
        A[i, i] = 2 * R1
        B[i] = R2

ResultValue = np.linalg.solve(A, B)

# =========================================================
# Plot results
# =========================================================


x = np.array([0, 0.2, 0.6, 1, 1.4, 1.8, 2])

ResultValue = np.concatenate(([100], ResultValue, [200]))

plt.scatter(x, ResultValue, marker="s", facecolors="r", label="Numerical Solution")
plt.title(
    "4.2 Comparison of the numerical result with the analytical solution", fontname="Arial", fontsize=12
)

# Linear equation
# the range of x
x_range = np.arange(0, 2.1, 0.1)
# define
y = (50 + 100 * (2 - x_range)) * x_range + 100
plt.plot(x_range, y, label="Analytical Solution")

plt.grid(True)

plt.ylabel("Temperature (C)")

max_y = np.max(y) + 100

plt.ylim(0, max_y)

plt.yticks(np.arange(0, max_y + 1, 50))

plt.tick_params(axis="y", length=5, width=1)

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
