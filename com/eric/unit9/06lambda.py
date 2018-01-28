infos = [{"name": "laowang", "age": 10}, {"name": "xiaoming", "age": 20}, {"name": "jack", "age": 99}]

infos.sort(key=lambda x: x['name'], reverse=True)
print(infos)


def test(a, b, func):
	result = func(a, b)
	return result


num = test(11, 22, lambda x, y: x + y)
print(num)

func_new = input("请输入一个匿名函数")
func_new = eval(func_new)
num2 = test(11, 23, func_new)
print(num2)
