# 字母的替换——大小写，考虑轮盘
# 加密程序1.0:
# ord 和chr 都是python中的内置函数,ord可以把ASCII字符转成对应在ASCII表中的序号,chr则是可以把序号转成字符串。
# 大写字母中在表中是从65开始，减掉64刚好是大写字母在表中的位置。
# 小写字母是从97开始，减于96就是对应的字母表位置。
# 记录x=(ord('item') - 96)
# 7行稳定版
a = input("put your code here :>")
b = str()
for index, item in enumerate(a):
    x = int(ord(item) - 96)
    if index % 2 == 0:
        b += chr(72 + x) if x == 26 or x == 25 else chr(98 + x)
    else:
        b += chr(95 + x) if x != 1 else chr(121 + x)
print(b)
