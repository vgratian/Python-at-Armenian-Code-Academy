import json

jdata = open('test.json')
pdata = json.load(jdata)

print("Replacing 'range' with age of customer... Done!")
i = 0 
while i < 5: # number of customers
	# changes range into the valeu of age
	pdata[i]['range'] = pdata[i]['age']	
	# prints full name of customer followed by range 
	print(pdata[i]['name']['first'] + " " + pdata[i]['name']['last'] + ": ")
	print(pdata[i]['range'])	
	i += 1


