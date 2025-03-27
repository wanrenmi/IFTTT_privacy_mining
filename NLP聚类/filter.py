from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
f=open("remove_duplicates.txt",'w',encoding='utf-8')
# writer=csv.writer(f)
lists=[]#二维列表，每一行有两个list，分别是username和twitter
blacklist=['jenette_fabian','ritu','califdreamhomes','onlinerepzen','zenniegeek','iamtootallstew',
           'moemaka','oaklandnews4you','hainesforsf','castrolgbtq','101_racism','sfhourly','sfo_cip',
           'oaklandnews4you','mariaayerdi','newsvlogger','bayareaauction1','sfhourly','eroticawild',
           '7longgame']#按用户名过滤无效内容
Input=[]
resultfile=open('preprocess_result.txt','r',encoding='utf-8')
documents=resultfile.readlines()
resultfile.close()

for i in range(0,len(documents)):
    flag=0
    for j in range(0,len(documents[i])):
        if(documents[i][j]==','):
            flag=1
        if(flag==1):
            tmp = [documents[i][0:j],documents[i][j+1:]]
            lists.append(tmp)
            break
for i in range(0,len(lists)):
    Input.append(lists[i][1])
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(Input)

true_k = 30 #聚类数
model = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1)
model.fit(X)
result=list(model.fit_predict(X))


for i in range(0,true_k):
    for j in range(0,len(result)):
        if(result[j]==i and lists[j][0] not in blacklist):
            f.write(str(lists[j][0])+','+str(lists[j][1]))

f.close()






