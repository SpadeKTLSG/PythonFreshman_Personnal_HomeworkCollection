# 倒序字符输出，使用list
def reverser(n):
    return [int(x) for x in reversed(str(n))]


print(reverser(1233))


# 字符串开头结尾去掉：使用【1：-1】

remove_char = lambda s: s[1:-1]


# to defined the function anonymously

def remove_char(s):
    s = list(s)
    s.pop()
    s.pop(0)
    return ' '.join(s)  # 这里是用了join方法来连接slist里面的元素，‘-’代表用-连接


print(remove_char("sadwdadss"))
