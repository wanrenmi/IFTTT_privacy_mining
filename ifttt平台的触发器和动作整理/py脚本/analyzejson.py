import json


filename = 'recipes.json'
result = dict()
count = 500
tmp = 0

with open(filename) as json_file:
	for line in json_file:
		recipe = json.loads(line)
		trigger = recipe['triggerChannelTitle']
		action = recipe['actionChannelTitle']
		if trigger in result.keys():
			if action not in result[trigger]:
				result[trigger].append(action)
		else:
			result[trigger] = [action]

		# if tmp > count:
		# 	break

		# tmp = tmp + 1

# for trigger in result.keys():
# 	print trigger.encode('utf-8')
# 	print result[trigger]
# 	print "------------------------------------------------"
#
#
#