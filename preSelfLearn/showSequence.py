# 悬而未决的map使用，吃大裤头
# 这个使用了map方法，没用过。join +  map(str, range(n+1))
def show_sequence(n):
    if n == 0:
        return "0=0"
    elif n < 0:
        return str(n) + "<0"
    else:
        counter = sum(range(n + 1))  # range的使用加上sum代表从1到这个值的求和。
        return '+'.join(map(str, range(n + 1))) + " = " + str(counter)  # return的东西竟然还嫩有加号，学到了




