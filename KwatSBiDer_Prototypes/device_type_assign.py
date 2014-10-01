import * from csv

with open('linhs_db','r') as old, open('linhs updated', 'w') as update:
    csv_old = csv_reader(old)
    csv_update = csv_writer(update)
    header = csv_old.read()
    header.append('Components_wType')
    csv_update.writerow(header)
    
    for row in csv_old:
        components = row[1]
        dtypes = row[8]
        concat = []
        for comp, dts in components, dtypes:
            csv_update.writerow(row[0:] + [dts + ":" + comp])