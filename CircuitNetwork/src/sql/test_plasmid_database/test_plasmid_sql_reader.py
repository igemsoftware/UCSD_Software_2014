import sqlite3
import csv
import sql_pytools as sql
import os

def which_table(table_list, table_name):
    print table_name
    for table in table_list:
        if table_name in table:
            return table
    print "This is screwed up for some reason." 
    
def main():

    plasmid_info = 'CREATE TABLE plasmid_info (Plasmid_ID VARCHAR(50), Plasmid_Name VARCHAR(50),Miriam_ID VARCHAR(50), Size NUM(50), Image_Path VARCHAR(50));'
    por = 'CREATE TABLE plasmid_operon_relationship (OP_ID VARCHAR(50), Operon_ID VARCHAR(50), Plasmid_ID VARCHAR(50), Main NUM(10));'
    operon_input = 'CREATE TABLE operon_input (Operon_ID VARCHAR(50), Input VARCHAR(50));'
    operon_output = 'CREATE TABLE operon_output (Operon_ID VARCHAR(50), Output VARCHAR(50));'
    operon_math = 'CREATE TABLE operon_math (Operon_ID VARCHAR(50), Math VARCHAR(50));'
    orc = 'CREATE TABLE operon_components_relationship  (Operon_ID VARCHAR(50), Component_ID VARCHAR(50), Position NUM(10));'
    parts = 'CREATE TABLE parts (Part_ID VARCHAR(50), Part VARCHAR(50));'
    table_list =[plasmid_info, por, operon_input, operon_output,operon_math,orc, parts]
    
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