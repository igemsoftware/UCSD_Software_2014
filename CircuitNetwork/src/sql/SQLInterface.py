<<<<<<< HEAD
'''test!!!'''
=======
#import csv
>>>>>>> df17aaf4cb0d976c09ebec1b3b28ccf4758145c3
import sqlite3

class running_table:
    
    
    #static variables, the idea is that the table name and the header do 
    #not change much so they can remain constant
    table_name = 'running'
    cols = ['Date', 'Miles', 'Trail']
    def __init__(self):
        self.db = sqlite3.connect(':memory:')
        self.db.text_factory = str
        cur = self.db.cursor()
        self.init_db(cur)
        self.populate_db(cur,[('2014-06-03',3,'Coopers'),('2014-06-05',5,'Bite Back'),('2014-06-07',3,'Anza Borrego'), ('2014-06-11',14,'Broken Hill')])
        self.db.commit()
        
    def init_db(self, cur):
        cur.execute('''CREATE TABLE running (
            Date DATE,
            Miles INTEGER(15),
            Trail VARCHAR(15));'''
            )
        print '''CREATE TABLE running(
            Date DATE,
            Miles INTEGER(15),
            Trail VARCHAR(15));'''
            
    def populate_db(self,cur,itr):
        cur.executemany('''
            INSERT INTO running (Date,Miles,Trail)
            VALUES (?,?,?)''',itr)
        for values in itr:
            print 'INSERT INTO running \n\t(Date,Miles,Trail) VALUES ({0[0]},{0[1]},{0[2]})'.format(values)
            
    def print_table(self):
        for row in self.db.execute("SELECT * FROM " + self.table_name):
            print row
        print '\n' + '*' * 10, 'Done', '*' * 10 + '\n'
        
        
class SQLInterface:
    
    
    #@def SQLInsertWrapper, a python wrapped SQL Insert method
    #@param table, the name of the SQL table
    #@param cols, a list of the column names
    #@newRow, a list of the new row to be added 
    def SQLInsertWrapper(self,tableName,cols,newRow):
        command = 'INSERT INTO ' + tableName
        variables = '(' + ','.join(cols) + ')'
        for i in range(len(newRow)): 
            if isinstance(newRow[i],str):
                unformatted = newRow[i]
                newRow[i] = "'" + unformatted + "'"  
                  
            else:
                unformatted = str(newRow[i])
                newRow[i] = unformatted      
                                             
        values = 'Values (' + ','.join(newRow) + ')'
        return command + '\n\t' + variables + '\n\t' + values + ';'
        
    #@def SQLUpdateWrapper, a python wrapped SQL Update method
    #@param table, the name of the SQL table
    #@param cols, a list of the column names for updating
    #@param values, a list of the updating values
    #@param w_cols, a list specifying the columns to change
    #@param w_ops, a list of possible operators
    #@param w_values, a list of values which set conditional statements
    #@param w_conts, a list of AND's and OR's
    def SQLUpdateWrapper(self, table, cols = [], values = [], w_cols = [], w_ops = [],w_values = [],w_conts = []):
        updateStr = 'UPDATE ' + table
        setList = []
        for var, value in zip(cols, values):
            setList.append(str(var) + ' = ' + str(value))
        setStr = 'SET ' + ', '.join(setList)
        if len(w_cols) > 0:
            whereStr = 'WHERE '
            #will definitely have to fix this because you will have a problem trying to access all of the 
            #variables because w_ops will definitely be shorter than all of the rest of the lists and so you
            #cannot use zip()
            for var, value, op, i in zip(w_cols,w_values,w_ops, range(len(w_cols) + 1)):
                if i < len(w_cols) - 1:
                    hold = whereStr + ' '.join([var,op,str(value)]) + ' ' + w_conts[i]
                else:
                    hold = whereStr + ' '.join([var,op,str(value)]) + ' ' 
                whereStr = hold 
            return updateStr + '\n\t' + setStr + '\n\t' + whereStr + ';'
        return updateStr + '\n\t' + setStr + ';'

#Running the code using an SQLInterface object to comvert information from
#Python in to SQL commands. A running_table database is also                
sqlObj = SQLInterface()
base = running_table()

base.db.execute(sqlObj.SQLInsertWrapper(base.table_name,base.cols,['2014-06-30',14,'Chunk Rock']))
#base.print_table()
#print sqlObj.SQLUpdateWrapper(base.table_name,['Miles'], [80] ,['Miles'], ['>'], [10])
base.db.execute(sqlObj.SQLUpdateWrapper(base.table_name,['Miles'], [80] ,['Miles'], ['>'], [10]))
#base.print_table()
base.db.execute(sqlObj.SQLUpdateWrapper(base.table_name, ['Miles'], [15]))
#base.print_table()
