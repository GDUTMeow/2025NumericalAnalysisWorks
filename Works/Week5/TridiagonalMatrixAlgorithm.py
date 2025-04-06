from typing import Union
import copy

"""
使用追赶法解线性方程组
[ 4 -1  0  0  0  100],
[-1  4 -1  0  0  200],
[ 0 -1  4 -1  0  200],
[ 0  0 -1  4 -1  200],
[ 0  0  0 -1  4  100]

"""

MATRIX = [
    [4, -1, 0, 0, 0, 100],
    [-1, 4, -1, 0, 0, 200],
    [0, -1, 4, -1, 0, 200],
    [0, 0, -1, 4, -1, 200],
    [0, 0, 0, -1, 4, 100],
]

"""
MATRIX 应该看做
[d1, c1,  0,  0,  0, b1],
[a2, d2, c2,  0,  0, b2],
[ 0, a3, d3, c3,  0, b3],
[ 0,  0, a4, d4, c4, b4],
[ 0,  0,  0, a5, d5, b5]
"""

add_sub_count = 0
mul_div_count = 0


def get_u(
    lidx: int,
    v_prev: Union[int, float, None] = None,
    u_prev: Union[int, float, None] = None,
) -> Union[int, float]:
    """
    计算 u 值，根据公式
    u1 = d1
    u2 = d2 - (a2 * v1 / u1)
    其中 a2 为当前行的 a 值，d2 为当前行的 d 值，根据主对角矩阵的元序为 a d c，其中主对角线为 d
    :param lidx: 当前行索引
    :param v_prev: 上一行的 v 值
    :param u_prev: 上一行的 u 值
    :return: 当前行的 u 值
    """
    global add_sub_count, mul_div_count
    if lidx == 0:
        return MATRIX[lidx][lidx]  # 当 lidx 为 0 时，u1 = d1
    else:
        a = MATRIX[lidx][lidx - 1]
        d = MATRIX[lidx][lidx]
        mul_div_count += 2
        add_sub_count += 1
        if v_prev is None or u_prev is None:
            raise ValueError(
                "v_prev and u_prev must be provided for non-first row."
            )  # 不是第一行的时候必须提供 v_prev 和 u_prev
        return d - (a * v_prev / u_prev)


def get_v(lidx: int) -> Union[int, float]:
    """
    计算 v 值，根据公式
    vi = ci
    可以直接采用 ci 的值
    :param lidx: 当前行索引
    :return: 当前行的 v 值
    """
    return MATRIX[lidx][lidx + 1]  # ci 的值就是 v 值


def get_y(
    lidx: int, v_prev: Union[int, float] = None, u_prev: Union[int, float] = None
) -> Union[int, float]:
    """
    计算 y 值，根据公式
    y1 = b1
    yi = bi - (ai * yi-1) / ui-1
    :param lidx: 当前行索引
    :param v_prev: 上一行的 v 值
    :param u_prev: 上一行的 u 值
    :return: 当前行的 y 值
    """
    global add_sub_count, mul_div_count
    if lidx == 0:
        return MATRIX[lidx][lidx + 5]  # 当 lidx 为 0 时，y1 = b1
    else:
        a = MATRIX[lidx][lidx - 1]
        b = MATRIX[lidx][-1]  # b 值在最后一列
        if v_prev is None or u_prev is None:
            raise ValueError(
                "v_prev and u_prev must be provided for non-first row."
            )  # 不是第一行的时候必须提供 v_prev 和 u_prev
        mul_div_count += 2
        add_sub_count += 1
        return b - (a * v_prev / u_prev)


def get_a(lidx: int) -> Union[int, float]:
    """
    计算 a 值，根据公式
    ai = ai+1
    :param lidx: 当前行索引
    :return: 当前行的 a 值
    """
    if lidx == 0:
        raise ValueError("lidx must be greater than 0 to get a value.")  # a1 是不存在的
    return MATRIX[lidx][lidx - 1]  # ai 的值


def get_c(lidx: int) -> Union[int, float]:
    """
    计算 c 值，根据公式
    ci = ci-1
    :param lidx: 当前行索引
    :return: 当前行的 c 值
    """
    if lidx == len(MATRIX) - 1:
        raise ValueError(
            "lidx must be less than the last index to get c value."
        )  # c[-1] 是不存在的
    return MATRIX[lidx][lidx + 1]  # ci 的值


# 回代
def backward(
    lidx: int,
    y_current: Union[int, float],
    u_current: Union[int, float],
    x_next: Union[int, float],
):
    """
    回代求解过程，根据公式
    xn = yn / un（n为行总数，也是未知元个数）
    xi = (yi - ci * xi+1) / ui（i为当前行索引）
    可以求得 xi 的值
    :param lidx: 当前行索引
    :param y_current: 当前行的 y 值
    :param u_current: 当前行的 u 值
    :param x_next: 下一行的 x 值，即索引自增的已知元的值
    :return: 当前行的 x 值
    """
    global add_sub_count, mul_div_count
    if lidx == len(MATRIX) - 1:
        mul_div_count += 1
        return y_current / u_current  # 最后一行的 x 值
    else:
        c = MATRIX[lidx][lidx + 1]  # ci 的值
        mul_div_count += 2
        add_sub_count += 1
        return (y_current - c * x_next) / u_current  # xi 的值


if __name__ == "__main__":
    matrix = copy.deepcopy(MATRIX)

    print(f"\n{'='*40}\n初始矩阵:")
    for row in matrix:
        print(row)

    # 追赶法求解线性方程组
    n = len(MATRIX)  # 行数
    u = [0] * n  # 存储 u 值的列表
    v = [0] * n  # 存储 v 值的列表
    y = [0] * n  # 存储 y 值的列表
    x = [0] * n  # 存储 x 值的列表

    # 计算 u 和 v 值
    for i in range(n):
        u[i] = get_u(i, v[i - 1] if i > 0 else None, u[i - 1] if i > 0 else None)
        v[i] = get_v(i)

    # 计算 y 值
    for i in range(n):
        y[i] = get_y(i, v[i - 1] if i > 0 else None, u[i - 1] if i > 0 else None)

    # 打印 u、v、y 的值
    print(f"\n{'='*40}\nu、v、y 的值:")
    for i in range(n):
        print(f"u[{i}] = {u[i]}, v[{i}] = {v[i]}, y[{i}] = {y[i]}")

    # 回代求解 x 值
    x[-1] = y[-1] / u[-1]  # 最后一行的 x 值
    mul_div_count += 1  # 手动统计最后一行除法
    for i in range(n - 2, -1, -1):  # 从倒数第二行开始回代求解 x 值
        x[i] = backward(i, y[i], u[i], x[i + 1])

    # 打印最终结果
    print(f"\n{'='*40}\n方程解:")
    for i in range(len(x)):
        print(f"x{i+1} = {x[i]} ({float(x[i]):.6f})")
    print(f"\n加减法次数: {add_sub_count}")
    print(f"乘除法次数: {mul_div_count}")
