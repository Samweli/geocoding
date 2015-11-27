
import json
import csv
from opencage.geocoder import OpenCageGeocode

key = 'c4a90be25d0047b2fa64faaaf456b1cc'
geocoder = OpenCageGeocode(key)


i = 0

with open('Roads_Nodes.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	values = {}
	for row in reader:
		print(row['Start Node'], row['End Node'], row['Via'])
		values['Start_Node'] = row['Start Node']
		values['End_Node'] = row['End Node']
		values['Via'] = row['Via']

		for key,value in values.iteritems():
			query = value
            print "Querying . . . \n"
            result = geocoder.geocode(query)

	        for res in result:
	        	if "Tanzania" in res['fomartted'] || row['District'] in res['formatted']:
	        		lat = res['geometry']['lat']
	        		lng = res['geometry']['lng']

		if i == 5:
			break
		i = i + 1






