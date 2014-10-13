import database_pytools_v1 as db
import pandas as pd
import itertools as it
import math

db.open("sbider1.db")
db.make_db()
path = "/Users/K/Desktop/SBiDer_Database.xlsx"

def id_abbrev(table_name):
	if table_name in ('plasmid','operon','species'):
		return table_name[0:3]
	elif table_name == 'op':
		return 'op'
	elif table_name == 'ot':
		return 'ot'
	elif table_name == 'in':
		return 'in'
	elif table_name == 'out':
		return 'out'	

def table_id_dict(table_name):
    """
    Returns:
        a dictionary of the table with the key_col
        as the column used for indexing and
        row_col is the value.
    """
    id = id_abbrev(table_name) + '_id'
    table_list = db.select(table_name, [id, 'name'])
    table_dict = {}
    for _id, name in table_list:
        table_dict[name] = _id
    return table_dict
        

def format_values(row):
    """Formats the values a given row based on the python types needed for 
    	proper sql insertion and update.
    """
    new_row = []
    for item in row:
            if isinstance(item, unicode):
                #print 'unicode change b', item
            	new_row.append(str(item))
                #print 'unicode change a', item
            elif math.isnan(item):
                #print 'nan change b', item
                new_row.append("na")
                #print 'nan change a', item
            elif isinstance(item, float):
                #print 'float changer b', item
                new_row.append(int(item))
                #print 'float changer a', item
            else:
            	new_row.append(item)
    #print 'what is the new row?', new_row
    return new_row
            

data = pd.io.excel.read_excel(path, "database")

#making the plasmid table DONE!
print '\n' * 2, 'Making the PLASMID TABLE', '\n' * 2
plasmid = data[['P_ID','P_Name', 'Title', 'Authors', 'Journal', 'Year']]
plasmid_t = plasmid.values.T.tolist()
plasmid_t = [row for row in it.izip(*plasmid_t)]

plasmid_done = []
for row in plasmid_t:
    row = list(row)
    row = format_values(row)
    if str(row[0]) not in plasmid_done:
    	#print 'The value of row[0] is', row[0]
    	#print 'The current plasmid done is', plasmid_done
    	db.insert('plasmid', ['pla_id', 'name', 'title', 'authors', 'journal', 
    		'year'], row)
    	plasmid_done.append(str(row[0]))
print plasmid_done
plasmid_dict = table_id_dict('plasmid')


#making the operon table DONE!
print '\n' * 2, 'Making the OPERON TABLE', '\n' * 2
operon = data[data['O_ID'] != ""]
operon = operon[['O_ID', 'Structure']]
operon_t = operon.values.T.tolist()
for row in it.izip(*operon_t):
    row = list(row)
    #print 'printing row before formmating', row
    row = format_values(row)
    #print 'printing row after formmating', row
    #print row
    if row[0] != 'na':
    	db.insert('operon', ['ope_id', 'name'], [row[0], row[1]])
operon_dict = table_id_dict('operon')


#making the species table DONE!
print '\n' * 2, 'Making the SPECIES TABLE', '\n' * 2
species = data[data['O_ID'] != ""]
domain = species[['Domain']]
range = species[['Range']]
species = domain.values.T.tolist()[0] + range.values.T.tolist()[0]
species = set(species)
species = list(species)
species.sort()
#print 'species current looks like this', species
#print 'what type is species', type(species)
count = 1
inserted_species = []
for row in species:
    row = format_values([row])[0]
    row = row.split(',')
    #print row
    for item in row:
    	if item.strip() not in inserted_species:
    		db.insert('species', ['spe_id', 'name'], [count, item.strip()])
    		count = count + 1
    		inserted_species.append(item.strip())
species_dict = table_id_dict('species')
            
            
#making the operon-plasmid table DONE!
#print '\n' * 2, 'Making the OPERON-PLASMID TABLE', '\n' * 2
op = data[['P_ID', 'O_ID', 'R/L']]
#print 'The op initial data', op
op_t = op.values.T.tolist() 
#print 'The op list data', op_t 
count = 1
for row in it.izip(*op_t):
    row = list(row)
    #print 'The value of the op row data', row
    #print 'The length of the op row data', len(row)
    row = format_values(row)
    #print 'The value of the op row data after formatting', row
    if row[1] != 'na': 
		db.insert('op', ['op_id', 'ope_id', 'pla_id', 'direction'], 
		[count, row[1], row[0], row[2]])
		count = count + 1
            
