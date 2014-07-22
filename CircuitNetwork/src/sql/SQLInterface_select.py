class SQLInterface(object):
    # basic sql select wrapper
    #@param table - the name of the table
    #@param column - the columns to be selected
    def SQLSelectWrapper(self,table,column):
        
        if ( table is None or len(table) == 0):
            raise Exception("a table name must be provided.")
        
        Q = "SELECT "
        
        # put columns name into the SQL command
        if column is "*":
            Q = Q+"* "
        else:
            for i in range(len(column)) :
                Q = Q + column[i]
                if ( i != len(column) - 1):
                    Q = Q + ", "
                else:
                    Q = Q + " "
    
        Q = Q +"\n"+"FROM " + table + " "
    

        Q += ";"
        return Q
    '''
    davanced SQL select function
    @param table - name of the table
    @param column - the columns to be selected
    @param w_col - column names for where clause
    @param w_opt - operator for where clause
    @param w_var - variable for where clause 
    @param w_bool - boolean for where clause
    @param group - group name for GROUP BY caluse
    @param h_col
    
    '''
    def SQLAdvancedSelect(self, table, column, w_col = None, w_opt = None,
        w_var = None,w_bool = None, group = None, h_col = None, h_bool = None, h_value = None):
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










    
col = ["name", "age", "salary"]
w_col = ["age", "age"]
w_opt = [">", "<"]
w_var = [30, 40]
w_bool = [ "and" ]
group = "dept"
h_col = "age"
h_bool = "<"
h_value = 22
o = SQLInterface()

print ".........."
print o.SQLAdvancedSelect('employee', col, w_col, w_opt, w_var,w_bool, group)
print ".........."
print o.SQLAdvancedSelect('employee', col)
print ".........."
print o.SQLAdvancedSelect('employee', col, w_col,w_opt,w_var,w_bool, group)
print ".........."
print o.SQLAdvancedSelect('employee', col, w_col, w_opt, w_var, w_bool,group, h_col, h_bool, h_value)
print '"' + '.'*11 + '"'






    
    
        
        
        
       
            
        
