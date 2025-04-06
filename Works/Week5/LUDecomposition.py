from fractions import Fraction
from typing import Union, List
from pprint import pprint
import copy

"""
使用 LU 分解法求解矩阵的值和其逆矩阵
    [2, 1, 2]
A = [1, 2, 3]
    [4, 1, 2]
"""

MATRIX = [
    [Fraction(2), Fraction(1), Fraction(2)],
    [Fraction(1), Fraction(2), Fraction(3)],
    [Fraction(4), Fraction(1), Fraction(2)],
]

matrix_inv = [  # 定义逆矩阵
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]

global_plus_times = 0  # 加法计数器
global_times = 0  # 乘法计数器

global_matrix = copy.deepcopy(MATRIX)  # 全局矩阵变量
global_l = []  # 全局 L 矩阵变量
global_u = []  # 全局 U 矩阵变量

def get_m(lidx: int, nidx: int) -> float:
    """
    计算将某行非零首元置零的系数
    :param mlidx: 行索引
    :param nidx: 列索引
    :return: 置零系数 m
    """
    global global_times
    global_times += 1  # 除法计数
    matrix_inv[nidx][lidx] = global_matrix[lidx][nidx] / global_matrix[nidx][nidx]  # 除法运算
    return matrix_inv[nidx][lidx]  # 返回置零系数 m

def position_zero(lidx: int, nidx: int) -> None:
    """
    将某行非零首元置零
    :param lidx: 行索引
    :param nidx: 列索引
    :return: None
    """
    global global_plus_times
    global global_matrix

    # 计算置零系数 m
    m = get_m(lidx, nidx)

    # 进行行变换
    for i in range(len(global_matrix[lidx])):
        global_matrix[lidx][i] -= m * global_matrix[nidx][i]  # 行变换运算
        global_plus_times += 1  # 加法计数器加一
        
        
def calculate_det_value(matrix: List[List[Union[int, float]]]) -> float:
    """
    计算行列式的值
    :param matrix: 矩阵
    :return: 行列式的值
    """
    det_value = 1.0
    for i in range(len(matrix)):
        det_value *= matrix[i][i]  # 乘法运算
    return det_value

def invert_lower_triangular(L: List[List[Fraction]]) -> List[List[Fraction]]:
    """
    计算下三角矩阵L的逆矩阵，L对角线为1
    :param L: 下三角矩阵
    :return: 逆矩阵
    """
    n = len(L)
    Linv = [[Fraction(0,1) for _ in range(n)] for _ in range(n)]
    # 对角线元素为1
    for i in range(n):
        Linv[i][i] = Fraction(1,1)
    # 逐列计算
    for j in range(n):
        for i in range(j+1, n):
            sum_val = Fraction(0,1)
            for k in range(j, i):
                sum_val += L[i][k] * Linv[k][j]
            Linv[i][j] = -sum_val
    return Linv

def invert_upper_triangular(U: List[List[Fraction]]) -> List[List[Fraction]]:
    """
    计算上三角矩阵U的逆矩阵
    :param U: 上三角矩阵
    :return: 逆矩阵
    """
    n = len(U)
    Uinv = [[Fraction(0,1) for _ in range(n)] for _ in range(n)]
    for j in range(n):
        x = [Fraction(0,1) for _ in range(n)]
        x[j] = Fraction(1,1) / U[j][j]
        for i in range(j-1, -1, -1):
            sum_val = Fraction(0,1)
            for k in range(i+1, j+1):
                sum_val += U[i][k] * x[k]
            x[i] = -sum_val / U[i][i]
        for i in range(n):
            Uinv[i][j] = x[i]
    return Uinv

def matrix_mult(a: List[List[Fraction]], b: List[List[Fraction]]) -> List[List[Fraction]]:
    """
    矩阵乘法
    :param a: 矩阵A
    :param b: 矩阵B
    :return: 矩阵乘积AB
    """
    n = len(a)
    result = [[Fraction(0,1) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += a[i][k] * b[k][j]
    return result

if __name__ == "__main__":
    print(f"\n{'='*40}\n初始矩阵:")
    for row in MATRIX:
        print(row)

    # LU 分解法求解线性方程组
    n = len(MATRIX)  # 行数

    # 初始化 L 和 U 矩阵
    global_l = [[0] * n for _ in range(n)]
    global_u = [[0] * n for _ in range(n)]

    # LU 分解过程
    for i in range(n):
        # 计算 U 矩阵的第 i 行
        for j in range(i, n):
            global_u[i][j] = global_matrix[i][j]
            if i == j:
                global_l[i][i] = 1  # 对角线元素为 1

        # 计算 L 矩阵的第 i 列
        for j in range(i + 1, n):
            global_l[j][i] = get_m(j, i)  # 获取置零系数 m
            position_zero(j, i)  # 将第 j 行的非零首元置零

    # 打印 L 和 U 矩阵
    print(f"\n{'='*40}\nL 矩阵:")
    pprint(global_l)
    print(f"\n{'='*40}\nU 矩阵:")
    pprint(global_u)

    # 打印行列式的值
    det_L_value = calculate_det_value(global_l)  # 计算 L 矩阵的行列式值
    det_U_value = calculate_det_value(global_u)  # 计算 U 矩阵的行列式值
    det_value = det_L_value * det_U_value  # 行列式的值
    print(f"\n{'='*40}\n行列式的值: {det_value}")
    
    # 计算 L 和 U 矩阵的逆矩阵
    L_inv = invert_lower_triangular(global_l)
    U_inv = invert_upper_triangular(global_u)
    
    # 计算A的逆矩阵
    A_inv = matrix_mult(U_inv, L_inv)

    # 打印A的逆矩阵
    print(f"\n{'='*40}\nA的逆矩阵:")
    for row in A_inv:
        print([e for e in row])

    # 打印运算次数统计
    print(f"\n{'='*40}\n运算次数统计:")
    print(f"乘法次数: {global_times}")
    print(f"加法次数: {global_plus_times}")
    print(f"总运算次数: {global_times + global_plus_times}")