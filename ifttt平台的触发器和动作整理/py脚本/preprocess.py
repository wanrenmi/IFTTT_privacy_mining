import json
file='test.json'
f=open(file,'r',encoding='utf-8')
i=0
txts=f.read()
f.close()
txts=list(txts)
txts.insert(0,'[')
txts.append(']')
for char in txts:
    i+=1
    if(char=='}'):
        txts.insert(i,',')
    if(char=='\n'):
        del txts[i-1]
    if(char==']'):
        del txts[i-2]
out=''.join(txts)
f=open('test.json','w',encoding='utf-8')
f.write(out)
f.close()
