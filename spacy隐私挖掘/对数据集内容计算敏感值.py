import spacy
import re
import pandas as pd
import time
start=time.time()

nlp = spacy.load('en_core_web_lg')
f=open("sensitive_words.txt",'r',encoding='UTF-8')
txt=f.readline()
f.close()
sensitive_words=nlp(re.sub(r',',' ',txt))


mat = "{:20}\t{:800}"

csv_data = pd.read_csv(r"C:\罗元项目相关\twitter数据\twitter"
                       r"\2019-11-21 00_00_00_2019-12-01 12_46_48.csv",
                       usecols=[ 'tweet'],engine='python')
LIST=[]
for i in range(0,len(csv_data)):
    LIST.append(csv_data.loc[i][0])

duanju=LIST

sum_tweet=list()
for tweet_txt in duanju:
    tweet_txt=re.sub(r'[^\u0030-\u0039\u0041-\u005a\u0061-\u007a .,]', "", tweet_txt)
    tweet = nlp(re.sub(r'\n','',tweet_txt))
    sum = 0.0
    for word in sensitive_words:
        for tweet_word in tweet:
            if word.similarity(tweet_word) > 0.9:
                sum = sum + word.similarity(tweet_word)*5
            else:
                sum = sum + word.similarity(tweet_word)*0.01
    sum_tweet.append([sum,re.sub(r'\n','',tweet_txt)])

f=open("csv内容敏感值计算结果.txt",'w',encoding='UTF-8')
sum_tweet.sort(key=lambda x:x[0],reverse=True)
for item in sum_tweet:
    f.write(mat.format(item[0], item[1]) + '\n')
f.close()

end=time.time()
print('Running time: %s Seconds'%(end-start))