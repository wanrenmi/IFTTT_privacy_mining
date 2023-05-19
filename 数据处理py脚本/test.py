# mat = "{:20}\t{:28}"
# print(mat.format("占4个长度","占8个长度", "占12长度"))
# #如果需要居中输出在宽度前面加一个^
# mat = "{:^20}\t{:^28}\t{:^32}"
# print(mat.format("占4个长度","占8个长度", "占12长度"))


import json
file='differences.json'
f=open(file,'r',encoding='utf-8')
data=json.load(f)
f.close()
for dict_data in data:
    print(dict_data)