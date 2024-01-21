def better_than_average(a, your):
    return 'True' if sum(a) / len(a) < float(your) else 'False'
# or 使用内部的方法： return sum(points) / len(points) < float(your) 直接就是true和false
