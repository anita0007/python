#定義函式
#函式內部的程式碼，若是沒有做函式呼叫，就不會執行
def multiply(n1,n2):
    print(n1*n2)
def add(a1,a2):
    print(a1+a2) #可寫可不寫
    return a1+a2
#呼叫函式
multiply(6,9)
value=add(3,5)+add(9,8)
print(value)
#函式可用來做程式的包裝:同樣的邏輯可以重複利用
def calculate(max):
    sum=0
    for x in range(1,max+1):
        sum=sum+x
    print(sum)
calculate(10)
calculate(20)