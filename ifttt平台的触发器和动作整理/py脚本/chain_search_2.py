import json
file='result.json'
# privatetriggers=['Office 365 Mail','SMS','Gmail','Telegram','Android SMS','Email','Ooma','MailChimp',
#        'Blogger','Evernote','Note widget','MeisterTask','RescueTime','dondeEsta Family','Life360',
#        'Lifelog','Foursquare','Location','Google Assistant','Amazon Alexa','Google Calendar',
#        'Office 365 Contacts','iOS Contacts','Android Phone Call','Phone Call (US only)','Google Contacts',
#        'Office 365 Calendar','Camera widget','Netatmo Security','Beseye','SpotCam HD','Android Photos',
#        'iSecurity+','Manything','Sighthound Video','Oco Camera','Somfy Protect','Arlo','Withings Home',
#        'iOS Photos','Nest Cam','Ivideon','D-Link Connected Home Camera']
privatetriggers=['Blogger']
allPT=[]
f=open(file,'r',encoding='utf-8')
data=json.load(f)
f.close()
# txt=open('blogger作为triggerchannel时两段连接结果_检索了具体action.txt','w',encoding='utf-8')
# txt.write('输出格式为：A --> B --> C，其中AB分别为app1的triggerchannel和actionchannel，'
#           'BC分别为app2的triggerchannel和actionchannel。')
for dict_data in data:
    if(dict_data['triggerChannelTitle'] in privatetriggers):
        allPT.append(dict_data)#A大概在45000个

count=0

for PT in allPT:
    j=0
    for dict_data in data:
        if (PT['actionChannelTitle'] == dict_data['triggerChannelTitle'] and
        PT['actionTitle'] == dict_data['triggerTitle']):#2段连接条件满足
            j+=1
            count+=1
            print('\n'+str(count)+'.'
                  +'\n信息流为'+PT['triggerChannelTitle']+' --> '+PT['actionChannelTitle']+
                  ' --> '+dict_data['actionChannelTitle']
                  # +'\napp1的title为：'+PT['title']
                  # +'\napp1的desc为：'+PT['desc']
                  # +'\napp2的title为：' + dict_data['title']
                  # +'\napp2的desc为：' + dict_data['desc']
                  )
        if(j==50):#每个A->B对应的C不超过50个
            break
# txt.close()