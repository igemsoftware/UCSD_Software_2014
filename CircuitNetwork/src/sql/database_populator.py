import sqlite3
import csv
import sql_pytools as sqlpy
import database_pytools as dbpy
import os
from subprocess import call
from sets import Set
import re

#--------------------parsers--------------------#
            
def parse_plasmid(csv_handle):
    '''
    using the plasmid.txt file, will populate the plasmid table
    '''
    for row in csv_handle:
        dbpy.database_insert("plasmid", ["ID","Name"], row[0:2])
        
def parse_operon(csv_handle):
    '''
    using the operon.txt file, will populate the operon table
    '''
    for row in csv_handle:
        dbpy.database_insert("operon", ["ID","Name"], row[0:2])
        
def parse_parts(csv_handle):
    '''
    using the structure.txt file, will populate the part table
    '''
    part_set = Set()
    for row in csv_handle:
        row = row.strip()
        row = re.sub('--->', ',',row)
        row = re.sub('_', ',', row)
        row = row.split(',')
        print row
        for item in row:
            if item.lower() not in part_set:
                part_set.add(item)
    for num in range(len(part_set)):
        #print ["part", [0,1], [num, part_set.pop()]]
        dbpy.database_insert("part", ["ID", "Name"], [num, part_set.pop()])
        
def parse_interactors(csv_handle):
    '''
    using the interactors.txt file, will populate the interactors table
    '''
    part_dict = {}
    for row in csv_handle:
        for item in row:
            part_dict[item] = True
    part_list = []
    part_list = [item for item in part_dict.keys() if item.lower() not in part_list]
    for num, key in enumerate(part_dict.keys()):
        print ["interactor", [0,1], [num, key]]
        dbpy.database_insert("interactors", [0,1], [num, part_set.pop()])
    
def parse_input(csv_handle):
    '''
    using the input.txt file, will populate the input table
    will need to modify to accomidate for O_ID mapping
    '''
    input_list = []
    idd = 0
    for row in csv_handle:
        inputt = row[1].split(',')
        for mol in inputt:
            input_list.append([idd, mol])
        idd += 1
    for item in input_list:
        print ["input", ["ID","Input"], item]
        dbpy.database_insert("input", ["ID","Input"], item)
        
def parse_output(csv_handle):
    '''
    using the output.txt file, will populate the output table
    '''
    output_list = []
    idd = 0
    for row in csv_handle:
        output = row[1].split(',')
        for mol in output:
            output_list.append([idd, mol])
        idd += 1
    for item in output_list:
        print ["output", ["ID","Input"], item]
        print sqlpy.sql_insert("output", ["ID","Output"], item)
        dbpy.database_insert("output", ["ID","Output"], item)
        
def parse_opr(csv_handle):
    '''
    using the input.txt file, will populate the input table
    '''
    idd = 0
    for row in csv_handle:
        new_row = [idd, row[0][0], row[0], row[1]]
        print sqlpy.sql_insert("opr", ["ID", "Operon_ID", "Plasmid_ID" ], new_row)
        dbpy.database_insert("opr", ["ID", "Operon_ID", "Plasmid_ID", "Direction" ], new_row)
        idd += 1
        
def parse_optr(csv_file):
    '''
    using the optr.txt file, will populate the optr table
    '''
    for row in csv_file:
        pass
        
#--------------------helpers--------------------#        
def which_table(table_list, table_name):
    '''
    decides which table is going to be inserted into
    have to fix it to do more. I have to get it to 
    decide how to parse the information that I pass it.
    It should only return when it has found that out. 
    '''
    print table_name
    for table in table_list:
        if table_name in table:
            return table
            
def parse_allocator(table_name, csv_handle):
    if table_name == "plasmid":
        parse_plasmid(csv_handle)
    elif table_name == "operon":
        parse_operon(csv_handle)
    elif table_name == "part":
        parse_part(csv_handle)
    elif table_name == "input":
        parse_input(csv_handle)
    elif table_name == "output":
        parse_output(csv_handle)
    elif table_name == "opr":
        parse_opr(csv_handle)
    elif table_name == "optr":
        parse_optr(csv_handle)
    elif table_name == "interactors":
        parse_interactor(csv_handle)
                    
#--------------------main--------------------#
def main():
    #Deleting all old information and creating new txt's
    #call(["r", "-f", "database_linh_formmating.r"])
    
    #Setting up all of the csv names to extract the data
    info_names = ["plasmid", "operon", "input", "output", "opr", "structure", "optr", "interactors"]

    ''' 
    Minimally parsing for table insertion
    '''    
    #Creating tables of genetic constructs and interactors
    plasmid = 'CREATE TABLE plasmid (ID VARCHAR(50), Name VARCHAR(50), Miriam_ID VARCHAR(50), Title VARCHAR(50), Authors VARCHAR(50), Journal VARCHAR(50), Year VARCHAR(50));'
    operon = 'CREATE TABLE operon (ID VARCHAR(50), Name VARCHAR(50), Image_Path VARCHAR(50));'
    part = 'CREATE TABLE part (ID VARCHAR(50), Name VARCHAR(50));'
    interactors = 'CREATE TABLE interactor (ID VARCHAR(50),Name VARCHAR(50),Type VARCHAR(50));'
    #Creating tables of transitions that are used for the petri nets
    inputt = 'CREATE TABLE input (ID VARCHAR(50), Input VARCHAR(50), Not_Bool bool);'
    output = 'CREATE TABLE output (ID VARCHAR(50), Output VARCHAR(50));'    
    #Creating tables of relationships
    opr = 'CREATE TABLE opr (ID VARCHAR(50), Operon_ID VARCHAR(50), Plasmid_ID VARCHAR(50), Direction VARCHAR(50), Main NUM(10));'
    ''' 
    Intensive parsing for table insertion
    '''
    optr = 'CREATE TABLE optr (ID VARCHAR(50), Operon_ID VARCHAR(50), Part_ID VARCHAR(50), Position NUM(10));'
    #can use input.txt
    oitr = 'CREATE TABLE oitr (ID VARCHAR(50), Operon_ID VARCHAR(50), Input_Transition_ID VARCHAR(50));'
    #can use output.txt
    ootr = 'CREATE TABLE ootr (ID VARCHAR(50), Operon_ID VARCHAR(50), Output_Transition_ID VARCHAR(50));'
    
    
    table_list =[plasmid, operon, part, interactors, opr, optr, oitr, ootr, inputt, output]
    for table in table_list:
        dbpy.database_custom(table)
        
    #Get all of the files you are making your database with. 
    #path = os.path.split(os.path.realpath(__file__))[0]
    #files_list = os.listdir(path)
    #files_list_formatted = [file_name for file_name in files_list if file_name[-3::] == 'txt']
    files_formatted = [(file_name + ".txt") for file_name in info_names]
    print files_formatted
    #Iterate thru all of the files and add the information to the appropriate table.
    for file_name, table_name in zip(files_formatted, info_names):
        with open(file_name, 'r') as file_handle:
            csv_handle = csv.reader(file_handle, dialect = "excel-tab")
            header = csv_handle.next()
            table_creator = which_table(table_list, table_name)
            parse_allocator(table_name, csv_handle)
    conn.commit()
    cur.close()
    
if __name__ == '__main__':
    main()