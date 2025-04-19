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
