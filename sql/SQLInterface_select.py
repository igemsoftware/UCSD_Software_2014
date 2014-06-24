class SQLInterface(object):
    # basic sql select wrapper
    #@param table - the name of the table
    #@param column - the columns to be selected
    def SQLSelectWrapper(self,table,column):
        
        if ( table is None or len(table) == 0):
            raise Exception("a table name must be provided.")
        
        Q = "SELECT "
        
        
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

    def SQLAdvancedSelect(self,table,column,w_col,w_opt,w_var,w_bool,group,):
        if (w_col is not None and w_opt is not None and w_var is not None \
            and w_bool is not None):
            if (len(w_col) != len(w_opt) and len(w_opt) != len(w_var)\
                and len(w_var) != (len(w_bool) - 1)):
                raise Exception("Invalid arguement")
        elif(w_col is not None or w_opt is not None or w_var is not None \
             or w_bool is not None):
                raise Exception("Invalid arguement")

        
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

        Q +=";"
        return Q










    
col = ["name", "age", "salary"]
w_col = ["age", "age"]
w_opt = [">", "<"]
w_var = [30, 40]
w_bool = [ "and" ]
group = "dept"
o = SQLInterface()

print ".........."
print o.SQLAdvancedSelect('employee', col, w_col, w_opt, w_var,w_bool,None)
print ".........."
print o.SQLAdvancedSelect('employee', col, None, None, None,None,None)
print ".........."
print o.SQLAdvancedSelect('employee', col,w_col,w_opt,w_var,w_bool,group)
print ".........."





    
    
        
        
        
       
            
        
