import sys


class Msg:
    def __send_msg(self):
        print("发送短信成功")

    def send_msg(self, money):
        if money > 0:
            self.__send_msg()
        else:
            print("余额不足，请充值后再试")

    def __del__(self):
        print("del方法")


msg = Msg()
msg.send_msg(-1)

count = sys.getrefcount(msg)
print(count)

print("-----------------")
