# functon return YES is tag is found in "about"
def isOrNot(about, tag):
	if tag in about:
		return "YES"
	else:
		return "NO"
			
import json

jdata = open('test.json')
pdata = json.load(jdata)

print("Does first tag match with description?")
i = 0 
while i < 5: # number of customers
	# prints full name of customer followed by country code
	print(pdata[i]['name']['first'] + " " + pdata[i]['name']['last'] + ": " + isOrNot(pdata[i]['about'], pdata[i]['tags'][0]))
	i += 1


			

