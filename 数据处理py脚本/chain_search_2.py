import json
file='result.json'
allapp=[]
f=open(file,'r',encoding='utf-8')
data=json.load(f)
f.close()
txt=open('chaintest输出结果.txt','a',encoding='utf-8')
txt.write('输出格式为：A --> B --> C，其中AB分别为app1的trigger和action，BC分别为app2的trigger和action。')
for dict_data in data:
    allapp.append(dict_data)
i=0
count=0
for app in allapp:
    j=0
    for dict_data in data:
        if (app['actionChannelTitle'] == dict_data['triggerChannelTitle']):#2段连接条件满足
            j+=1
            count+=1
            txt.write('\n'+str(count)+'.'
                  +'\n信息流为'+app['triggerChannelTitle']+' --> '+app['actionChannelTitle']+' --> '+dict_data['actionChannelTitle']
                  +'\napp1的title为：'+app['title']
                  +'\napp1的desc为：'+app['desc']
                  +'\napp2的title为：' + dict_data['title']
                  +'\napp2的desc为：' + dict_data['desc']
                  )
        if(j==50):
            break
    i+=1
    if(i==10):
        break
txt.close()