names = ["Michael", "Eric", "Jack"]
for name in names:
	print(name)
mysum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
	mysum = mysum + x
print(mysum)

mysum2 = 0
rangelist = list(range(101))
for x in rangelist:
	mysum2 = mysum2 + x
print(mysum2)
mysum3 = 0
n = 99
while n > 0:
	mysum3 = mysum3 + n
	n = n - 2
print(mysum3)

n = 1
while n <= 100:
	if n > 10:
		break
	print(n)
	n = n + 1
print("END")

n = 0
while n < 100:
	n = n+1
	if n % 2 == 0:
		continue
	print(n)

