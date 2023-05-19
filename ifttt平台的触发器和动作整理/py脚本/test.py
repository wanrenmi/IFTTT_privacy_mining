# mat = "{:20}\t{:28}"
# print(mat.format("占4个长度","占8个长度", "占12长度"))
# #如果需要居中输出在宽度前面加一个^
# mat = "{:^20}\t{:^28}\t{:^32}"
# print(mat.format("占4个长度","占8个长度", "占12长度"))


# import re
# f=open('twitter作为action的所有和隐私有关的trigger统计.txt','r',encoding='utf-8')
# txt=f.read()
# f.close()
# txt=re.sub(r'"','',txt)
# f=open('twitter作为action的所有和隐私有关的trigger统计.txt','w',encoding='utf-8')
# f.write(txt)
# f.close()


from summa import summarizer as sm
from summa import keywords as kw
text = """Automatic summarization is the process of reducing a text document with a \
computer program in order to create a summary that retains the most important points \
of the original document. As the problem of information overload has grown, and as \
the quantity of data has increased, so has interest in automatic summarization. \
Technologies that can make a coherent summary take into account variables such as \
length, writing style and syntax. An example of the use of summarization technology \
is search engines such as Google. Document summarization is another."""
print(kw.keywords(text, split=True,ratio=0.1))

