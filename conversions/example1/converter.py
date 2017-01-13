import csvmapper
from pprint import pprint
import json

# load the file
parser = csvmapper.CSVParser('result.csv', hasHeader=True)
rows = parser.buildObject()

# make an empty list
json_data = []
for row in rows:
	# define how to translate the CSV to correct type of JSON
	item =  {
		"title": row.title ,
		"subtitle":row.subtitle,
		"ranges":[float(row.ranges0),float(row.ranges1),float(row.ranges2)],
		"measures":[float(row.measures0),float(row.measures1)],
		"markers":[float(row.markers0)]
	}
	# add to the empty list
	json_data.append(item)

# print it to the terminal
pprint(json_data)

# output to json
with open('output.json', 'w') as jsonfile:
	json.dump(json_data, jsonfile, indent=4)