import csv
def get_out_list(row):
	outputs = row[3].strip().split(',')
	return outputs
	
def all_intermediates(row):
	comp = row[1]
	comp = comp.split('+')
	comp = [item for item in comp if not item.endswith('<') and not item.endswith('>')]
	return comp
	
with open('ML_June_2013.txt', 'r') as db, open('ML_June_2013_implicit_output.txt', 'w') as imp:
	csv_db = csv.reader(db, dialect = 'excel-tab')
	header = csv_db.next()
	for row in csv_db:
		out_list = get_out_list(row)
		total_io_list = all_intermediates(row)
		implicit_outputs = [item for item in total_io_list if item not in out_list]
		print ','.join(implicit_outputs)

		
		
		

	 
