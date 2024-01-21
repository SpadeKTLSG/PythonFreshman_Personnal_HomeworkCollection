# 找元音字母，按照基本想法，for循环加上if，计数器++,纯手工最复杂的

def get_count(sentence):
    a = 0
    for i in sentence:
        if i == 'a' or i == 'e' or i == 'o' or i == 'i' or i == 'u': a += 1
    return a


# 升级做法：使用sum函数去除计数，然后条件判断是否在字符串里面 in ，再搭配for后置。
def getCount(Str):
    return sum(1 for a in Str if a in "aeiou")  # 表示sum每次都加一，for循环加上 in 修饰a，if条件加手动字符串“ ”


def getCount2(s):
    return sum(c in 'aeiou' for c in s)  # 另一种表达，说明sum的结构可以十分的灵活。这里 的for很明显的是后置的，并且，c在前面并不参与计数，这里默认为1，下面进行语法流畅性的测试，test在不同情况下sum的使用情况：


# 测试完毕，只有这两种情况可以选择，反正第一项都是值（相加的）或者后面用于判断的对象。

print(get_count('sdgaaadjskfis'))
