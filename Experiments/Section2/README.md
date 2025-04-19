# 实验2：Python绘图模拟非线性方程求解过程、求解Hilbert系数矩阵方程组

## 实验条件

- 计算机配置：Python 3.11.7 (tags/v3.11.7:fa7a6f2, Dec  4 2023, 19:24:49)
- CPU： Intel(R) Core(TM) i7-7660U (4) @ 4.00 GHz
- 内存大小： 15.92GB
- 操作系统： Windows 11 专业版 x86_64 WIN32_NT 10.0.22621.4317 (22H2)

## Python绘图模拟非线性方程求解过程

### 实验要求

对不动点迭代法fixPointFig.py进行修改，使得

- 图形坐标根据迭代范围缩小自动调整；
- 在图像上显示迭代序号，和对应迭代得到的值。

### 实验过程描述

#### 中文显示

为了能够在figure上显示中文，首先加入以下代码：

```python
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
```

#### 坐标调整与过程显示

```python
    plt.title(f"不动点迭代法求近似解：第 {_} 次迭代")
    plt.plot([x, x], [x, y], 'g')   # 从 (x, x) 划线到 (x, y)
    plt.annotate(f"({x}, {y})", [x, y], textcoords="offset points", xytext=(0, 10), ha="center")
```

#### 实现动态效果

```python
x_offset = x - y
y_offset = x - y
plt.xlim(x - x_offset, x + x_offset)
plt.ylim(y - x_offset, y + x_offset)
plt.plot([x, y], [y, y], 'g')   # 从 (x, y) 划线到 (y, y)
plt.pause(3)
_ += 1
```

#### **测试**

