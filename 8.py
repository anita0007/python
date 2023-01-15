# break 的簡易範例
n=0
while n<6:
    if n==3:
        break
    print(n) #印出迴圈的n
    n+=1
print("最後的n:",n) #印出迴圈中最後的n
# continue 的簡易範例
a=0
for x in [3,4,5,6]:
    if x%2==0: # x是偶數
        continue
    print(x)
    a+=1
print("最後的a:",a)
# else的簡易範例
sum=0
for s in range(11):
    sum+=s
else:
    print(sum) # 印出0+1+2+3...+10的結果
# 綜合範例:找出整數平方根
c=int(input("請輸入一個正整數:"))
for f in range(c): #f從0~c-1
    if f*f==c: 
        print("整數平方根:",f)
        break #用break強制結束迴圈時，不會執行else區塊
else:
    print('沒有整數平方根')
