

import json


import sys



# searchtrigger = u'Google Assistant'
searchtrigger = u'Android Phone Call'
searchaction =  u'Twitter'

with open('recipes.json') as json_file:
	for line in json_file:
		data = json.loads(line)
		trigger = data['triggerChannelTitle']
		action = data['actionChannelTitle']
		if searchtrigger == trigger and searchaction == action and data['desc']!='':
			print(data['title']+'\n'+data['desc']+data['url']+'\n\n')