# 載入內建的sys 模組並取得資訊
import sys as s
print(s.platform)
print(s.maxsize)
#建立geometry 模組，載入使用
import geometry
result=geometry.distance(1,1,5,5)
print(result)
result=geometry.slope(1,1,5,5)
print(result)
# 調整搜尋模組的路徑
import sys 
sys.path.append("modules") #在模組的搜索路徑列表中[新增路徑]
print(sys.path) #印出模組的搜尋路徑
import geometry 
print(geometry.distance(1,1,5,5))

import sys as s
s.path.append("modules")
print(s.path)
import geometry as g
print(g.distance(1,1,5,5))