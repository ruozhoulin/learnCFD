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

## Chapter 5-The upwind differencing scheme without diffusion
def upwind_difference_without_diffusion(length, RHO, GAMMA, phiA, phiB, nx, u):
    deltaX = length / nx

    F = RHO * u  # F represent the convective mass flux per unit area
    D = GAMMA / deltaX  # D represent diffusion conductance at cell faces

    # initialize matrices
    A = np.zeros((nx, nx))
    B = np.zeros(nx)

    # set matrices value
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

## Chapter 5-The hybrid differencing scheme of one-dimensional convection and diffusion
def hybrid_difference(length, RHO, GAMMA, phiA, phiB, nx, u):
    deltaX = length / nx

    F = RHO * u  # F represent the convective mass flux per unit area
    D = GAMMA / deltaX  # D represent diffusion conductance at cell faces
    Pe = F / D  # Peclet numbers

    if Pe < 2:
        return central_difference(length, RHO, GAMMA, phiA, phiB, nx, u)
    else:
        return upwind_difference_without_diffusion(length, RHO, GAMMA, phiA, phiB, nx, u)


# plot picture in Chapter 5
def plot_figure_Ch5(x, resultValue, x_range, y):
    plt.figure() 
    plt.scatter(x, resultValue, marker="s", facecolors="r", label="Numerical Solution")
    plt.plot(x_range, y, label="Analytical Solution")
    plt.grid(True)
    plt.ylabel("φ")
    plt.xlabel("Distance X (m)")
    plt.legend(loc="best")

    #plt.show()  

# plot picture in Chapter 4
def plot_figure_Ch4(x1,T, x, y):
    plt.figure()
    plt.scatter(x1, T, marker="s", facecolors="r", label="Numerical Solution")

    plt.plot(x, y, label="Analytical Solution")
    plt.grid(True)
    plt.ylabel('Temperature (°C)') 
    maxY = np.max(y) + 100
    plt.ylim([0, maxY])
    plt.yticks(np.arange(0, maxY + 1, 100))
  
    plt.xlabel('Distance X (m)')
    maxx = np.max(x)
    plt.xlim([0, maxx])
   
    plt.box(True)
    plt.legend(loc='lower right') 

## Chapter4 - one dimensional steady state diffusion source_free_heat_conduction
def source_free_heat_conduction(nx, Q, temperatureA, temperatureB):

    A = np.zeros((nx, nx))
    B = np.zeros(nx)
 
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
    return np.linalg.inv(A).dot(B)

## Chapter 4 - one dimensional steady state diffusion other_sources_heat_conduction
def other_sources_heat_conduction(nx,R1,R2,temperatureA,temperatureB): 

    A = np.zeros((nx, nx))
    B = np.zeros(nx) 
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
    return np.linalg.solve(A, B)