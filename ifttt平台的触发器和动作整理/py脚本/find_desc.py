#打印方便阅读的结果
import json
import re
f=open('twitter作为action的所有和隐私有关的trigger统计.txt','r',encoding='utf-8')
triggers=f.readlines()
f.close()
f=open('result.json')
datas=json.load(f)
f.close()
count=1
num=0
for trigger in triggers:
    trigger = re.sub(r'\n', '', trigger)
    print(str(count)+'. '+trigger+'\n')
    for data in datas:
        if trigger==data['triggerChannelTitle'] and data['actionChannelTitle']=='Twitter' and data['desc']!='':
            print('    '+data['desc']+'\n------------------------------------------------------------------------')
            num+=1
    count+=1
    print('###########################################################################################\n\n')
print(num)




