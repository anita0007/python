#有序可變動列表 #中括號
grades=[12,36,96,87,66]
grades=grades+[23,69,87,55,64]
grades[0]=60 #把60放到列表中的第一個位置
grades[1:4]=[] #連續刪除列表中從編號1到編號4(不含)的資料
length=len(grades) #取得列表的長度 len(列表資料)
print(length)
date=[[3,4,5],[6,7,8]]
print(date)
date[0][0:2]=[1,2,3]
print(date)
#有序不可變動列表Tuple #小括號
date=(2,4,5)
print(date)