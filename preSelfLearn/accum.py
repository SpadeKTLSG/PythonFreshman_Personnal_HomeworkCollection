def accum(s):
    a = list(s)
    times = 1
    sit = 0
    for i in range(len(a)):
        if times == 1:
            times -= 1
            a[i] = a[i].upper()
        for o in range(sit):
            a[i] += s[i].lower()
        sit += 1
        times += 1

    return '-'.join(a)


# 尝试使用先全部放大，最后再一起全部最大的方法 , 4 lines
def accum1(s):
    a = list(s)  # 基本思路，拆分字符串为关键的处理部分，不可缺少。
    for i in range(len(a)):
        a[i] = s[i].upper()  # 必须的大写
        for j in range(i): a[i] += s[i].lower()  # 后面小写
    return '-'.join(a)  # join


# 太牛啦， 不仅使用了字符串相乘代表后面小写，还有enumerate（）这个函数，i代表位子，c代表目标，同时对字符串的每个小目标成立，这个我忘了。
def accum2(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))  # 还有一点，这个join函数可以指定后面这个小部件


# 得到灵感进行修改：使用enumerate函数来简化表达：

def accum3(s):
    a = list(s)  # 基本思路，拆分字符串为关键的处理部分，不可缺少。2-行  ——所以如果一开始就化整为零的话就0行了。
    for i, c in enumerate(s): a[i] = c.upper() + c.lower() * i
    return '-'.join(a)


print(accum3("EvidjUnokmM"))
# 只有字母的倒序，使用join各个字符方法，这个展示了join的强大之处，
# 在拆分的基础上，还可以有for+if的结构，最后还有切片倒序输出。
