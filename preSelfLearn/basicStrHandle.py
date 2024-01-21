# 我的删除空格，一个字符串
def no_space(x):
    a = list(x)
    x = a.count(' ')
    for o in range(x):
        a.remove(' ')
    b = ""
    for i in a:
        b += i
    return b


print(no_space("34  fgfg gfg g f"))


def no_space(x):
    return x.replace(' ', '')  # 把前面的这个参数变成后面的这个。


print(no_space("ssd r t e "))


def reverse_words(text):
    k = a = ''
    for i in text:
        if i == ' ':
            k += (a[::-1])
            a = ''
            k += ' '
        elif i == text[-1]:
            a += i
            k += (a[::-1])
        else:
            a += i
    return k


def reverse_words1(str):
    return ' '.join(s[::-1] for s in str.split(' '))  # 删去空格大神做法：


def reverse_words2(str):
    return ' '.join(str[::-1])  # 直接全部倒序输出，表示一个一个字符进行拼接


def reverse_words3(str):
    return ' '.join(s[::-1] for s in str)  # 若没有分割，那么就和原来的一样，加上了空格


def deep_in(str):
    return str.split(' ')  # 这个说明变成了列表，每个切片都是里面的一个对象（成员），所以前面可以使用for s in 来进行遍历。


print(reverse_words("elbuod  decaps  sdrow"))
print(reverse_words1("elbuod  decaps  sdrow"))
print(reverse_words2("elbuod  decaps  sdrow"))
print(reverse_words3("elbuod  decaps  sdrow"))
print(deep_in("elbuod  decaps  sdrow"))
