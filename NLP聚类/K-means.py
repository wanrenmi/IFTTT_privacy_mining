from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score
import csv
f=open("cluster_results.txt",'w',encoding='utf-8')
# writer=csv.writer(f)
lists=[]#二维列表，每一行有两个list，分别是username和twitter
Input=[]
resultfile=open('remove_duplicates.txt','r',encoding='utf-8')
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
            #lists[i][0]= documents[i][0:j]
            #lists[i][1] = documents[i][j+1:]
            break
for i in range(0,len(lists)):
    Input.append(lists[i][1])
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(Input)

true_k = 30 #聚类数
model = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1)
model.fit(X)
result=list(model.fit_predict(X))

mat = "{:20}\t{:30}\t{:300}"
for i in range(0,true_k):
    f.write('the %dth cluster----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n'% i)
    f.write(mat.format('cluster number', 'username', 'twitter'))
    f.write('\n')
    for j in range(0,len(result)):
        if(result[j]==i):
            f.write(mat.format(str(result[j]), str(lists[j][0]),str(lists[j][1])))
            f.write('\n')

f.close()







# print("Top terms per cluster:")
# order_centroids = model.cluster_centers_.argsort()[:, ::-1]
# terms = vectorizer.get_feature_names()
# for i in range(true_k):
#     print("Cluster %d:" % i),
#     for ind in order_centroids[i, :10]:
#         print(' %s' % terms[ind]),
#     print
# print("\n")



# print("Prediction")
#
# Y = vectorizer.transform(["chrome browser to open."])
# prediction = model.predict(Y)
# print(prediction)
#
# Y = vectorizer.transform(["My cat is hungry."])
# prediction = model.predict(Y)
# print(prediction)