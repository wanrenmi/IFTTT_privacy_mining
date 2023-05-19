import re
import csv
import pandas as pd
txt=open('tmp.txt','w',encoding='utf-8')
csv_data = pd.read_csv("twitter_data_luoyuan1130.csv", usecols=['username', 'tweet'])
# with open("twitter爬虫数据两列.csv",encoding='utf-8') as f:
#     reader = csv.reader(f)
#     rows=[row for row in  reader]
# for i in range(0,len(rows)):
#     # print(rows[i])
#     LIST.append(",".join(rows[i]))
# f.close()
LIST=[]
for i in range(0,len(csv_data)):
    LIST.append([csv_data.loc[i][0],csv_data.loc[i][1]])
for s in LIST:
    i=0
    flag=0#代表本行k里是否找到了第一个逗号
    k=s[1]#仅对tweet内容进行正则过滤
    k = re.sub(r'\?*', "", k)#删除连续乱码问号
    k = re.sub(r'\n*', "", k)#删除行内换行
    k = re.sub(r'[^\u0030-\u0039\u0041-\u005a\u0061-\u007a @().#$,:\[\]\"\'\-]', "", k)#删除特殊字符
    k = re.sub(r'[\'\".\[\]]*http(s)?[a-zA-Z0-9/.?=:]*[\'\".\[\]]*\b', "(a http_link)", k)#替换http链接
    k = re.sub(r'[\'\".\[\]]*pic\.twitter\.com[a-zA-Z0-9/.?=]*[\'\".\[\]]*\b', "(a twitter_link)", k)#替换推特链接
    k = re.sub(r'#[a-zA-Z0-9/@\'\"]*\b', "(a #tag)", k)#替换标签
    k = re.sub(r'\.\.+', "", k)#删除连续句点
    k = re.sub(r',,+', "", k)#删除连续逗号
    k = re.sub(r'[\'\".\[\]]*\(a http_link\)[\'\".\[\]]*', "(a http_link)", k) #去除链接多余符号
    k = re.sub(r'  +', "", k)#删除连续空格
    #k = re.sub(r'\(a http_link\).*(\b|$)', "(a http_link)", k)
    for i in range(0,len(k)):#转义文本内逗号
        if(k[i]==','):
            flag=1
        if(flag==1):#找到了第一个逗号
            t=list(k)
            t[i+1:]=re.sub(r',', " ", k[i+1:]) #删除剩下的逗号
            k = ''.join(t)
            break
    txt.write(s[0]+','+k+'\n')
txt.close()
preprocess_result=open('preprocess_result.txt','w',encoding='utf-8')
txt=open('tmp.txt','r',encoding='utf-8')
lines=txt.readlines()
for line in lines:
    if line[0] !=' ' and line[0]!='\n':
        preprocess_result.write(line)
txt.close()
preprocess_result.close()