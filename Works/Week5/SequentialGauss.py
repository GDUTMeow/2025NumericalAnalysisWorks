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
    global_times += 1  # 除法运算计数
    return current_line_first / base_line_first


def elimination(matrix: list[list[Union[int, float]]], base_line_index: int) -> None:
    """
    高斯消元法的消元操作
    :param matrix: 矩阵
    :param base_line_index: 基准行的索引
    :return: None
    """
    global global_plus_times, global_times
    
    # 打印消元前矩阵状态
    print(f"\n{'='*40}\n消元前 [第{base_line_index+1}步]")
    pprint(matrix)
    
    # 主元为零时的行交换处理 (修正：检查当前处理的矩阵)
    if matrix[base_line_index][base_line_index] == 0:
        print(f"⚠️ 第{base_line_index+1}行主元为零，正在寻找交换行...")
        for i in range(base_line_index + 1, len(matrix)):
            if matrix[i][base_line_index] != 0:
                matrix[base_line_index], matrix[i] = matrix[i], matrix[base_line_index]
                print(f"↔️ 已交换第{base_line_index+1}行和第{i+1}行")
                break
    
    # 进行逐行消元
    for i in range(base_line_index + 1, len(matrix)):
        # 计算行乘数 l
        l = calculate_l(
            matrix[base_line_index][base_line_index],  # 基准行主元
            matrix[i][base_line_index]                 # 当前行首项
        )
        print(f"系数 L_{i+1}{base_line_index+1} = {l:.3f}")
        
        # 执行行变换
        for j in range(len(matrix[i])):
            delta = matrix[base_line_index][j] * l  # 乘法运算
            matrix[i][j] -= delta                    # 减法运算
            # 运算次数统计
            global_times += 1      # 乘法计数
            global_plus_times += 1 # 减法计数
    
    # 打印消元后矩阵状态
    print(f"\n消元后 [第{base_line_index+1}步]")
    pprint(matrix)


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

    # 显示最终矩阵结构
    print(f"\n{'='*40}\n上三角矩阵最终形态:")
    pprint(matrix)

    # 回代求解过程
    print(f"\n{'='*40}\n开始回代求解:")
    
    # 求解 x3 (从最后一行开始)
    solved[2] = matrix[2][3] / matrix[2][2]
    global_times += 1  # 除法计数
    print(f"x3 = {matrix[2][3]} / {matrix[2][2]} = {solved[2]}")
    
    # 求解 x2
    numerator = matrix[1][3] - matrix[1][2] * solved[2]
    solved[1] = numerator / matrix[1][1]
    global_times += 2    # 乘法 + 除法
    global_plus_times += 1  # 减法
    print(f"x2 = ({matrix[1][3]} - {matrix[1][2]}×{solved[2]}) / {matrix[1][1]} = {solved[1]}")
    
    # 求解 x1
    numerator = matrix[0][3] - matrix[0][1]*solved[1] - matrix[0][2]*solved[2]
    solved[0] = numerator / matrix[0][0]
    global_times += 3    # 两次乘法 + 除法
    global_plus_times += 2  # 两次减法
    print(f"x1 = ({matrix[0][3]} - {matrix[0][1]}×{solved[1]} - {matrix[0][2]}×{solved[2]}) / {matrix[0][0]} = {solved[0]}")


if __name__ == "__main__":
    # 创建矩阵副本避免修改原始数据
    import copy
    matrix = copy.deepcopy(MATRIX)
    
    print(f"\n{'='*40}\n初始矩阵:")
    pprint(matrix)
    
    solve(matrix)  # 调用高斯消元法求解
    
    # 打印最终结果
    print(f"\n{'='*40}\n方程解:")
    for i in range(len(solved)):
        print(f"x{i+1} = {solved[i]} ({float(solved[i]):.6f})")
    
    # 运算统计
    print(f"\n{'='*40}\n运算次数统计:")
    print(f"乘法/除法次数: {global_times}")
    print(f"加法/减法次数: {global_plus_times}")
    print(f"总运算次数: {global_times + global_plus_times}")