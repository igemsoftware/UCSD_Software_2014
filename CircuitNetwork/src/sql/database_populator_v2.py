import sqlite3
import csv
import sql_pytools as sqlpy
import database_pytools as dbpy
import os
from subprocess import call
from sets import Set
import re
import os.path as osp
        
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
                    
#--------------------main--------------------#
def main():
    
    #if(osp.isfile())
    
    #Setting up all of the csv names to extract the data
    info_names = ["plasmid", "operon", "input", "output", "opr", "part", "optr", "interactor"]

    ''' 
    Minimally parsing for table insertion
    '''    
    #Creating tables of genetic constructs and interactors
    plasmid = 'CREATE TABLE plasmid (id VARCHAR(50), name VARCHAR(50), miriam_id VARCHAR(50), title VARCHAR(50), authors VARCHAR(50), journal VARCHAR(50), year VARCHAR(50));'
    operon = 'CREATE TABLE operon (id VARCHAR(50), name VARCHAR(50), sbol_image_path VARCHAR(50));'
    part = 'CREATE TABLE part (id VARCHAR(50), name VARCHAR(50));'
    interactors = 'CREATE TABLE interactor (id VARCHAR(50),name VARCHAR(50), type VARCHAR(50));'
    #Creating tables of transitions that are used for the petri nets
    inputt = 'CREATE TABLE input (id VARCHAR(50), interactor_id VARCHAR(50), repressor bool);'
    output = 'CREATE TABLE output (id VARCHAR(50), interactor_id VARCHAR(50));'    
    #Creating tables of relationships
    opr = 'CREATE TABLE opr (id VARCHAR(50), operon_id VARCHAR(50), plasmid_id VARCHAR(50), direction VARCHAR(50), Main NUM(10));'
    ''' 
    Intensive parsing for table insertion
    '''
    optr = 'CREATE TABLE optr (id VARCHAR(50), operon_id VARCHAR(50), part_id VARCHAR(50), position NUM(10));'
    #can use input.txt
    oitr = 'CREATE TABLE oitr (id VARCHAR(50), operon_id VARCHAR(50), input_id VARCHAR(50));'
    #can use output.txt
    ootr = 'CREATE TABLE ootr (id VARCHAR(50), operon_id VARCHAR(50), output_id VARCHAR(50));'
    
    
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
        with open(file_name, 'rU') as file_handle:
            csv_handle = csv.reader(file_handle, dialect = "excel-tab")
            header = csv_handle.next()
            for row in csv_handle:
                if row[0] == "" and row[1] == "":
                    break
                else:
                    dbpy.database_insert(table_name, header, row)
    dbpy.database_close()
    
if __name__ == '__main__':
    main()