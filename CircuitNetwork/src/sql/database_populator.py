import sqlite3
import csv
import sql_pytools as sql
import os


def which_table(table_list, table_name):
    '''
    '''
    print table_name
    for table in table_list:
        if table_name in table:
            return table
            
def domain_to_database(,domain_str):
    '''
    Takes in domain and puts into correct tables
    '''
    domain_str = domain.split(',')
            
def spreadsheet_parser():
    '''
    Takes in data from the spreadsheet and parses it for the sql database
    '''
    

def main():
    #Creating tables of genetic constructs and interactors
    plasmid_table = 'CREATE TABLE plasmid (ID VARCHAR(50), Plasmid_Name VARCHAR(50), Miriam_ID VARCHAR(50), Size NUM(50));'
    operon_table = 'CREATE TABLE operon (ID VARCHAR(50), Name VARCHAR(50), Image_Path VARCHAR(50));'
    part_table = 'CREATE TABLE parts (ID VARCHAR(50), Part VARCHAR(50));'
    interactors_table = 'CREATE TABLE interactors (ID,Name,Type)
    #Creating tables of relationships
    opr_table = 'CREATE TABLE opr (ID VARCHAR(50), Operon_ID VARCHAR(50), Plasmid_ID VARCHAR(50), Main NUM(10));'
    orc_table = 'CREATE TABLE optr (ID VARCHAR(50), Operon_ID VARCHAR(50), Part_ID VARCHAR(50), Position NUM(10));'
    oitr_table = 'CREATE TABLE oitr (ID, Operon_ID, Input_Transition_ID)
    ootr_table = 'CREATE TABLE ootr (ID, Operon_ID, Output_Transition_ID)
    #Creating tables of transitions that are used for the petri nets
    it_table = 'CREATE TABLE input_trans (ID VARCHAR(50), Input VARCHAR(50), NOT Bool );'
    ot_table = 'CREATE TABLE output_trans (ID VARCHAR(50), Output VARCHAR(50));'
    
    
    table_list =[plasmid_table, por, operon_input, operon_output,operon_table,orc, part_table]
    
    #Connect to the database
    conn = sqlite3.connect('test_plasmid.db')
    conn.text_factory = str
    cur = conn.cursor()
    
    #Get all of the files you are making your database with. 
    path = os.path.split(os.path.realpath(__file__))[0]
    files_list = os.listdir(path)
    files_list_formatted = [file_name for file_name in files_list if file_name[-3::] == 'csv']
    
    #Iterate thru all of the files and add the information to the appropriate table.
    for file_name in files_list_formatted:
        with open(file_name, 'r') as file_handle:
            csv_dict = csv.reader(file_handle)
            header = csv_dict.next()
            table_name = file_name[:-10:]
            table_creator = which_table(table_list, table_name)
            cur.execute(table_creator)
            for row in csv_dict:
                insert_command = sql.sql_insert(table_name, header, row)
                cur.execute(insert_command)
                
    conn.commit()
    cur.close()
    
if __name__ == '__main__':
    main()