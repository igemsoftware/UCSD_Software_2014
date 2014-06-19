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
        return command + '\n\t' + variables + '\n\t' + values
        
sqlObj = SQLInterface()
print sqlObj.SQLInsertWrapper('joaquin', ['Date', 'Miles', 'Trail', 'YouWent'], ['06/17',14,'Boar\'s Roar',True])

    def SQLUpdateWrapper(self, table, cols, values, w_cols = [], w_ops = [],w_values = [],w_conts = []):
        updateStr = 'UPDATE ' + table
        setList = []
        for var, value in cols, values:
            setList.append(str(var) + ' = ' + str(value))
        setStr = 'SET ' + ','.join(setList)
        if len(w_cols) > 0:
            whereStr = 'SET'
            for var, value, op, i in w_cols,w_cols,w_values,w_ops,range(len(w_cols)):
                if i < len(w_cols - 1):
                    hold = whereStr + ' '.join([var,op,value]) + ' ' + w_conts[count]
                else:
                    hold = whereStr + ' '.join([var,op,value]) + ' ' 
                whereStr = hold
                
        