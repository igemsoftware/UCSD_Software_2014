import sqlite3
import csv
import database_pytools as dbpy
import os
from subprocess import call
from sets import Set
import re

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
            
def parse_plasmid(csv_handle,cur):
    '''
    using the plasmid.txt file, will populate the plasmid table
    '''
    for row in csv_file:
        cur.execute(dbpy.database_insert("plasmid", [0,1]), row[0:1]))
        
def parse_operon(csv_handle,cur):
    '''
    using the operon.txt file, will populate the operon table
    '''
    for row in csv_file:
        cur.execute(dbpy.database_insert("operon", [0,1], row[0:1])
        
def parse_parts(csv_handle):
    '''
    using the structure.txt file, will populate the part table
    '''
    part_set = Set()
    for row in csv_handle:
        row = row.strip()
        print 'row is stripped', row
        row = re.sub('--->', ',',row)
        print 'row ---> replacement by ,', row
        row = re.sub('_', ',', row)
        print 'row _ replacement by ,', row
        row = row.split(',')
        print 'row splitting by ,', row
        print row
        for item in row:
            if item.lower() not in part_set:
                part_set.add(item)
    for num in range(len(part_set)):
        #print ["part", [0,1], [num, part_set.pop()]]
        #cur.execute(dbpy.database_insert("part", [0,1], [num, part_set.pop()])
        
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
        #cur.execute(dbpy.database_insert("interactors", [0,1], [num, part_set.pop()])
    
def parse_input(csv_file,cur):
    '''
    using the input.txt file, will populate the input table
    '''
    input_list = []
    for row in csv_file:
        
def parse_output(csv_file,cur):
    '''
    using the output.txt file, will populate the output table
    '''
def parse_opr(csv_file,cur):
    '''
    using the input.txt file, will populate the input table
    '''
def parse_optr(csv_file,cur):
    '''
    using the output.txt file, will populate the output table
    '''

                    

def main():
    #Deleting all old information and creating new txt's
    #call(["r", "-f", "database_linh_formmating.r"])
    
    #Connect to the database
    conn = sqlite3.connect('test_plasmid.db')
    conn.text_factory = str
    cur = conn.cursor()
    
    ''' 
    Minimally parsing for table insertion
    '''    
    #Creating tables of genetic constructs and interactors
    plasmid = 'CREATE TABLE plasmid (ID VARCHAR(50), Plasmid_Name VARCHAR(50), Miriam_ID VARCHAR(50), Title VARCHAR(50), Authors VARCHAR(50), Journal VARCHAR(50), Year VARCHAR(50));'
    operon = 'CREATE TABLE operon (ID VARCHAR(50), Name VARCHAR(50), Image_Path VARCHAR(50));'
    
    ''' 
    Intensive parsing for table insertion
    '''
    part = 'CREATE TABLE parts (ID VARCHAR(50), Part VARCHAR(50));'
    interactors = 'CREATE TABLE interactors (ID VARCHAR(50),Name VARCHAR(50),Type VARCHAR(50));'
    
    #Creating tables of transitions that are used for the petri nets
    input_ = 'CREATE TABLE input (ID VARCHAR(50), Input VARCHAR(50), Not_Bool bool);'
    output = 'CREATE TABLE output (ID VARCHAR(50), Output VARCHAR(50));'    
    
    #Creating tables of relationships
    opr = 'CREATE TABLE opr (ID VARCHAR(50), Operon_ID VARCHAR(50), Plasmid_ID VARCHAR(50), Main NUM(10));'
    optr = 'CREATE TABLE optr (ID VARCHAR(50), Operon_ID VARCHAR(50), Part_ID VARCHAR(50), Position NUM(10));'
    #can use input.txt
    oitr = 'CREATE TABLE oitr (ID VARCHAR(50), Operon_ID VARCHAR(50), Input_Transition_ID VARCHAR(50))
    #can use output.txt
    ootr = 'CREATE TABLE ootr (ID VARCHAR(50), Operon_ID VARCHAR(50), Output_Transition_ID VARCHAR(50))
    
    
    table_list =[plasmid, operon, part, interactors, opr, orc, oitr, ootr, inputt, output]
    #Setting up all of the csv names to extract the data
    info_names = ["plasmid", "operon", "input", "output", "opr", "structure", "optr", "interactors")
    
    
    #Get all of the files you are making your database with. 
    #path = os.path.split(os.path.realpath(__file__))[0]
    #files_list = os.listdir(path)
    #files_list_formatted = [file_name for file_name in files_list if file_name[-3::] == 'txt']
    file_list_formatted = [(file_name + ".txt"), for file_name in info_names]
    
    #Iterate thru all of the files and add the information to the appropriate table.
    for file_name, table_name in files_list_formatted, info_names:
        with open(file_name, 'r') as file_handle:
            file_csv = csv.reader(file_handle)
            header = file_csv.next()
            table_creator = which_table(table_list, table_name)
            for row in csv_dict:
                insert_command = sql.sql_insert(table_name, header, row)
                cur.execute(insert_command)
                
    conn.commit()
    cur.close()
    
if __name__ == '__main__':
    main()