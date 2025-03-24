"""
Author: GamerNoTitle
Date: 2025-03-24
Link: https://github.com/GDUTMeow/2025NumericalAnalysisWorks
"""

"""
用本章学习的多种方法分别求解以下方程并进行对比
$7x^5 - 13x^4-21x^3-12x^2+58x+3=0, x∈[1,2]$
其中初值取 x0 = 1.5，并设置停止条件为 | x(n) - x(n-1) | < 1e-5
"""
from autograd import grad  # 求导工具

DEADLINE = 1e-5  # 终止条件
MAX_ITER_COUNT = 1000  # 最大迭代次数
x0 = 1.5  # 初值
chord_x0 = 2  # 弦截法的初值
chord_x1 = 1  # 弦截法的初值


def f(x):  # 题目给的 f(x)
    """
    f = 7x^5 - 13x^4-21x^3-12x^2+58x+3
    """
    return 7 * x**5 - 13 * x**4 - 21 * x**3 - 12 * x**2 + 58 * x + 3


# 输出到 Markdown 表格的函数，用于处理数据
def output_with_markdown_table(iter_data: list, table_name: str) -> None:
    """
    输出 Markdown 表格
    :param iter_data: 迭代数据
    :param table_name: 表格名

    :return: None
    """
    with open("Works/Homework4.md", "at", encoding="utf8") as f:
        f.write("\n\n")  # 区分上层数据
        f.write(f"## {table_name}\n\n")  # 写入表格的名称，便于区分
        f.write("| 迭代次数 | x |\n")  # 表头
        f.write("| ---- | ---- |\n")  # 表头与数据的分隔线
        for iter_time, x in iter_data:
            f.write(f"| {iter_time} | {x} |\n")
        f.write("\n")  # 区分下层数据


########## 定义迭代函数 ##########
def iter1(x):
    return 7 * x**5 - 13 * x**4 - 21 * x**3 - 12 * x**2 + 59 * x + 3


def iter2(x):
    return ((13 * x**4 + 21 * x**3 + 12 * x**2 - 58 * x - 3) / 7) ** (1 / 5)


def iter3(x):
    return ((13 + (21 / x) + (12 / x**2) - (58 / x**3) - (3 / x**4))) / 7


def iter4(x):
    return ((12 * x**2 - 58 * x - 3) / (7 * x**2 - 13 * x - 21)) ** (1 / 3)


def iter5(x):
    return ((-58 * x - 3) / (7 * x**3 - 13 * x**2 - 21 * x - 12)) ** (1 / 2)


########## 定义迭代方法 ##########
# 不动点迭代法
def fixed_point_iteration(**kwargs) -> None:
    """
    不动点迭代法
    :param x: 初值
    :param iter_func: 迭代函数

    :return: None
    """
    x: float = kwargs["x"]
    iter_func: callable = kwargs["iter_func"]
    iter_count = 0  # 初始化迭代次数
    iter_data = []  # 初始化迭代数据，用于后期输出成 Markdown 表格
    iter_data.append((iter_count, x))  # 将初值加入迭代数据
    try:
        while abs(x - iter_func(x)) > DEADLINE:
            x = iter_func(x)
            iter_count += 1
            iter_data.append((iter_count, x))
            print(f"进行 {iter_count} 次迭代，此时的 x 为 {x}")
    except OverflowError:
        print(f"进行 {iter_count} 次迭代时出现了溢出错误，终止迭代！")
        iter_data.append((iter_count, "溢出错误"))
    finally:
        output_with_markdown_table(iter_data, f"不动点迭代法 {iter_func.__name__}")


# Aitken 埃特金算法加速的迭代法
def aitken(**kwargs) -> None:  # 抄 PPT 里面的代码的
    """
    Aitken 加速的迭代法
    :param x: 初值
    :param max_iter_count: 最大迭代次数
    :param iter_func: 迭代函数

    :return: None
    """
    x: float = kwargs["x"]
    max_iter_count: int = kwargs["max_iter_count"]
    iter_func: callable = kwargs["iter_func"]
    iter_count = 0  # 初始化迭代次数
    iter_data = []  # 初始化迭代数据，用于后期输出成 Markdown 表格
    found_flag = 0  # 是否找到符合要求的解
    try:
        for i in range(max_iter_count):  # 最多迭代 max_iter_count 次
            x1 = iter_func(x)  # 根据算法要求，获得两个值
            x2 = iter_func(x1)  # 根据算法要求，获得两个值
            iter_count += 1
            iter_data.append((iter_count, x2))  # 将迭代数据加入列表
            if (x2 - 2 * x1 + x) != 0:
                result = x2 - (x2 - x1) ** 2 / (
                    x2 - 2 * x1 + x
                )  # 根据 Aitken 算法，通过 x, x1, x2 可以得到一个结果
                print(f"进行 {iter_count} 次迭代，此时的 x 为 {result}")
                if (
                    abs(result - iter_func(result)) < DEADLINE
                ):  # 如果结果和迭代函数的差值达到了精度要求，则迭代结束
                    found_flag = 1
                    break
                else:
                    x = result  # 将结果赋值给 x，进行下一轮迭代
            else:
                print(
                    f"进行 {iter_count} 次迭代时出现了除零错误，Aitken 算法无法使用提供的迭代函数为此函数进行迭代！"
                )
                break
        if not found_flag:
            print(f"经过 {iter_count} 次迭代后，在有限步迭代中无法达到精度要求！")
            iter_data.append((iter_count, "无法达到精度要求"))
    except OverflowError:
        print(f"进行 {iter_count} 次迭代时出现了溢出错误，终止迭代！")
        iter_data.append((iter_count, "溢出错误"))
    except ZeroDivisionError:
        print(f"进行 {iter_count} 次迭代时出现了除零错误，终止迭代！")
        iter_data.append((iter_count, "除零错误"))
    finally:
        output_with_markdown_table(
            iter_data, f"Aitken 算法加速的迭代法 {iter_func.__name__}"
        )


