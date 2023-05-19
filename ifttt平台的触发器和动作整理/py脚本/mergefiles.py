#把1的内容写入2中
json_data=open('recipes7.json', encoding='utf-8').read()#1
aim_f = open('recipes1.json', 'a', encoding='utf-8')#2
aim_f.write(json_data)