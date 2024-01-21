# 完全相同的时间

def count_by1(x, n):  # x: 步长， n: 个数
    b = list()
    t = 0
    a = x
    while t < n:
        b.append(a)
        a += x
        t += 1
    return b


def count_by2(x, n):  # x: 步长， n: 个数
    return range(x, x * n + 1, x)


def count_by3(x, n):  # x: 步长， n: 个数
    return [i * x for i in range(1, n + 1)]


print(count_by3(3, 4))
