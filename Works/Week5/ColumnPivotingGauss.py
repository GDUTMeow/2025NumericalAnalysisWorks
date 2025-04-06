from fractions import Fraction
from typing import Union
from pprint import pprint

"""
使用列主元高斯消元法求解线性方程组

- 6*x1 + 3*x2 + 2*x3 = 1/3
- 10*x1 + 5*x2 + 6*x3 = 0
- 8*x1 + 5*x2 + 3*x3 = 0
"""

MATRIX = [
    [6, 3, 2, Fraction(1, 3)],
    [10, 5, 6, 0],
    [8, 5, 3, 0],
]

solved = [0, 0, 0]  # 存储解的列表
global_plus_times = 0  # 加减法计数器
global_times = 0       # 乘除法计数器

def print_matrix(matrix: list, title: str) -> None:
    """带格式的矩阵打印函数
    :param matrix: 矩阵
    :param title: 打印的标题
    :return: None
    """
    print(f"\n{title}")
    for row in matrix:
        print("[", end="")
        print(", ".join([f"{x:>7}" if isinstance(x, int) else 
                        f"{x.numerator:>3}/{x.denominator:<1}" if isinstance(x, Fraction) else
                        f"{x:>7.3f}" for x in row]), end=" ]\n")

def elimination(matrix: list, base_idx: int) -> None:
    """列主元消元操作
    :param matrix: 矩阵
    :param base_idx: 基准行索引
    :return: None
    """
    global global_plus_times, global_times
    
    print_matrix(matrix, f"消元前 [第{base_idx+1}步]")

    # 列主元选择
    max_row = base_idx
    max_val = abs(matrix[base_idx][base_idx])
    for i in range(base_idx + 1, len(matrix)):
        current_val = abs(matrix[i][base_idx])
        if current_val > max_val:
            max_val = current_val
            max_row = i
    
    # 执行行交换
    if max_row != base_idx:
        matrix[base_idx], matrix[max_row] = matrix[max_row], matrix[base_idx]
        print(f"🔀 交换第{base_idx+1}行和第{max_row+1}行")

    # 消元操作
    for i in range(base_idx + 1, len(matrix)):
        # 计算行乘数
        l = matrix[i][base_idx] / matrix[base_idx][base_idx]
        global_times += 1  # 除法计数
        print(f"系数 L_{i+1}{base_idx+1} = {l:.3f}")
        
        # 执行行变换
        for j in range(base_idx, len(matrix[i])):
            matrix[i][j] -= matrix[base_idx][j] * l
            # 运算次数统计
            global_times += 1   # 乘法
            global_plus_times +=1 # 减法
    
    print_matrix(matrix, f"消元后 [第{base_idx+1}步]")

def back_substitution(matrix: list) -> None:
    """回代求解
    :param matrix: 消元后的矩阵
    :return: None
    """
    global global_plus_times, global_times
    
    print("\n" + "="*40 + "\n开始回代求解:")
    
    # 反向求解变量
    n = len(matrix)
    for i in reversed(range(n)):
        sum_ax = 0
        for j in range(i+1, n):
            sum_ax += matrix[i][j] * solved[j]
            global_times += 1  # 乘法
            global_plus_times +=1 # 加法
        solved[i] = (matrix[i][n] - sum_ax) / matrix[i][i]
        global_times += 1      # 除法
        global_plus_times +=1  # 减法
        
        # 显示计算过程
        terms = " + ".join([f"{matrix[i][j]}×x{j+1}" for j in range(i+1, n)])
        print(f"x{i+1} = ({matrix[i][n]} - {terms}) / {matrix[i][i]} = {solved[i]}")

def column_pivot_gauss(matrix: list) -> None:
    """列主元高斯消元法主函数
    :param matrix: 输入矩阵
    :return: None
    """
    # 创建矩阵副本
    matrix = [row.copy() for row in matrix]
    
    # 消元过程
    for step in range(len(matrix)):
        elimination(matrix, step)
        if step == len(matrix)-1: break  # 最后一行无需消元
    
    # 回代求解
    back_substitution(matrix)

if __name__ == "__main__":
    print("="*50 + "\n列主元高斯消元法求解过程")
    column_pivot_gauss(MATRIX)
    
    # 打印最终结果
    print("\n" + "="*40 + "\n最终解:")
    for i, x in enumerate(solved):
        print(f"x{i+1} = {x} ({float(x):.6f})")
    
    # 运算统计
    print("\n运算统计:")
    print(f"乘法/除法次数: {global_times}")
    print(f"加法/减法次数: {global_plus_times}")
    print(f"总运算次数: {global_times + global_plus_times}")