# 找最大值和最小值，分开的字符串里面。
"""def high_and_low(numbers):
    return (max(numbers.split(' ')), min(numbers.split(' ')))  # 找最大值和最小值，分开的字符串里面。"""
import math


def high_and_low2(numbers):
    return "%s %s" % (max(numbers.split(' ')), min(numbers.split(' ')))


# 偶数奇数求和判断
def odd_or_even(arr):
    return "even" if sum(arr) % 2 == 0 else "odd"


print(odd_or_even([0, 1, 3]))


# 嵌套求最小的循环min再求和

def sum_of_minimums(numbers):  # 嵌套求最小的循环min再求和
    return sum(min(a) for a in numbers)


# 真的骚的n开平方
def is_square(n):
    if n >= 0:
        return True if (int(n ** 0.5)) ** 2 == n else False
    else:
        return False


def is_square2(n):
    return n > -1 and math.sqrt(n) % 1 == 0  # 真的骚的n开平方后是不是能被1整除——判断是不是整数的方法：if sqrt（n）==0


# 碎碎念的第一版, 使用之前的c++的纯手动计数的方法，话费11行，手动加上计数器变量也是非常累人，之前c++的时候因为这个花费了不少时间，
# 很长时间以来，我都只知道这种手动计数的方法，但是现在要向精简化大步前行了、！


# 求阶乘和的递归双重
def fact(a): return 1 if a == 1 else fact(a - 1) * a


def factsum(a): return 1 if fact(a) == 1 else factsum(a - 1) + fact(a)


n = int(input("n="))
print(factsum(n))