#making all of the transitions
print '\n' * 2, 'Making the TRANSITIONS DICTIONARY', '\n' * 2
#1 Get the data
#2 Get all of the domains 
#3 Sort the domains
#4 Get complete set of domains by using a set
#5 Sort the list
#5 Make a dictionary for transition id's. Key: domain, Value: id


domains = data[['Domain']]
#print 'The initial domains data', domains, '\n' * 3
domains = domains.values.T.tolist()[0]
#print 'The listed domains data', domains, '\n' * 3
domains = [str(x) for x in domains if not isinstance(x, float)]
#print 'The stringifying the domains data and removing nan', domains, '\n' * 3
domains = set(domains)
#print 'The duplicate removing process using a set', domains, '\n' * 3
domains = list(domains)
domains.sort()
#print 'The relisting and sorting of the values', domains, '\n' * 3
trans_dict = {}
count = 2
#print 'domains is type', type(domains)
for item in domains:
	trans_dict[item.strip()] = count 
	count = count + 1
trans_dict['na'] = 1
'''print 'The transitions dictionary finished'
for x, y in trans_dict.items():
	print '\n'
	print 'key:', x
	print 'key:', y
	print '\n' 
'''

#making the Operon-Transition table DONE!
print '\n' * 2, 'Making the OPERON-TRANSITION TABLE', '\n' * 2
ot = data[['Structure', 'Domain', 'O_ID']]
#print 'The intial ot data', ot, '\n' * 3
ot_t = ot.values.T.tolist()
#print 'The listed ot data', ot_t, '\n' * 3
count = 1
for row in it.izip(*ot_t):
	#print '\nRows inside of the ot data', row
	row = format_values(row)
	#print 'Rows inside of the ot data after formmating', row, '\n' * 3
	if row[2] != 'na':
		db.insert('ot', ['ot_id', 'ope_id', 'tra_id'], 
			[count, row[2], trans_dict[row[1]]])
	count = count + 1

#making the In Operon-Species table DONE (for now)!
print '\n' * 2, 'Making the IN TABLE', '\n' * 2
#going to need fixing for the not column. UPDATE LATER!
#in_ = ot[['Domain']]
#in_t = in_.values.T.tolist()
#in_t.sort()
#print 'The values int in_t are', in_t
count = 1
#print "The value of domains", domains
#print "The transitions_dict has the following values", transitions_dict
#print "The species_dict as the following values", species_dict
in_ = data[['Domain']]
#print '\n\nThe in data', in_
in_ = in_.values.T.tolist()[0]
#print '\n\nThe listed in data', in_
in_ = format_values(in_)
#print '\n\nThe formatted data', in_
in_ = [x.strip() for x in in_ if x != 'na']
#print '\n\nThe nas are removed', in_
in_ = set(in_)
#print '\n\nThe duplicate values are removed',in_
in_ = list(in_)
in_.sort()
#print '\n\nReturning back to a list', in_
count = 1
for trans in in_:
	species = trans.split(',')
	for spe in species:
		db.insert('input', ['in_id', 'tra_id', 'spe_id'],
				[count, trans_dict[trans.strip()], species_dict[spe.strip()]])
		count = count + 1
			 
#making the Out Operon-Species table DONE!
print '\n' * 2, 'Making the OUT TABLE', '\n' * 2
out = data[['O_ID','Structure', 'Range']]
#print 'The full data set', out
out_t = out.values.T.tolist()
#print 'The listed data', out_t
count = 1
for row in it.izip(*out_t):
	#print 'Each row before formatting', row
	row = format_values(row)
	#print 'Each row after formmating', row
	if row[0] != 'na':
		ope = row[1]
		species = row[2].split(',')
		for spe in species:
			db.insert('output', ['out_id', 'ope_id', 'spe_id'],[count, 
				operon_dict[ope], species_dict[spe]])
		count = count + 1
db.close()


db.open('sbider1.db')

print '\n' * 2, 'Printing the PLASMID TABLE'
db.print_table('plasmid')

print '\n' * 2, 'Printing the OPERON TABLE'
db.print_table('operon')

print '\n' * 2, 'Printing the species TABLE'
db.print_table('species')

print '\n' * 2, 'Printing the OP TABLE'
db.print_table('op')

print '\n' * 2, 'Printing the TRANSITION DICTIONARY'
print trans_dict

print '\n' * 2, 'Printing the OT TABLE'
db.print_table('ot')

print '\n' * 2, 'Printing the INPUT TABLE'
db.print_table('input')

print '\n' * 2, 'Printing the OUTPUT TABLE'
db.print_table('output')

db.close()


