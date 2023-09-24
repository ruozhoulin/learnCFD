import numpy as np
import matplotlib.pyplot as plt


# change funciton name into center_difference()
def center_difference(RHO, GAMMA, nx, length, u, phiA, phiB):
    deltaX = length / nx

    # F and D to represent the convective mass flux per unit area and diffusion conductance at cell faces
    F = RHO * u
    D = GAMMA / deltaX

    # initialize matrices
    A = np.zeros((nx, nx))
    B = np.zeros(nx)

    # set matrices value
    for i in range(nx):
        if i == 0:
            A[i, i + 1] = 0.5 * F - D
            A[i, i] = 3 * D + 0.5 * F
            B[i] = (2 * D + F) * phiA
        elif i == nx - 1:
            A[i, i - 1] = -D - 0.5 * F
            A[i, i] = 3 * D - 0.5 * F
            B[i] = (2 * D - F) * phiB
        else:
            A[i, i - 1] = -D - 0.5 * F
            A[i, i + 1] = 0.5 * F - D
            A[i, i] = 2 * D

    # solve the equation
    return np.linalg.inv(A).dot(B)


# upwind

# hybrid differencing
