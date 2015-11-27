
import json
import csv
from opencage.geocoder import OpenCageGeocode

key = 'c4a90be25d0047b2fa64faaaf456b1cc'
geocoder = OpenCageGeocode(key)

i = 0

results = {}

with open('Roads_Nodes.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    values = {}
    for row in reader:
        print(row['Start Node'], row['End Node'], row['Via'])
        values['Start_Node_Cords'] = row['Start Node']
        values['End_Node_Cords'] = row['End Node']
        values['Via_Cords'] = row['Via']
        results[i] = {}
        for key,value in values.iteritems():
            query = value
            results[i][key] = "No Cords"
            print "Querying . . . "
            result = geocoder.geocode(query)
            for res in result:
                if "Tanzania" in res['formatted'] and row['District'] in res['formatted']:
                    lat = res['geometry']['lat']
                    lng = res['geometry']['lng']
                    results[i][key] = str(lat)+','+str(lng)
        if i == 5:
            break
        i = i + 1

   
with open('Results.csv', 'w') as csvfile:
    fieldnames = ['Start_Node_Cords', 'End_Node_Cords', 'Via_Cords']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for key , end_result in results.iteritems():
        writer.writerow({'Start_Node_Cords': end_result['Start_Node_Cords'] ,'End_Node_Cords': end_result['End_Node_Cords'],'Via_Cords': end_result['Via_Cords']})






