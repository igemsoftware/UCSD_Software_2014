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
    intermediate = c.fetchall()

    '''
    for row in rows:
        print row
    '''
    
    
    connD = sqlite3.connect('igemDBdevice.db.txt')
    d = connD.cursor()
    d.execute('DROP TABLE IF EXISTS igemDBdevice')
    # Create table
    d.execute('CREATE TABLE igemDBdevice (NAME,COMPONENT,AUTHOR,ARTICLE,JOURNAL,YEAR)')
    d.executemany('INSERT INTO igemDBdevice VALUES (?,?,?,?,?,?)', device)
    connD.commit()

    d.execute("SELECT * FROM igemDBdevice")
    
    device = d.fetchall()
    
    for row in device:
        print row


    connI = sqlite3.connect('igemDBintermediate.db.txt')
    i = connI.cursor()
    i.execute('DROP TABLE IF EXISTS igemDBintermediate')
    # Create table
    i.execute('CREATE TABLE igemDBintermediate (INPUT,OUTPUT)')
    i.executemany('INSERT INTO igemDBintermediate VALUES (?,?)', intermediate)
    connI.commit()

    i.execute("SELECT * FROM igemDBintermediate")
    intermediate = i.fetchall()
    for row in intermediate:
        print row













    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    conn.close()


SQLreader('ML_June_2013.txt')



