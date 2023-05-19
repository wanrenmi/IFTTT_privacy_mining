import json
file='result.json'
searchkey='triggerChannelTitle'
value='Blogger'#Blogger，Android SMS，Beeminder，Evernote
f=open(file,'r',encoding='utf-8')
data=json.load(f)
f.close()
count=1
for dict_data in data:
    if(dict_data[searchkey]==value):
        print(str(count)+':\n'+'trigger名为：'+dict_data['triggerChannelTitle']+'\n''action名为：'+dict_data['actionChannelTitle']+'\n'
              '该app的链接为：'+dict_data['url']+'\n')
        count+=1

