def is_odd(n):
	return n % 2 == 1


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(filter(is_odd, nums)))

# 用filter求素数


def _odd_iter():
	n = 1
	while True:
		n = n + 2
		yield n


def _not_divisible(n):
	return lambda x: x % n > 0


def primes():
	yield 2
	it = _odd_iter()
	while True:
		n = next(it)
		yield n
		it = filter(_not_divisibl(n), it)
