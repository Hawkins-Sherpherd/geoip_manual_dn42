import csv

PRIMARY_PATH = 'geoip_primary.csv'
MANUAL_PATH = 'geoip_manual.csv'

primary_file = open(PRIMARY_PATH,'r')
manual_file = open(MANUAL_PATH,'r')

primary = csv.reader(primary_file)
manual = csv.reader(manual_file)

rows = []

for row in primary:
    rows.append(row)
for row in manual:
    rows.append(row)

with open('geofeed.csv','w') as geofeed_file:
    writer = csv.writer(geofeed_file, quoting=csv.QUOTE_ALL)
    for row in rows:
        writer.writerow(row)
    primary_file.close()
    manual_file.close()
    geofeed_file.close()