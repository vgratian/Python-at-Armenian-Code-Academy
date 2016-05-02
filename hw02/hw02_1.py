import json

jdata = open('test.json')
pdata = json.load(jdata)

print("Country for each customer:")
i = 0 
while i < 5: # number of customers
	# prints full name of customer followed by country code
	print(pdata[i]['name']['first'] + " " + pdata[i]['name']['last'] + ": " + pdata[i]['phone'][4:7])
	i += 1


