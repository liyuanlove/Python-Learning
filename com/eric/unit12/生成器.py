# a = [x * 2 for x in range(10)]
# print(a)
# b = (x * 2 for x in range(10000000000000000))
# print(next(b))


def fib(times):
    n = 0
    print("---start----")
    a, b = 0, 1
    while n < times:
        print("---1----")
        temp = yield b
        print("---2----")
        print(temp)
        a, b = b, a + b
        print("---3----")
        n += 1
    return 'done'


g = fib(5)
for t in g:
    print(t)