![](https://cdn.jsdelivr.net/gh/GDUTMeow/2025NumericalAnalysisWorks/Experiments/Section2/img/image-20250419150509762.png)![](https://cdn.jsdelivr.net/gh/GDUTMeow/2025NumericalAnalysisWorks/Experiments/Section2/img/image-20250419150511850.png)![](https://cdn.jsdelivr.net/gh/GDUTMeow/2025NumericalAnalysisWorks/Experiments/Section2/img/image-20250419150514199.png)![](https://cdn.jsdelivr.net/gh/GDUTMeow/2025NumericalAnalysisWorks/Experiments/Section2/img/image-20250419150516140.png)![](https://cdn.jsdelivr.net/gh/GDUTMeow/2025NumericalAnalysisWorks/Experiments/Section2/img/image-20250419150518622.png)![](https://cdn.jsdelivr.net/gh/GDUTMeow/2025NumericalAnalysisWorks/Experiments/Section2/img/image-20250419150520419.png)![](https://cdn.jsdelivr.net/gh/GDUTMeow/2025NumericalAnalysisWorks/Experiments/Section2/img/image-20250419150522876.png)![](https://cdn.jsdelivr.net/gh/GDUTMeow/2025NumericalAnalysisWorks/Experiments/Section2/img/image-20250419150524593.png)

### 实验结果及分析

![](https://cdn.jsdelivr.net/gh/GDUTMeow/2025NumericalAnalysisWorks/Experiments/Section2/img/image-20250419150533600.png)

结果讨论：

通过图的动态过程可以看出，不动点迭代法会不断接近两直线的交点，直到符合我们的精度要求时，停止迭代。此过程迭代了8次，最后得到结果为 (1.3089288992033927, 1.3089257658608728)

### 算法源代码

> 源文件：[fixPointFig.py](https://github.com/GDUTMeow/2025NumericalAnalysisWorks/blob/master/Experiments/Section2/fixPointFig.py)

```python
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

```

## 求解Hilbert系数矩阵方程组

### 实验目的

比较直接法和迭代法求解病态方程组的特点。

### 实验要求

系数矩阵为Hilbert阵，对解全为1的方程组，随着 *n* = 2, 3,……的增加，编写程序，测试和分析利用直接法和迭代法求解方程组的结果差别。

![](data:image/wmf;base64,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)          

### 实验准备

首先对Hilbert阵的病态性进行大致了解，因此先求出Hilbert阵前10阶的2-条件数。

<div align="center">表 1 前10阶Hilbert阵的2-条件数</div>

| 阶数     | 1           | 2            | 3              | 4               | 5                 |
| -------- | ----------- | ------------ | -------------- | --------------- | ----------------- |
| 2-条件数 | 1.00        | 19.28        | 524.06         | 15513.74        | 476607.25         |
| 阶数     | 6           | 7            | 8              | 9               | 10                |
| 2-条件数 | 14951058.64 | 475367356.59 | 15257575538.07 | 493153755601.22 | 16024413500363.82 |

由表 1 可知：Hilbert 阵的阶数越大，其 2-条件数 越大

<div align="center">表 2 前10阶迭代矩阵谱半径表</div>

| 阶数*n* | Jacobi迭代矩阵谱半径 | Gauss-Seidel迭代矩阵谱半径 |
| ------- | -------------------- | -------------------------- |
| 1       | 0                    | 0                          |
| 2       | 0.87                 | 0.75                       |
| 3       | 1.72                 | 0.98                       |
| 4       | 2.58                 | 1                          |
| 5       | 3.44                 | 1                          |
| 6       | 4.31                 | 1                          |
| 7       | 5.17                 | 1                          |
| 8       | 6.04                 | 1                          |
| 9       | 6.91                 | 1                          |
| 10      | 7.78                 | 1                          |

### 实验结果及分析

| 阶数n | x    | 直接法 | 迭代法（Jacobi/Gauss-Sandel） | 实际解 |
| ----- | ---- | ------ | ----------------------------- | ------ |
| 2     | x1   | 1      | 1月1日                        | 1      |
|       | x2   | 1      | 1月1日                        | 1      |
| 3     | x1   | 1      | -1E+236                       | 1      |
|       | x2   | 1      | -2.26038852E+2361  / 1.0001   | 1      |
|       | x3   | 1      | -3E+236                       | 1      |
| 4     | x1   | 1      | 发散 / 1.0019                 | 1      |
|       | x2   | 1      | 发散 / 0.9792                 | 1      |
|       | x3   | 1      | 发散 / 1.0489                 | 1      |
|       | x4   | 1      | 发散 / 0.9688                 | 1      |
| 5     | x1   | 1      | 发散 / 1.0008                 | 1      |
|       | x2   | 1      | 发散 / 0.9957                 | 1      |
|       | x3   | 1      | 发散 / 0.9939                 | 1      |
|       | x4   | 1      | 发散 / 1.0328                 | 1      |
|       | x5   | 1      | 发散 / 0.976                  | 1      |
| 6     | x1   | 1      | 发散 / 0.9993                 | 1      |
|       | x2   | 1      | 发散 / 1.0131                 | 1      |
|       | x3   | 1      | 发散 / 0.9537                 | 1      |
|       | x4   | 1      | 发散 / 1.0374                 | 1      |
|       | x5   | 1      | 发散 / 1.0296                 | 1      |
|       | x6   | 1      | 发散 / 0.9662                 | 1      |
| 7     | x1   | 1      | 发散 / 0.9981                 | 1      |
|       | x2   | 1      | 发散 / 1.0252                 | 1      |
|       | x3   | 1      | 发散 / 0.9321                 | 1      |
|       | x4   | 1      | 发散 / 1.0238                 | 1      |
|       | x5   | 1      | 发散 / 1.0485                 | 1      |
|       | x6   | 1      | 发散 / 1.0165                 | 1      |
|       | x7   | 1      | 发散 / 0.9545                 | 1      |
| 8     | x1   | 1      | 发散 / 0.9972                 | 1      |
|       | x2   | 1      | 发散 / 1.0329                 | 1      |
|       | x3   | 1      | 发散 / 0.9272                 | 1      |
|       | x4   | 1      | 发散 / 1.0024                 | 1      |
|       | x5   | 1      | 发散 / 1.0458                 | 1      |
|       | x6   | 1      | 发散 / 1.0411                 | 1      |
|       | x7   | 1      | 发散 / 1.0035                 | 1      |
|       | x8   | 1      | 发散 / 0.9479                 | 1      |
| 9     | x1   | 1      | 发散 / 0.9967                 | 1      |
|       | x2   | 1      | 发散 / 1.0344                 | 1      |
|       | x3   | 1      | 发散 / 0.9382                 | 1      |
|       | x4   | 1      | 发散 / 0.9813                 | 1      |
|       | x5   | 1      | 发散 / 1.0299                 | 1      |
|       | x6   | 1      | 发散 / 1.0458                 | 1      |
|       | x7   | 1      | 发散 / 1.0308                 | 1      |
|       | x8   | 1      | 发散 / 0.9945                 | 1      |
|       | x9   | 1      | 发散 / 0.9458                 | 1      |
| 10    | x1   | 1      | 发散 / 0.9968                 | 1      |
|       | x2   | 1      | 发散 / 1.0297                 | 1      |
|       | x3   | 1      | 发散 / 0.9612                 | 1      |
|       | x4   | 1      | 发散 / 0.9653                 | 1      |
|       | x5   | 1      | 发散 / 1.0085                 | 1      |
|       | x6   | 0.9999 | 发散 / 1.0374                 | 1      |
|       | x7   | 1.0002 | 发散 / 1.0409                 | 1      |
|       | x8   | 0.9998 | 发散 / 1.0226                 | 1      |
|       | x9   | 1.0001 | 发散 / 0.989                  | 1      |
|       | x10  | 1      | 发散 / 0.9459                 | 1      |

### 结果讨论

当n较小（即n ≤ 3）时，直接法和迭代法都能给出与实际解非常接近的结果，误差几乎为零。这是因为Hilbert矩阵的条件数较小，数值稳定性较高。迭代法的谱半径也较小，收敛迅速。

当n较大（即n ≥ 4）时，开始出现显著误差（如舍入误差），这是由于Hilbert矩阵的2-条件数急剧增加，导致矩阵病态，在使用雅可比迭代法的过程中出现了溢出错误，进而无法求解。相比之下，Gauss-Seidel迭代法表现更好，因为其谱半径始终小于等于1，确保了收敛。

在此过程中，直接法总能求得近似解， 且未出现溢出的情况。

### 算法源代码

> 源文件：[Hilbert.py](https://github.com/GDUTMeow/2025NumericalAnalysisWorks/blob/master/Experiments/Section2/Hilbert.py)

```python
from typing import List
import numpy as np
from numpy.linalg import cond, eigvals, solve

def generate_hilbert_matrix(n: int) -> np.ndarray[np.float64]:
    """
    生成 Hilbert 矩阵
    :params n: 矩阵阶数
    :return: n*n 的 Hilbert 矩阵
    """
    return np.array([[1.0 / (i + j + 1) for j in range(n)] for i in range(n)])


def spectral_radius(matrix) -> float:
    """
    计算谱半径 ρ(matrix)
    :params matrix: 矩阵
    :return: 矩阵的谱半径
    """
    eigenvalues = eigvals(matrix)
    return np.max(np.abs(eigenvalues))


def jacobi(A, b, x0, tol=1e-6, max_iter=1000) -> np.ndarray:
    """
    雅可比迭代法
    原理：x^{(k+1)} = D^{-1} (b - (L + U)x^{(k)}) 其中 D 是对角矩阵，L 和 U 分别是下三角和上三角矩阵
    :params A: 系数矩阵
    :params b: 常数向量
    :params x0: 初始值
    :params tol: 收敛容忍度
    :params max_iter: 最大迭代次数
    :return: 迭代结果
    """
    n = len(b)  # 矩阵的阶数
    D = np.diag(np.diagonal(A))  # 提取对角矩阵
    R = A - D  # L + U
    x = x0.copy()
    for _ in range(max_iter):
        x_new = np.dot(np.linalg.inv(D), b - np.dot(R, x))  # x_new = D^{-1} (b - R x)
        if np.linalg.norm(x_new - x, np.inf) < tol:
            return x_new
        x = x_new
    return x


def gauss_seidel(A, b, x0, tol=1e-6, max_iter=1000) -> np.ndarray:
    """
    高斯-赛德尔迭代法
    原理：x^{(k+1)} = D^{-1} (b - (L + U)x^{(k)}) 其中 D 是对角矩阵，L 和 U 分别是下三角和上三角矩阵
    :params A: 系数矩阵
    :params b: 常数向量
    :params x0: 初始值
    :params tol: 收敛容忍度
    :params max_iter: 最大迭代次数
    """
    n = len(b)  # 矩阵的阶数
    x = x0.copy()
    for _ in range(max_iter):
        x_new = x.copy()
        for i in range(n):
            s1 = np.dot(A[i, :i], x_new[:i])  # 下三角部分
            s2 = np.dot(A[i, i + 1 :], x[i + 1 :])  # 上三角部分
            x_new[i] = (b[i] - s1 - s2) / A[i, i]
        if np.linalg.norm(x_new - x, np.inf) < tol:
            return x_new
        x = x_new
    return x


if __name__ == "__main__":
    print("# 表1: 前10阶Hilbert阵的2-条件数")
    print("| 阶数 (n) | 2-条件数 |")
    print("|----------|----------|")
    for n in range(1, 11):
        H = generate_hilbert_matrix(n)
        cond_num = cond(H, p=2)
        print(f"| {n}        | {cond_num:.2f}     |")

    print("\n# 表2: 前10阶迭代矩阵谱半径")
    print("| 阶数 (n) | Jacobi迭代矩阵谱半径 | Gauss-Seidel迭代矩阵谱半径 |")
    print("|----------|-----------------------|-----------------------------|")
    for n in range(1, 11):
        H = generate_hilbert_matrix(n)
        D = np.diag(np.diagonal(H))
        L_plus_U = D - H  # L + U = D - A
        B_j = np.dot(np.linalg.inv(D), L_plus_U)  # Jacobi矩阵
        rho_j = spectral_radius(B_j)

        lower_tri = np.tril(H)  # 下三角矩阵（包括对角）
        U = H - lower_tri  # 严格上三角
        D_minus_L = lower_tri
        B_gs = np.dot(np.linalg.inv(D_minus_L), U)  # Gauss-Seidel矩阵
        rho_gs = spectral_radius(B_gs)

        print(
            f"| {n}        | {rho_j:.2f}                 | {rho_gs:.2f}                       |"
        )

    print("\n# 表3: 前10阶直接法与迭代法求解结果对比")
    print(
        "| 阶数 (n) | 直接法 (x1, x2, ...) | 迭代法 (Jacobi / Gauss-Seidel) | 实际解 (x1, x2, ...) |"
    )
    print(
        "|----------|-----------------------|--------------------------------|-----------------------|"
    )
    for n in range(1, 11):
        H = generate_hilbert_matrix(n)
        x_true = np.ones(n)
        b = np.dot(H, x_true)  # 计算b
        x_direct = solve(H, b)  # 直接法
        x0 = np.zeros(n)  # 初始猜测
        x_jacobi = jacobi(H, b, x0)  # Jacobi
        x_gs = gauss_seidel(H, b, x0)  # Gauss-Seidel

        print(
            f"| {n}        | {np.round(x_direct, 4)}     | Jacobi: {np.round(x_jacobi, 4)} / Gauss-Seidel: {np.round(x_gs, 4)} | {np.round(x_true, 4)}     |"
        )

```

## 参考资料

- 【Python Matplotlib 数据点标记】 https://www.cnblogs.com/chenshifu666/p/18663035
- 【矩阵的范数、谱半径和条件数】https://www.cnblogs.com/Nientse/articles/16190419.html
