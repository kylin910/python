print('-----------猜数字游戏-------------')
temp=input("不妨猜一下我现在心里想的是哪个数字：")
guess=int(temp)
if guess==8:
    print("猜对了")
    print("哼!猜中了也没奖励")
else:
    print("猜错了。")
print("游戏结束。")
