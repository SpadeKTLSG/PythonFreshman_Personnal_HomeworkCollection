# 加减乘除表达：
def basic_op(operator, value1, value2):
    a = int(value1)
    b = int(value2)
    # if operator=='+':return(a+b)这个是最容易想到的解决方法，使用elif不断查找，但是维护成本很高。
    # 使用字典实现switch/case这种方式易维护，同时也能够减少代码量
    op = {
        '+': a + b,
        '-': a - b,
        '*': a * b,
        '/': a / b
    }
    return op.get(operator)  # KEY Point


print(basic_op('-', 23, 5))


# 当然，还有eval做法：

def basic_op(operator, value1, value2):
    return eval("{}{}{}".format(value1, operator, value2))  # 格式化字符输入，一一对应然后从str识别到表达式。


# ? 字典的勇武之地
def get_grade(s1, s2, s3):
    mean = float((s1 + s2 + s3) / 3)
    if mean >= 90: return 'A'
    if mean >= 80: return 'B'
    if mean >= 70: return 'C'
    if mean >= 60: return 'D'
    return 'F'  # 这种有大小的层层筛查，并没有字典的勇武之地
