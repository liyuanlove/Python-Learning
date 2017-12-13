import random
while 1:
	value = int(input("请输入 剪刀（0） 石头（1） 布（2）"))
	if value == 3:
		break
	computer = random.randint(0, 2)
	if computer == 2:
		if value == 2:
			print("电脑是2,平局")
		else:
			print("电脑是2,输了")
	elif computer < value:
		print("电脑是" + str(computer)+",赢了")
	elif computer > value:
		print("电脑是" + str(computer)+",输了")
	print(computer)
