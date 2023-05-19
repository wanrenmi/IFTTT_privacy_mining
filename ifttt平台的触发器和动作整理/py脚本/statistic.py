import json
file='result.json'
alltriggers=[]
f=open(file,'r',encoding='utf-8')
data=json.load(f)
f.close()
txt=open('ceshi.txt','a',encoding='utf-8')
for dict_data in data:
    alltriggers.append(dict_data['triggerChannelTitle'])
alltriggers=list(set(alltriggers))
txt.write('\n共有'+str(len(alltriggers))+'个trigger')
for trigger in alltriggers:
    txt.write('\n在trigger为' + trigger + '时，对应的前50个applet如下：\n')
    i=0
    for dict_data in data:
        if (trigger == dict_data['triggerChannelTitle']):
            txt.write(str(i+ 1) + ':\n该applet的title为：'+ dict_data['title']+'\n其链接为：' + dict_data['url'] +
                  '\n对应的描述信息为：'+dict_data['desc']+'\n'+'对应的action名为：' +dict_data['actionChannelTitle'] + '\n\n' )
            i += 1
        if(i==50):
            break
txt.close()




