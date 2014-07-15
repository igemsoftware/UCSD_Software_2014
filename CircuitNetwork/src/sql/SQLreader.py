from SQLInterface import SQLInterface
import sqlite3

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


    conn = sqlite3.connect('igemDatabase.db.txt')
    c = conn.cursor()

    c.execute('DROP TABLE IF EXISTS igemDatabase')
    # Create table
    c.execute('CREATE TABLE igemDatabase (' +  ", ".join(column) + ')')


    # Insert a row of data
    for i in range(1,len(table)):
        c.execute(sql.SQLInsertWrapper('igemDatabase',column,table[i][:8]))


#c.execute('SELECT * FROM igemDatabase;' )
#print c.fetchone()



    # Save (commit) the changes
    conn.commit()


    c.execute("SELECT NAME,COMPONENT,AUTHOR,ARTICLE,JOURNAL,YEAR FROM igemDatabase")
    device = c.fetchall()


    c.execute("SELECT INPUT,OUTPUT FROM igemDatabase")
    transition = c.fetchall()


    deviceL = []
    transitionL = []
    for i in range(len(device)):
        print list(device[i])
        # !!!!!!!!!!!
        #row = [device[i]].append("[]")
        tuple(row)
        deviceL.append(rowT)
        #!!!!!!!!! to be modified later

    for i in range(len(transition)):
        transitionL.append(tuple(list(transition[i]).append('[]')))
        # !!!!!!!!! tobe modified later

    c.execute('DROP TABLE IF EXISTS Devices')
    # Create table
    c.execute('CREATE TABLE Devices (NAME,COMPONENT,AUTHOR,ARTICLE,JOURNAL,YEAR,IMAGE_PATH)')
    c.executemany('INSERT INTO Devices VALUES (?,?,?,?,?,?,?)', device)
    conn.commit()

    c.execute("SELECT * FROM Devices")
    
    device = c.fetchall()
    
    for row in device:
        print row


    c.execute('DROP TABLE IF EXISTS Transitions')
    # Create table
    c.execute('CREATE TABLE Transitions (INPUT,OUTPUT,FUNCTION)')
    c.executemany('INSERT INTO Transitions VALUES (?,?,?)', transition)
    conn.commit()

    c.execute("SELECT * FROM Transitions")
    transition = c.fetchall()
    for row in transition:
        print row


    c.execute('DROP TABLE IF EXISTS Intermediates')

    c.execute('CREATE TABLE Intermediates (NAME, TYPE, ANNOTATION)')



    conn.commit()


    


    print type(transition)
    print type(transition[0])










    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    conn.close()


SQLreader('ML_June_2013.txt')



