#集合的運算
s1={3,4,5}
s2={4,5,6,7}
print(2 not in s1 )
print(3 in s1) #in在裡面 not in 不在裡面
s3=s1&s2 #&交集:取兩個集合中，相同的資料
print(s3)
s4=s1|s2 #|聯集:取兩個集合中所有的資料，但不重複
print(s4)
s5=s1-s2 #差集:從s1中，減去和s2重複的部分
print(s5)
s6=s1^s2 #反交集:取兩個集合中，不重複的部分
print(s6)
s=set("Hello") #set(字串)
print(s) #將字串的字母拆解成集合
#字典的運算:key-value的配對
dic={"apple":"蘋果","banana":"香蕉"}
print(dic["apple"])
print("apple" in dic)
print(dic)
del dic["apple"] #刪除字典中的鍵值對 (key-value pair)
print(dic)
dic={x:x*2 for x in [3,4,5]} #從列表的資料產生字典
print(dic) #把列表轉化成鍵值對