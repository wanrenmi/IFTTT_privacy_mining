#打印详细信息，考虑trigger，triggerchanneltitle会有重复
# import json
# file='result.json'
# searchkey='actionChannelTitle'
# value='Twitter'#Blogger，Android SMS，Beeminder，Evernote
# f=open(file,'r',encoding='utf-8')
# data=json.load(f)
# f.close()
# f=open('twitter作为action的所有app信息.txt','w',encoding='utf-8')
# count=1
# for dict_data in data:
#     if(dict_data[searchkey]==value):
#         f.write(str(count)+':\n'+'triggerChannelTitle为：'+dict_data['triggerChannelTitle']
#               +'\n''actionChannelTitle为：'+dict_data['actionChannelTitle']
#               +'\n该app的链接为：'+dict_data['url']
#               +'\ntrigger为：'+dict_data['triggerTitle']
#               +'\naction为：'+dict_data['actionTitle']+'\n\n')
#         count+=1
# f.close()


#///////////////////////////////////////////////////////////////////////////////


#只考虑triggerchanneltitle，tct不会有重复
import json
file='result.json'
searchkey='actionChannelTitle'
value='Twitter'#Blogger，Android SMS，Beeminder，Evernote
f=open(file,'r',encoding='utf-8')
data=json.load(f)
f.close()
f=open('twitter作为action的所有trigger统计.txt','w',encoding='utf-8')
triggerchannellist=list()
for dict_data in data:
    if dict_data[searchkey]==value and dict_data['triggerChannelTitle'] not in triggerchannellist:
        triggerchannellist.append(dict_data['triggerChannelTitle'])

for item in triggerchannellist:
    f.write(item+',\n')

f.close()