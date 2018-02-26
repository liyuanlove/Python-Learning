# filter是过滤器，根据第一个参数的函数返回的true or false
def is_odd(n):
    return n % 2 == 1


print(list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9])))


# 把一个序列中的空字符串删掉
def not_empty(s):
    return s and s.strip()


ml = list(filter(not_empty, ['A', '', 'B', None, 'C', ' ']))
print(ml)
