import pandas as pd
csv_file = "tweet5.csv"
column_name = "username"
f=open('ceshi.txt','w',encoding='utf-8')
df = pd.read_csv(csv_file)
username = df.iloc[:,7]
tweetnumber = username.shape[0]
f.write(csv_file+" tweets number: "+ str(tweetnumber)+'\n')
#print username, type(username)
#input()
usernamecount = dict()
mat = "{:15}\t{:20}"
for i in range(tweetnumber):
	if username[i] in usernamecount.keys():
		usernamecount[username[i]] = usernamecount[username[i]] + 1
	else:
		usernamecount[username[i]] = 1
for username in usernamecount.keys():
	if  usernamecount[username] <= 5:#正常情况打印所有条目
		f.write("----------------------------------------------------------------------------------"
				"-----------------------------------------------------------------" + '\n')
		f.write(mat.format(username, 'sum=' + str(usernamecount[username])) + '\n\n')
		selectedrow = df.loc[df.iloc[:,7] == username]
		for j in range(usernamecount[username]):
			f.write('tweet:' + selectedrow.iloc[j, 10] + '\n')
			f.write('link:' + selectedrow.iloc[j, 19] + '\n\n')


	else:#如果认为是公众号就只打印第一个条目
		f.write("----------------------------------------------------------------------------------"
				"-----------------------------------------------------------------" + '\n')
		f.write(mat.format(username, 'sum=' + str(usernamecount[username])) + '\n\n')
		f.write('maybe an ad!!!!!!!!!!!!!!!!!!!!!!!\n')
		selectedrow = df.loc[df.iloc[:, 7] == username]
		f.write('tweet:' + selectedrow.iloc[0, 10] + '\n')
		f.write('link:' + selectedrow.iloc[0, 19] + '\n')
		pass
f.close()
		




