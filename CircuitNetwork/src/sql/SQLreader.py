from SQLInterface import SQLInterface
import sqlite3

def SQLreader(file):
    ######################## read txt file #####################################
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

    ###################### create database #####################################
    sql = SQLInterface()

    conn = sqlite3.connect('igemDatabase.db.txt')
    c = conn.cursor()

    c.execute('DROP TABLE IF EXISTS igemDatabase')
    # Create table
    c.execute('CREATE TABLE igemDatabase (' +  ', '.join(column) + ')')


    # Insert a row of data
    for i in range(1,len(table)):
        c.execute(sql.SQLInsertWrapper('igemDatabase',column,table[i][:8]))


    #c.execute('SELECT * FROM igemDatabase;' )
    #print c.fetchone()

    # Save (commit) the changes
    conn.commit()

    '''
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
    '''


    ##################### create Devices table #################################
    index = [0,1,4,5,6,7]
    deviceCol = [table[0][x] for x in index]
    deviceCol.append("IMAGE_PATH")
    device = [table[x] for x in range(1,len(table)) ]
    device = [[device[y][x] for x in index] for y in range(len(device))]
    for i in range(len(device)):
        device[i].append("[ ]")

    c.execute('DROP TABLE IF EXISTS Devices')
    # Create table
    c.execute('CREATE TABLE Devices (' + ', '.join(deviceCol) + ')')
    for i in range(len(device)):
        c.execute(sql.SQLInsertWrapper("Devices",deviceCol,device[i]))
    conn.commit()

    ## print table ##
    c.execute("SELECT * FROM Devices")
    tableD = c.fetchall()
    for row in tableD:
        print row
    print '*'*10 + " END " + '*'*10


    ##################### create Transitions table #############################

    #input_species: input; output_species: device name
    #so I use 0 to represent this.
    index = [2,0]
    transition  = [[table[y][x] for x in index] for y in range(1,len(table))]
    for i in range(len(transition)):
        transition[i].append("0")
    #input_species: device name; output_species: output
    #so I use 1 to represent this.
    index = [0,3]
    transition.extend([[table[y][x] for x in index] for y in range(1,len(table))])
    for i in range(len(transition)/2, len(transition)):
        transition[i].append("1")

    for i in range(len(transition)):
        transition[i].append('[ ]')
    transitionCol = ['INPUT_SPECIES','OUTPUT_SPECIES','TYPE','FUNCTION']

    c.execute('DROP TABLE IF EXISTS Transitions')
    # Create table
    c.execute('CREATE TABLE Transitions ('+ ', '.join(transitionCol) +')')

    for i in range(len(transition)):
        c.execute(sql.SQLInsertWrapper("Transitions",transitionCol,transition[i]))
    conn.commit()

    ## print table ##
    c.execute("SELECT * FROM Transitions")
    tableT = c.fetchall()
    for row in tableT:
        print row
    print '*'*10 + " END " + '*'*10




    ##################### create Intermediates table ###########################
    
    intermediates = [[table[y][0] ]for y in range(1, len(table))]
    for i in range(len(intermediates)):
        intermediates[i].extend(["[ ]","[ ]"])

    intermediatesCol = ['NAME','TYPE','ANNOTATION']
    c.execute('DROP TABLE IF EXISTS Intermediates')
    c.execute('CREATE TABLE Intermediates ('+ ', '.join(intermediatesCol)+')')
    for i in range(len(intermediates)):
        c.execute(sql.SQLInsertWrapper("Intermediates",intermediatesCol,intermediates[i]))

    conn.commit()
    ## print table ##
    c.execute("SELECT * FROM Intermediates")
    tableI = c.fetchall()
    for row in tableI:
        print row
    print '*'*10 + " END " + '*'*10




    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    conn.close()


SQLreader('ML_June_2013.txt')



