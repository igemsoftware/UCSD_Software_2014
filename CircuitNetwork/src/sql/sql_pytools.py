# filename: SQLInterface
# author: Joaquin Reyna and Fred Layao
# date: 07/02/14
# description: SQLwrappers and testing
def stringify_list(ls):
    return [str(x) for x in ls]

def sql_insert(table_name,cols,new_row):
    '''
    Constructs a string to insert a row into a sql table
    '''
    command = 'INSERT INTO ' + table_name
    variables = '(' + ','.join(cols) + ')'
    for i in range( len(new_row) ): 
        if isinstance(new_row[i], str):
            unformatted = new_row[i]
            new_row[i] = "'" + unformatted + "'"  
                
        else:
            unformatted = str(new_row[i])
            new_row[i] = unformatted      
                                            
    values = 'Values (' + ','.join(new_row) + ')'
    return command + '\n\t' + variables + '\n\t' + values + ';'
    
def sql_update(table_name, cols, values, w_cols = [], w_ops = [],w_values = [],w_conts = []):
    '''
    Constructs a string to update a value in a sql table
    param: table_name, the name of the SQL table
    param: cols, a list of the column names for updating
    param: values, a list of the updating values
    param: w_cols, a list specifying the columns to change
    param: w_ops, a list of possible operators
    param: w_values, a list of values which set conditional statements
    param: w_conts, a list of AND's and OR's
    '''
    update_str = 'UPDATE ' + table_name
    set_list = []
    for var, value in zip(cols, values):
        set_list.append(str(var) + ' = ' + str(value))
    set_str = 'SET ' + ', '.join(set_list)
    if len(w_cols) > 0:
        where_str = 'WHERE '
        #will definitely have to fix this because you will have a problem trying to access all of the 
        #variables because w_ops will definitely be shorter than all of the rest of the lists and so you
        #cannot use zip()
        for var, value, op, i in zip(w_cols,w_values,w_ops, range(len(w_cols) + 1)):
            if i < len(w_cols) - 1:
                hold = where_str + ' '.join([var,op,str(value)]) + ' ' + w_conts[i]
            else:
                hold = where_str + ' '.join([var,op,str(value)]) + ' ' 
            where_str = hold 
        return update_str + '\n\t' + set_str + '\n\t' + where_str + ';'
    return update_str + '\n\t' + set_str + ';'    
        
def sql_select(table, column, w_col = None, w_opt = None,
    w_var = None,w_bool = None, group = None, h_col = None, h_bool = None, h_value = None):
    '''
    advanced SQL select function
    @param table - name of the table
    @param column - the columns to be selected
    @param w_col - column names for where clause
    @param w_opt - operator for where clause
    @param w_var - variable for where clause 
    @param w_bool - boolean for where clause
    @param group - group name for GROUP BY caluse
    @param h_col
    
    '''
    # check whether argument is valid or not
    # all the w_ variables must be all None or same size w_bool is less by 1
    if (w_col is not None and w_opt is not None and w_var is not None \
        and w_bool is not None):
        if (len(w_col) != len(w_opt) and len(w_opt) != len(w_var)\
            and len(w_var) != (len(w_bool) - 1)):
            raise Exception("Invalid arguement")
    elif(w_col is not None or w_opt is not None or w_var is not None \
         or w_bool is not None):
            raise Exception("Invalid arguement")

    # must have a table name
    if ( table is None or len(table) == 0):
        raise Exception("a table name must be provided.")

    Q = "SELECT "
    
    for i in range(len(column)):
        Q = Q + column[i]
        if (i != len(column) - 1):
            Q += ", "
        else:
            Q += " "
    Q += "\n" + "FROM " + table + " "

    if w_col is not None :
        Q = Q + "\n"+"WHERE "
        for i in range(len(w_col)):
            Q = Q + w_col[i] + " " + w_opt[i] + " " + str(w_var[i]) + " "
            if i < len(w_bool):
                Q = Q + w_bool[i] + " "

    if group is not None:
        Q += "\n" + "GROUP BY " + group
        
    if h_col is not None and h_bool is not None and h_value is not None:
        Q += "\n" + "HAVING " + h_col + " " +  h_bool + " " + str(h_value)
    Q +=";"
    
    return Q
