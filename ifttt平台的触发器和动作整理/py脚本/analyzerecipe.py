

import json



actions_to_triggers = dict()
triggers_to_actions = dict()

with open('recipes.json') as json_file:
	for line in json_file:
		data = json.loads(line)
		trigger = data['triggerChannelTitle']
		action = data['actionChannelTitle']
		#print trigger, type(trigger)
		if not trigger in triggers_to_actions.keys():
			triggers_to_actions[trigger] = list()
			triggers_to_actions[trigger].append(action)

		else:
			if not action in triggers_to_actions[trigger]:
				triggers_to_actions[trigger].append(action)

		#print triggers_to_actions
		#-----------------------------------
		if not action in actions_to_triggers.keys():
			actions_to_triggers[action] = list()
			actions_to_triggers[action].append(trigger)
		else:
			if not trigger in actions_to_triggers[action]:
				actions_to_triggers[action].append(trigger)

		#print actions_to_triggers



for key in triggers_to_actions.keys():
	print(key)
	print(triggers_to_actions[key])
	print( "--------------------------")


print( "=========================")
for key in actions_to_triggers.keys():
	print( key)
	if key == u'Twitter':
		print( "found twitter")
	print( actions_to_triggers[key])
	print( "--------------------------")


print( "*************************")

twittertriggerlist = actions_to_triggers[u'Twitter']
for trigger in twittertriggerlist:
	if trigger in actions_to_triggers.keys():
		firsttrigger = actions_to_triggers[trigger]
		print( firsttrigger)
		print( trigger, " -> Twitter")
		print( "-------------------")





