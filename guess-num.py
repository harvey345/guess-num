import time
import random
print("~猜數字遊戲 Guess Number~")
st=int(input("請輸入範圍起始值："))
ed=int(input("請輸入範圍結束值："))
ti=int(input("請輸入猜數次數："))
tt=0
print("~遊戲開始~")
rnu=random.randint(st,ed)
while 1:
    pl=int(input("請輸入一個數 :"))

    if pl > rnu:
        print("再小一點。")
    elif pl < rnu:
        print("再大一點。")
    else:
        print("你猜中了！")
        tt+=1
        break
    tt+=1
print("你猜了",tt,"次")