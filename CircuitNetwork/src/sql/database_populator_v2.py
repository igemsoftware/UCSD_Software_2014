import sqlite3
import csv
import sql_pytools as sqlpy
import database_pytools as dbpy
import os
from subprocess import call
from sets import Set
import re
        
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
        with open(file_name, 'ru') as file_handle:
            csv_handle = csv.reader(file_handle, dialect = "excel-tab")
            header = csv_handle.next()
            for row in csv_handle:
                dbpy.database_insert(table_name, header, row)
        conn.commit()
    cur.close()
    
if __name__ == '__main__':
    main()