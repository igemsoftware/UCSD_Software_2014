import csv
import sqlite3

def init_db(cur):
    cur.execute('''CREATE TABLE running (
        Date DATE,
        Miles INTEGER(15),
        Trail VARCHAR(15));'''
        )
def populate_db(cur,itr):
    cur.executemany('''
        INSERT INTO running (Date,Miles,Trail)
        VALUES (?,?,?)''',itr)



#@def SQLInsertWrapper, a pythonized wrapped SQL Insert method
#@param table, the name of the SQL table
#@param cols, a list of the column names
#@newRow, a list of the new row to be added 
class SQLInterface:
    def SQLInsertWrapper(self,table,cols,newRow):
        command = 'INSERT INTO ' + table
        variables = '(' + ','.join(cols) + ')'
        i = 0
        
        for i in range(len(newRow)):
            if isinstance(newRow[i],str):
                unformatted = newRow[i]
                newRow[i] = "'" + unformatted + "'"  
                  
            else:
                unformatted = str(newRow[i])
                newRow[i] = unformatted       
                                             
        values = 'Values (' + ','.join(newRow) + ')'
        return command + '\n\t' + variables + '\n\t' + values + ';'

    def SQLUpdateWrapper(self, table, cols, values, w_cols = [], w_ops = [],w_values = [],w_conts = []):
        updateStr = 'UPDATE ' + table
        setList = []
        for var, value in zip(cols, values):
            setList.append(str(var) + ' = ' + str(value))
        setStr = 'SET ' + ', '.join(setList)
        if len(w_cols) > 0:
            whereStr = ''
            #will definitely have to fix this because you will have a problem trying to access all of the 
            #variables because w_ops will definitely be shorter than all of the rest of the lists and so you
            #cannot use zip()
            for var, value, op, i in w_cols,w_cols,w_values,w_ops,range(len(w_cols)):
                if i < len(w_cols - 1):
                    hold = whereStr + ' '.join([var,op,value]) + ' ' + w_conts[count]
                else:
                    hold = whereStr + ' '.join([var,op,value]) + ' ' 
                whereStr = hold 
            return updateStr + '\n\t' + setStr + 'n\t' + whereStr + ';'
        return updateStr + '\n\t' + setStr + ';'
        
sqlObj = SQLInterface()
#print sqlObj.SQLInsertWrapper('joaquin', ['Date', 'Miles', 'Trail', 'YouWent'], ['06/17',14,'Boar\'s Roar',True])
#print sqlObj.SQLUpdateWrapper('joaquin', ['Date', 'Miles'], ['01/05',15])

db = sqlite3.connect(':memory:')
cur = db.cursor()
init_db(cur)
populate_db(cur,[('2014-06-03',3,'Coopers'),('2014-06-05',5,'Bite Back'),('2014-06-07',3,'Anza Borrego'), ('2014-06-11',14,'Broken Hill')])
db.commit()

for row in db.execute("SELECT * FROM running"):
    print row
