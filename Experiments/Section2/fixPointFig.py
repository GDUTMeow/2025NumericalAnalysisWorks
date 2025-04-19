# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
import numpy as np

def fixpt(f, x, epsilon=1.0E-5, N=500, store=False):
    y = f(x)
    n = 0
    if store:
        Values = [(x, y)]
    while abs(y-x) >= epsilon and n < N:
        x = f(x)
        n += 1
        y = f(x)
        if store:
            Values.append((x, y))
    if store:
        return y, Values
    else:
        if n >= N:
            return "No fixed point for given start value"
        else:
            return x, n, y

# define f
def f(x):
     return ((-58 * x - 3) / (7 * x ** 3 - 13 * x ** 2 - 21 * x - 12)) ** (1 / 2)

# find fixed point
res, points = fixpt(f, 1.5, store = True)
print(res, points)

# create mesh for plots
xx = np.arange(1.2, 1.6, 1e-5)

# 设置中文字体，避免表头中文变成方块
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# plot function and identity
plt.plot(xx, f(xx), 'b')
plt.plot(xx, xx, 'r')
plt.title("不动点迭代法求近似解")

_ = 1   # 迭代次数标记
# plot lines
for x, y in points:
    plt.title(f"不动点迭代法求近似解：第 {_} 次迭代")
    plt.plot([x, x], [x, y], 'g')   # 从 (x, x) 划线到 (x, y)
    plt.annotate(f"({x}, {y})", [x, y], textcoords="offset points", xytext=(0, 10), ha="center")
    x_offset = x - y
    y_offset = x - y
    plt.xlim(x - x_offset, x + x_offset)
    plt.ylim(y - x_offset, y + x_offset)
    plt.plot([x, y], [y, y], 'g')   # 从 (x, y) 划线到 (y, y)
    plt.pause(3)
    _ += 1

# show result
plt.show()
