#判斷式
x=input("請輸入數字:") #取得字串形式的使用者輸入
x=int(x) #將字串型態轉換成數字型態
if x>200:
    print("大於200")
elif x>100:
    print("大於100，小於等於200")
else:
    print("小於等於100")
a1=int(input("請輸入數字一:"))
a2=int(input("請輸入數字二:"))
op=input("+,-,*,/:")
if op=="+":
    print(a1+a2)
elif op=="-":
    print(a1-a2)
elif op=="*":
    print(a1*a2)
elif op=="/":
    print(a1/a2)
else:
    print("請不要瞎掰好嗎")