import glob
from csv_diff import load_csv, compare

differences = dict()



def comparefile(file1, file2, flag):
	#print("compare two files")
	filename1 = file1.split("/")[4]
	enddate1 = filename1.split("_")[1][:-4]
	filename2 = file2.split("/")[4]
	enddate2 = filename2.split("_")[1][:-4]
	print(enddate1, enddate2)

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

    

	print(diff["removed"])
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
			

	











folderpath = "/root/twitterIFTTT/twitter/*.csv"
filelist = list()

filelist = glob.glob(folderpath)
#print filelist

flag = "xiaoyu"

for file1 in filelist:
	filename1 = file1.split("/")[4]
	startdate1 = filename1.split("_")[0]
	enddate1 = filename1.split("_")[1][:-4]
	#print enddate1
	for file2 in filelist:
		filename2 = file2.split("/")[4]
		startdate2 = filename2.split("_")[0]
		enddate2 = filename2.split("_")[1][:-4]
		if enddate2 > enddate1:
			#print enddate1, enddate2, "<"
			flag = "xiaoyu"
			comparefile(file1, file2, flag)
		elif enddate2 < enddate1:
			#print enddate1, enddate2, ">"
			flag = "dayu"
			comparefile(file1, file2, flag)


#print(differences)
for item in differences.keys():
	print(item)
	print(differences[item])

