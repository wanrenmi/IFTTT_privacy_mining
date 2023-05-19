import glob
from csv_diff import load_csv, compare
import pandas as pd
import numpy as np
import csv




differences = dict()



def comparefile(file1, file2, flag):
	#print("compare two files")
	filename1 = file1.split("/")[6]
	enddate1 = filename1.split("_")[1][:-4]
	filename2 = file2.split("/")[6]
	enddate2 = filename2.split("_")[1][:-4]
	#print(enddate1, enddate2)

	#file2 is more recent
	if "xiaoyu" in flag:
		diff = compare(load_csv(open(file1), key="id"), load_csv(open(file2), key="id"))
		firstdate = enddate1
		seconddate = enddate2
	#file1 is more recent
	else:
		diff = compare(load_csv(open(file2), key="id"), load_csv(open(file1), key="id"))
		firstdate = enddate2
		seconddate = enddate1

    

	#print(diff["removed"])
	for diffitem in diff["removed"]:
		diffdetailitem = dict()
		#print( diffitem["id"])
		if diffitem["id"] not in differences.keys():
			diffdetailitem["startdate"] = firstdate
			diffdetailitem["existdate"] = firstdate
			diffdetailitem["nonexistdate"] = seconddate
			differences[diffitem["id"]] = diffdetailitem
		else:
			if firstdate > differences[diffitem["id"]]["existdate"]:
				differences[diffitem["id"]]["existdate"] = firstdate
			if firstdate < differences[diffitem["id"]]["startdate"]:
				differences[diffitem["id"]]["startdate"] = firstdate
			if seconddate < differences[diffitem["id"]]["nonexistdate"]:
				differences[diffitem["id"]]["nonexistdate"] = seconddate
			

	











folderpath = "/home/luoyuan/Downloads/twitterIFTTT/sanfranciscobackup/*.csv"
comparecache = "/home/luoyuan/Downloads/twitterIFTTT/comparecache"
filelist = list()

filelist = glob.glob(folderpath)
#print filelist

flag = "xiaoyu"
comparecacheread = dict()
comparecachewrite = dict()

with open(comparecache, 'rt') as f:
	reader = csv.reader(f)
	for row in reader:
		#print(row)
		key =  row[0]
		comparecacheread[key] = row[1:]

print(comparecacheread)
#print(comparecacheread['2019-11-22 23:44:36'], type(comparecacheread['2019-11-22 23:44:36']))




for file1 in filelist:
	#print(file1.split("/"))
	#input()
	filename1 = file1.split("/")[6]
	startdate1 = filename1.split("_")[0]
	enddate1 = filename1.split("_")[1][:-4]
	#print enddate1
	for file2 in filelist:
		filename2 = file2.split("/")[6]
		startdate2 = filename2.split("_")[0]
		enddate2 = filename2.split("_")[1][:-4]
		if enddate2 > enddate1:
			#print enddate1, enddate2, "<"
			flag = "xiaoyu"

			if enddate1 in comparecacheread.keys() and enddate2 in comparecacheread[enddate1]:
				print(enddate1, " ", enddate2, " already compared")
			else:
				if enddate1 not in comparecacheread.keys():
					comparecacheread[enddate1] = list()
					comparecacheread[enddate1].append(enddate2)
				else:
					comparecacheread[enddate1].append(enddate2)
				comparefile(file1, file2, flag)

		# elif enddate2 < enddate1:
		# 	#print enddate1, enddate2, ">"
		# 	flag = "dayu"
		# 	comparefile(file1, file2, flag)


filepath = folderpath[:-5]
resultfile = "/home/luoyuan/Downloads/twitterIFTTT/compareresult.csv"
f = open(resultfile, 'a') 
#print(differences)
for item in differences.keys():
	print(item)
	filename = str(filepath) + "2019-11-21 00:00:00_" + str(differences[item]['existdate']) + ".csv"
	#print(filename)
	df = pd.read_csv(filename)
	result = df[df['id'] == np.int64(item)]
	result.to_csv(f, header = False)
	
	#print(result)
	print(differences[item])

f.close()

#print(comparecacheread)
w = csv.writer(open(comparecache, "w"))
for key in comparecacheread.keys():
    w.writerow([key] + comparecacheread[key])




