# 数羊

# 难点： 1，填入自然增长的数字  2，字符串连续输出join
def count_sheep(n):
    return ''.join(f"{i} sheep..." for i in range(1, n + 1))
    # 填入前面的数字return "".join("{} sheep...".format(i) for i in range(1, n+1))


print(count_sheep(5))


def summation(num):
    return sum(range(num + 1))
# 只能说求和配上这个range真的很好用。。  sum+ range
