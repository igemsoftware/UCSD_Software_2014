from SQLInterface import SQLInterface

def SQLreader(file):
    # create the name of the table
    # the name of table is the same as the file name without ".txt"
    tableName = file[:(len(file)-4)]

    table = []
    column = []

    # split each line by tab
    # create a 2-dimensional list called table
    with open(file,'r') as filename:
        for line in filename:
            table.append(line.split("\t"))

    # the first line of the file is the header of each column
    # since we only have 8 columns in ML_June_2013.txt, I only keep the first 8
    # items in the list
    column = table[0][:8]


    sql = SQLInterface()
    # ingore the first row, because it is the header of columns
    for i in range(1,len(table)):
        sql.SQLInsertWrapper(tableName,column,table[i][:8])




SQLreader('ML_June_2013.txt')



