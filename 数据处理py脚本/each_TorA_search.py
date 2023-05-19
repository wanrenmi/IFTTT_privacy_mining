import json
file='result.json'
allTorA=[]
f=open(file,'r',encoding='utf-8')
data=json.load(f)
f.close()
for dict_data in data:
    allTorA.append(dict_data['triggerChannelTitle'])#这里选着是搜索trigger或者是action
allTorA=list(set(allTorA))
print(('\n共有'+str(len(allTorA))+'个TorA'))
for TorA in allTorA:
    i=0
    for dict_data in data:
        if (TorA == dict_data['triggerChannelTitle']):
             i+=1
    mat = "{:50}\t{:10}"
    print(mat.format(TorA+' ('+str(i)+')',str(i)))
