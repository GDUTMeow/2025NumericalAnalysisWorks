minus = 2
LIMIT = 1e-20


def f(x):
    """
    f = x ** 2 - 2
    """
    return x**2 - minus


head = float(input("x 区间下限: "))
tail = float(input("x 区间上限: "))

itercount = 0

# 制 Markdown 表格提取数据
# print("""|      |      |      |      |      |
# | ---- | ---- | ---- | ---- | ---- |""")

if __name__ == "__main__":
    while (tail - head) ** 2 > LIMIT:
        middle = (tail + head) / 2
        itercount += 1
        print(f"进行 {itercount} 次迭代，下限为 {head}，上限为 {tail}, 此时的中值为 {middle}，f({middle}) {'<' if f(middle) < 0 else '>'} 0")
        # Markdown 表格提取数据
        # print(f"|{itercount - 1}|{head}|{tail}|{middle}|{'<' if f(middle) < 0 else '>'} 0|")
        if f(middle) > 0:
            tail = middle
        elif f(middle) < 0:
            head = middle
        else:
            print(
                f"经过 {itercount} 次迭代后，区间为 [{head}, {tail}]， 已经找到了解为 {middle}！"
            )
            break
    print(f"经过 {itercount} 次迭代后，程序结束")
