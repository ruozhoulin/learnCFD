import numpy as np
import matplotlib.pyplot as plt


# 改了函数要保存！！！！保存才能成功调用！！
## Chapter 5-The central differencing scheme of one-dimensional convection and diffusion
def central_difference(length, RHO, GAMMA, phiA, phiB, nx, u):
    deltaX = length / nx

    F = RHO * u  # F represent the convective mass flux per unit area
    D = GAMMA / deltaX  # D represent diffusion conductance at cell faces

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


## Chapter 5-The upwind differencing scheme of one-dimensional convection and diffusion
def upwind_difference(length, RHO, GAMMA, phiA, phiB, nx, u):
    deltaX = length / nx

    F = RHO * u  # F represent the convective mass flux per unit area
    D = GAMMA / deltaX  # D represent diffusion conductance at cell faces

    # initialize matrices
    A = np.zeros((nx, nx))
    B = np.zeros(nx)

    # set matrices value
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
    # solve the equation
    return np.linalg.inv(A).dot(B)


## Chapter 5-The hybrid differencing scheme of one-dimensional convection and diffusion
def hybrid_difference(length, RHO, GAMMA, phiA, phiB, nx, u):
    deltaX = length / nx

    F = RHO * u  # F represent the convective mass flux per unit area
    D = GAMMA / deltaX  # D represent diffusion conductance at cell faces
    Pe = F / D  # Peclet numbers

    if Pe < 2:
        return central_difference(length, RHO, GAMMA, phiA, phiB, nx, u)
    else:
        # Why do not you just call upwind_difference()? I think the code should be identical.
        # initialize matrices
        A = np.zeros((nx, nx))
        B = np.zeros(nx)
        for i in range(nx):
            if i == 0:
                A[i, i] = 2 * D + F
                B[i] = (2 * D + F) * phiA
            elif i == nx - 1:
                A[i, i - 1] = -F
                A[i, i] = F + 2 * D
                B[i] = 2 * D * phiB
            else:
                A[i, i - 1] = -F
                A[i, i] = F
    return np.linalg.solve(A, B)


# plot picture in Chapter 5
def plot_figure_Ch5(x, resultValue, x_range, y):
    # plt.figure() # Why do you disable this line?
    plt.scatter(x, resultValue, marker="s", facecolors="r", label="Numerical Solution")
    plt.plot(x_range, y, label="Analytical Solution")
    plt.grid(True)
    plt.ylabel("φ")
    plt.xlabel("Distance X (m)")
    plt.legend(loc="best")
    plt.show()  # maybe you should put this line in the main program, not here.
