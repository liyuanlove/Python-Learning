# -*- coding :utf-8-*-
players = ['charles','martina','micheael','florence','eli']
print("只打印0-2")
print(players[0:3])
print("只打印2-3")
print(players[2:4])
print("不指定初始索引")
print(players[:4])
print("不指定结尾索引")
print(players[2:])
print("打印倒数两个")
print(players[-2:])
print("遍历前3个切片")
for player in players[:3]:
	print(player.title())
print("复制")
my_food = ['pizza','cafe','Martini','Cappuccino']
friend_foods = my_food[:]
print("my favorite foods are :" ,my_food)
print("my friend's favorite foods are:" ,friend_foods)
friend_foods = my_food[:2]
print("my friend's favorite foods are:" ,friend_foods)