import database_pytools as db
import pandas as pd
import itertools as it
import math

db.open("sbider.db")
db.make_db("lkj")
path = "/Users/K/Desktop/SBiDer_Database.xlsx"

def table_id_dict(table_name):
    """
    Returns:
        a dictionary of the table with the key_col
        as the column used for indexing and
        row_col is the value
    """
    table_list = db.select(table_name, ['id', 'name'])
    table_dict = {}
    for _id, name in table_list:
        table_dict[name] = _id
    return table_dict
        

def format_values(row):
    """ formats the values a given row based on the python types needed for 
        proper sql insertion and update
    Returns:
        a new list with the values formatted accordingly
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
    return new_row
            
#making the plasmid table
plasmid = pd.io.excel.read_excel(path, "database")
plasmid = plasmid[['P_ID','P_Name', 'Title', 'Authors', 'Journal', 'Year']]
plasmid_t = plasmid.values.T.tolist()

for row in it.izip(*plasmid_t):
    row = list(row)
    if not (math.isnan(row[0])):
        row = format_values(row)
        print row
        db.insert('plasmid', ['id', 'name', 'title', 'authors', 'journal', 
            'year'], row)
plasmid_dict = table_id_dict('plasmid')
            
#making the operon table
operon = pd.io.excel.read_excel(path, "plasmid")
operon = operon[['O_ID', 'Structure']]
operon_t = operon.values.T.tolist()

for row in it.izip(*operon_t):
    row = list(row)
    row = format_values(row)
    if row[0] != 'na':
        db.insert('operon', ['id', 'name'], row)
operon_dict = table_id_dict('operon')        
            
#making the part table
part = pd.io.excel.read_excel(path, 'part')
part_t = part.values.T.tolist()

for row in it.izip(*part_t):
    row = list(row)
    row = format_values(row)
    db.insert('part', ['id', 'name'], 
        row)        
#making a part dict
part_dict = table_id_dict("part")

#making the interactor table
interactor = pd.io.excel.read_excel(path, 'interactor')
interactor = interactor[['id', 'name']]
interactor_t = interactor.values.T.tolist()

for row in it.izip(*interactor_t):
    row = list(row)
    row = format_values(row)
    db.insert('interactor', ['id', 'name'], row)
#making a interactor dict
interactor_dict = table_id_dict("interactor")
        

#making the input transition table     
inputt = pd.io.excel.read_excel(path, 'input')
input_t = inputt.values.T.tolist()

for row in it.izip(*input_t):
    row = list(row)
    row = format_values(row)
    db.insert('input', ['id', 'interactor_id'], row)
#making an input dict
#input_dict = table_id_dict('input')  

#making the output transition table
output = pd.io.excel.read_excel(path, 'output1')
output_t = output.values.T.tolist()

for row in it.izip(*output_t):
    row = list(row)
    row = format_values(row)
    db.insert('output', ['id', 'interactor_id'], 
        row)
#making an input dict
#input_dict = table_id_dict('input')

#making the opr table
opr = pd.io.excel.read_excel(path, 'opr')
opr_t = opr.values.T.tolist()

for row in it.izip(*opr_t):
    row = list(row)
    row = format_values(row)
    db.insert('opr', ['id', 'plasmid_id', 'operon_id'], 
        row)
        
#making the oitr table        
oitr = pd.io.excel.read_excel(path, 'database')
oitr = oitr[["O_ID", "Domain"]]
oitr_t = oitr.values.T.tolist()

count = 1
for row in it.izip(*oitr_t):
    row = list(row)
    row = format_values(row)
    interactors = row[1].split(',')
    if not isinstance(row[0], float) and row[0] != 'na':
        for item in interactors:
            clean_item = item.strip()
            print "Print the interacting molecule", clean_item
            print "Checking if molecule", clean_item, "is in the dictionary", clean_item in interactor_dict
            if clean_item in interactor_dict:
                db.insert('oitr', ['id', 'operon_id', 'interactor_id'], 
                    [count, row[0], interactor_dict[clean_item]])
            else:
                db.insert('oitr', ['id', 'operon_id', 'interactor_id'], 
                    [count, row[0], "none"] )
            count = count + 1

#making the ootr table        
ootr = pd.io.excel.read_excel(path, 'database')
ootr = ootr[["O_ID", "Range"]]
ootr_t = ootr.values.T.tolist()

count = 1
for row in it.izip(*ootr_t):
    row = list(row)
    row = format_values(row)
    interactors = row[1].split(',')
    if not isinstance(row[0], float) and row[0] != 'na':
        for item in interactors:
            clean_item = item.strip()
            print "Print the interacting molecule", clean_item
            print "Checking if molecule", clean_item, "is in the dictionary", clean_item in interactor_dict
            if clean_item in interactor_dict:
                db.insert('ootr', ['id', 'operon_id', 'interactor_id'], 
                    [count, row[0], interactor_dict[clean_item]])
            else:
                db.insert('ootr', ['id', 'operon_id', 'interactor_id'], 
                    [count, row[0], "none"] )
            count = count + 1
            
#making the oprt table
oprt = pd.io.excel.read_excel(path, 'database')
oprt = oprt[['O_ID', 'Structure']]
oprt_t = oprt.values.T.tolist()

count = 1
for row in it.izip(*oprt_t):
    row = list(row)
    row = format_values(row)
    row[1] = row[1].replace('--->', '+')
    row[1] = row[1].replace('<---', '+')
    row[1] = row[1].split('+')
    print "Operon:", row[0]
    for item in row[1]:
        print "Part:", item
        if row[0] is not 'na' and item in part_dict:
            db.insert('optr', ['id', 'operon_id', 'part_id'], [count, row[0], part_dict[item]])
            count = count + 1

db.close()