# Steffensen 加速的迭代法
def steffensen(**kwargs) -> None:
    """
    Steffensen 加速的迭代法
    :param x: 初值
    :param max_iter_count: 最大迭代次数
    :param iter_func: 迭代函数

    :return: None
    """
    x: float = kwargs["x"]
    max_iter_count: int = kwargs["max_iter_count"]
    iter_func: callable = kwargs["iter_func"]
    iter_count = 0
    iter_data = []
    found_flag = 0
    for i in range(max_iter_count):  # 最多迭代 max_iter_count 次
        if iter_func(iter_func(x)) - 2 * iter_func(x) + x != 0:
            result = x - (iter_func(x) - x) ** 2 / (
                iter_func(iter_func(x)) - 2 * iter_func(x) + x
            )
            iter_count += 1
            iter_data.append((iter_count, result))
            print(f"进行 {iter_count} 次迭代，此时的 x 为 {result}")
            if abs(result - iter_func(result)) < DEADLINE:
                found_flag = 1
                break
            else:
                x = result
        else:
            print(
                f"进行 {iter_count} 次迭代时出现了除零错误，Steffensen 算法无法使用提供的迭代函数为此函数进行迭代！"
            )
            iter_data.append((iter_count, "除零错误"))
            break
    if not found_flag:
        print(f"经过 {iter_count} 次迭代后，在有限步迭代中无法达到精度要求！")
        iter_data.append((iter_count, "无法达到精度要求"))
    output_with_markdown_table(
        iter_data, f"Steffensen 算法加速的迭代法 {iter_func.__name__}"
    )


# Newton 牛顿迭代法
def newton(**kwargs) -> None:
    """
    Newton 牛顿迭代法
    :param x: 初值
    :param max_iter_count: 最大迭代次数
    :param iter_func: 迭代函数

    :return: None
    """
    x: float = kwargs["x"]
    max_iter_count: int = kwargs["max_iter_count"]
    iter_func: callable = kwargs["iter_func"]
    iter_count = 0
    iter_data = []
    found_flag = 0  # 是否找到符合要求的解
    for i in range(max_iter_count):
        y0 = iter_func(x)  # 算出初始 y0
        dy0 = grad(iter_func)(x)  # 算出初始 dy0（在 x 处的导数值）
        if dy0 != 0:  # 牛顿迭代法的条件：导数不为 0
            x1 = x - y0 / dy0
            iter_count += 1
            iter_data.append((iter_count, x1))
            print(f"进行 {iter_count} 次迭代，此时的 x 为 {x1}")
            if abs(x1 - x) < DEADLINE:
                found_flag = 1
                break
            else:
                x = x1
        else:
            break
    if not found_flag:
        print(f"经过 {iter_count} 次迭代后，在有限步迭代中无法达到精度要求！")
        iter_data.append((iter_count, "无法达到精度要求"))
    output_with_markdown_table(iter_data, f"Newton 牛顿迭代法 {iter_func.__name__}")


# 弦截法
def chord_method(**kwargs) -> None:
    """
    弦截法
    :param x0: 初值
    :param x1: 初值
    :param iter_func: 迭代函数
    :param MAX_ITER_COUNT: 最大迭代次数

    :return: None
    """
    x0 = kwargs["x0"]
    x1 = kwargs["x1"]
    MAX_ITER_COUNT: int = kwargs["max_iter_count"]
    iter_func: callable = kwargs["iter_func"]
    iter_count = 0
    iter_data = []
    try:
        for i in range(MAX_ITER_COUNT):
            x2 = x1 - iter_func(x1) * (x1 - x0) / (iter_func(x1) - iter_func(x0))
            iter_count += 1
            iter_data.append((iter_count, x2))
            relative_error = abs(x1 - x2)  # 计算相对误差
            print(f"进行 {iter_count} 次迭代，此时的 x 为 {x2}")
            if relative_error < DEADLINE:  # 当相对误差在精度范围内，停止迭代
                break
            else:
                x0, x1 = x1, x2
    except ZeroDivisionError:
        print(f"进行 {iter_count} 次迭代时出现了除零错误，终止迭代！")
        iter_data.append((iter_count, "除零错误"))
    finally:
        output_with_markdown_table(iter_data, f"弦截法 {iter_func.__name__}")


if __name__ == "__main__":  # 执行部分
    functions = [fixed_point_iteration, aitken, steffensen, newton, chord_method]
    iters = [iter1, iter2, iter3, iter4, iter5]
    for func in functions:
        for iter_func in iters:
            print(f"正在进行 {func.__name__} 的 {iter_func.__name__} 迭代法")
            func(
                x=x0,
                x0=chord_x0,
                x1=chord_x1,
                max_iter_count=MAX_ITER_COUNT,
                iter_func=iter_func,
            )
