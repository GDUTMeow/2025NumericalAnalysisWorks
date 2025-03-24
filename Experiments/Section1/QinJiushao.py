import time
import sys

sys.set_int_max_str_digits(99999999)    # 设置 int 转 str 的长度限制为 99999999，否则炸ValueError
# ValueError: Exceeds the limit (4300 digits) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit

x = [0.1, 1, 2, 10]

def calculate(x):
    f = 0
    add_times = 0
    mul_times = 0
    
    start_time = time.time()
    
    for i in range(100000, 0, -1):
        f = f * x + i
        add_times += 1
        mul_times += 1
        
    end_time = time.time()
    
    print("========== calculator output ==========")
    print(f"x = {x}")
    print(f"f length = {len(str(f))}")
    print(f"result = {f}")
    print(f"add_times = {add_times} times")
    print(f"mul_times = {mul_times} times")
    print(f"time used: {round(end_time - start_time, 2)} seconds",)
    print("")

if __name__ == "__main__":
    for _ in x:
        calculate(_)    