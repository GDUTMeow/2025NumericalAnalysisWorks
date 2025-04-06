from fractions import Fraction
from typing import Union
from pprint import pprint

"""
使用高斯消元法求解线性方程组

- 6*x1 + 3*x2 + 2*x3 = 1/3
- 10*x1 + 5*x2 + 6*x3 = 0
- 8*x1 + 5*x2 + 3*x3 = 0
"""

MATRIX = [
    [6, 3, 2, Fraction(1, 3)],  # 用 Fraction 类表示分数来减小后续运算可能造成的误差
    [10, 5, 6, 0],
    [8, 5, 3, 0],
]

solved = [0, 0, 0]  # 用于存储解的列表
global_plus_times = 0  # 用于存储加法次数
global_times = 0  # 用于存储乘法次数


def calculate_l(
    base_line_first: Union[int, float], current_line_first: Union[int, float]
) -> float:
    """
    计算高斯消元法的行乘数 l
    :param base_line_first: 基准行的首项
    :param current_line_first: 当前行的首项
    :return: 行乘数 l
    """
    global global_times
    global_times += 1
    return current_line_first / base_line_first


def elimination(matrix: list[list[Union[int, float]]], base_line_index: int) -> None:
    """
    高斯消元法的消元操作
    :param matrix: 矩阵
    :param base_line_index: 基准行的索引
    :return: None
    """
    global global_plus_times
    if (
        MATRIX[base_line_index][base_line_index] == 0
    ):  # 如果基准行的首项为0，则与下面某行非零的进行交换
        print(f"基准行第 {base_line_index} 行首项为0，进行行交换")
        pprint(matrix)
        for i in range(base_line_index + 1, len(matrix)):
            if matrix[i][base_line_index] != 0:
                matrix[base_line_index], matrix[i] = matrix[i], matrix[base_line_index]
                print(f"交换第 {base_line_index} 行和第 {i} 行")
                pprint(matrix)
                break
    # 进行逐行消元
    for i in range(base_line_index + 1, len(matrix)):
        # 计算行乘数 l
        l = calculate_l(
            matrix[base_line_index][base_line_index], matrix[i][base_line_index]
        )
        prev_line = matrix[i]
        # 将当前行减去基准行乘以行乘数 l
        for j in range(len(matrix[i])):
            matrix[i][j] -= matrix[base_line_index][j] * l
            global_plus_times += 1
        print(f"经过消元过程，{prev_line} - {l} * {matrix[base_line_index]} = \n{matrix[i]}")


def solve(matrix: list[list[Union[int, float]]]) -> None:
    """
    高斯消元法求解线性方程组
    :param matrix: 矩阵
    :return: None
    """
    global global_plus_times, global_times
    # 进行高斯消元法的消元操作
    for i in range(len(matrix) - 1):
        elimination(matrix, i)
        
    # 消元后打印矩阵
    print("消元后:")
    pprint(matrix)

    # 回代修正
    # x3 = (第三行常数项) / 第三行x3系数
    solved[-1] = matrix[-1][-1] / matrix[-1][-2]
    global_times += 1

    # x2 = (第二行常数项 - x3系数*x3) / x2系数
    solved[-2] = (matrix[-2][-1] - matrix[-2][2] * solved[-1]) / matrix[-2][1]
    global_times += 2  # 乘法和除法
    global_plus_times += 1  # 减法

    # x1 = (第一行常数项 - x2系数*x2 - x3系数*x3) / x1系数
    solved[-3] = (
        matrix[0][-1] - matrix[0][1] * solved[-2] - matrix[0][2] * solved[-1]
    ) / matrix[0][0]
    global_times += 3  # 两次乘法一次除法
    global_plus_times += 2  # 两次减法


if __name__ == "__main__":
    solve(MATRIX)  # 调用高斯消元法求解线性方程组
    print(solved)  # 输出解的列表
    for i in range(len(solved)):
        print(f"x{i + 1} = {solved[i]}")  # 输出每个变量的值
    pprint(MATRIX)
    print(f"加法次数: {global_plus_times}")  # 输出加法次数
    print(f"乘法次数: {global_times}")  # 输出乘法次数
    print(f"总运算次数: {global_plus_times + global_times}")  # 输出总运算次数
