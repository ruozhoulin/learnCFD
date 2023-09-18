import numpy as np
import matplotlib.pyplot as plt

# Please tell me how doimport numpy as np
import matplotlib.pyplot as plt

# 基本条件
nx = 5
L = 0.5  # length
k = 1000
areaOfPipe = 0.01  # 单位
Ta = 100  # temperature °C
Tb = 500

# coding style
deltaX = L / nx

# 初始化
A = np.zeros((nx, nx))
B = np.zeros((nx, 1))

Q = k * areaOfPipe / deltaX

for i in range(nx):
    if i == 0:
        A[i, i + 1] = -Q
        A[i, i] = 3 * Q
        B[i] = 2 * Q * Ta
    elif i == nx - 1:
        A[i, i - 1] = -Q
        A[i, i] = 3 * Q
        B[i] = 2 * Q * Tb
    else:
        A[i, i - 1] = -Q
        A[i, i + 1] = -Q
        A[i, i] = 2 * Q

T = np.linalg.inv(A).dot(B)

x = np.array([0, 0.05, 0.15, 0.25, 0.35, 0.45, 0.5])

T = np.vstack((np.array([100]), T))
T = np.vstack((T, np.array([500])))

plt.figure()
plt.scatter(x, T, marker='s', color='b')  # 绘制散点图

plt.title('4.1 Comparison of the numerical result with the analytical solution', fontname='Arial', fontsize=12)

x = np.arange(0, 0.51, 0.01)
y = 800 * x + 100

plt.plot(x, y, 'r')

plt.grid(True)

plt.ylabel('Temperature (°C)')

maxY = np.max(y) + 100
plt.ylim([0, maxY])
plt.yticks(np.arange(0, maxY + 1, 100))

ax = plt.gca()
ax.yaxis.set_tick_params(width=0.02)
ax.yaxis.set_tick_params(which='minor', width=0.02)

plt.xlabel('Distance X (m)')
maxx = np.max(x)
plt.xlim([0, maxx])
plt.xticks(np.arange(0, maxx + 0.05, 0.05))
ax.xaxis.set_tick_params(width=0.02)
ax.xaxis.set_tick_params(which='minor', width=0.02)

plt.box(True)

plt.legend(loc='lower right')
plt.show()
 you create this matrix
# 定义方程组的系数矩阵
A = np.array([[300, -100, 0, 0, 0],
              [-100, 200, -100, 0, 0],
              [0, -100, 200, -100, 0],
              [0, 0, -100, 200, -100],
              [0, 0, 0, -100, 300]])
# 常数向量
b = np.array([20000, 0, 0, 0, 100000])

# 线性方程求解
ResultValue = np.linalg.solve(A, b)

# 定义坐标横轴点
x = np.array([0, 0.05, 0.15, 0.25, 0.35, 0.45, 0.5])

# 把100与500添加进Ti数组(为第一个点与最后一个点）
ResultValue = np.concatenate(([100], ResultValue, [500]))

# 绘制散点图
plt.scatter(x, ResultValue, marker='s', color='blue', label='Numerical', edgecolors='black')
plt.gca().set_prop_cycle(None)

# 线性方程
# x 的变化范围
x_range = np.arange(0, 0.51, 0.01)
# Y对X的线性方程
y = 800 * x_range + 100
# 绘制线性方程
plt.plot(x_range, y, color='red', label='Exact')
# 设置图形Title 显示
plt.title('4.1 Comparison of the numerical result with the analytical solution', fontname='Arial', fontsize=12)
# 把网格显示出来
plt.grid(True)
# Y轴Caption
plt.ylabel('Temperature (C)')
# 指定Y轴最大数值
max_y = np.max(y) + 100
# 把Y轴从0 绘制到 最大数值
plt.ylim(0, max_y)
# 绘制Y 轴的 主 刻度线，间隔 100
plt.yticks(np.arange(0, max_y + 1, 100))
# 把刻度线 的长度设为10  宽度设为 2
plt.tick_params(axis='y', length=5, width=1)
# 设定次 刻度线  间隔为 50
plt.gca().yaxis.set_minor_locator(plt.MultipleLocator(50))
#绘制X 轴的Caption
plt.xlabel('Distance X (m)')
# 定制X轴的最大值
max_x = np.max(x)
# 把X轴 从0 绘制到最大值
plt.xlim(0, max_x)
# 定制X轴 主刻度
plt.xticks(np.arange(0, max_x + 0.01, 0.05))
# 把刻度线 的长度设为10  宽度设为 2
plt.tick_params(axis='x', length=5, width=1)
# 设定次 刻度线  间隔为 50
plt.gca().xaxis.set_minor_locator(plt.MultipleLocator(0.025))
# 把图形的外框绘制出来
plt.box(True)
# 把图例绘制出来
# loc='best' 图自动选择最佳位置；
# loc='upper right'：图例放置在右上角
# loc='upper left'：图例放置在左上角
# loc='lower right'：图例放置在右下角
# loc='lower left'：图例放置在左下角
# loc='center'：图例放置在中心位置
# loc='center right'：图例放置在右侧中心位置
# loc='center left'：图例放置在左侧中心位置
# loc='upper center'：图例放置在上方中心位置
# loc='lower center'：图例放置在下方中心位置
plt.legend(loc='lower right')
# 显示图形
plt.show()