# 10转2小助手 - 自己造轮子
# 10-->2小助手V 2.03 18行 概念版
"""a = input("your number to be changed: ")
if ('-' in a):
    print('-', end='')
    a = a.strip('-')
e = obj = float(a)
up = []
while obj >= 1:
    up += str(int(obj % 2))
    obj = (obj // 2)
for i in up[::-1]: print(i, end='')
if ('.' in a):
    print('.', end='')
    up.clear()
    x = e - int(e)
    for j in range(0, 6):
        x *= 2
        up += str(int(x))
        if x > 1: x -= 1
    for i in up: print(i, end='')"""

# 10-->2小助手V 3.12 8行 稳定版
"""a = float(input())
b = a - int(a)
if b < 0: b *= -1
print(format(int(a), 'b'), end='.')
for j in range(0, 6):
    b *= 2
    print(str(int(b)), end='')
    if b > 1: b -= 1"""

# 10-->2小助手V 3.72 8行 旗舰版
"""# 原始数据处理；
front = float(input("your number to be changed: "))
back = front - int(front)
if back < 0: back *= -1
# 整数输出，‘b’代表二进制，仅支持整数；
print(format(int(front), 'b'), end='.')
# 小数输出，推演；
for j in range(0, 6):
    back *= 2
    print(str(int(back)), end='')
    if back > 1: back -= 1"""

# 10-->2小助手V 01.01 15行 专业版
"""a = float(input("your number to be changed: "))
if a < 0:
    a *= -1
    print("-", end='')
x = a - int(a)
obj = int(a)
up = []
while obj >= 1:
    up += str(int(obj % 2))
    obj //= 2
for i in up[::-1]: print(i, end='')
print('.', end='')
for j in range(0, 6):
    x *= 2
    print(str(int(x)), end='')
    if x > 1: x -= 1
"""

# 10-->2小助手V 3.90 8行 专业版
front = float(input("your number to be changed: "))
back = front - int(front)
if back < 0: back *= -1
print(format(int(front), 'b'), end='.')
for j in range(0, 6):
    back *= 2
    print(str(int(back)), end='')
    if back > 1: back -= 1
