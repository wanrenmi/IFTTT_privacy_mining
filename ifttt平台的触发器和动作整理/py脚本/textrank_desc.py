import json
import re
from summa import keywords as kw
f=open('twitter作为action的所有和隐私有关的trigger统计.txt','r',encoding='utf-8')
triggers=f.readlines()
f.close()
f=open('result.json')
datas=json.load(f)
f.close()
for trigger in triggers:
    trigger = re.sub(r'\n', '', trigger)
    desc = list()
    print(trigger+'\n')
    for data in datas:
        if trigger==data['triggerChannelTitle'] and data['actionChannelTitle']=='Twitter' and data['desc']!='':
            data['desc']=re.sub(r'\n',' ',data['desc'])
            desc.append(data['desc'])
    desc=re.sub(r'[^\u0030-\u0039\u0041-\u005a\u0061-\u007a .]','',str(desc))
    print(kw.keywords(desc, split=True, ratio=0.1))
    print('---------------------------------------------------------------')