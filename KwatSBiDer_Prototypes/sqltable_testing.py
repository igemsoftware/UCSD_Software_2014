import sql_pytools as sp
import database_pytools as dp
import sqlite3 

class sql_database:    
    '''
    SQL table object used to test SQL wrappers.
    ''' 
    # Static variables    
    TABLE_NAME = 'running'
    COLUMNS = ['Date', 'Miles', 'Trail']
    
    
    def __init__(self):
        '''
        This is the constructor for a table for SQL testing
        ''' 
        # Stores database on local machine
        self.db = sqlite3.connect('iGEM.db.txt')
        # Formats SQL output string
        self.db.text_factory = str
        self.cur = self.db.cursor()
        self.init_db(self.cur)
        self.fill_table(self.cur,[('2014-06-03',3,'Coopers'), 
                            ('2014-06-05',5,'Bite Back'),
                            ('2014-06-07',3,'Anza Borrego'),
                            ('2014-06-11',14,'Broken Hill')]
                        )
        # Commits the SQL commands to the current machine
        self.init_db2(self.cur)
        self.db.commit()
        
    def init_db(self, cur):
        '''
        The init_db(...) method initiatilizes the SQL table.
        '''
        cur.execute('CREATE TABLE running({0} DATE, {1} INTEGER(15), {2} VARCHAR(15));'.format(self.COLUMNS[0],self.COLUMNS[1],self.COLUMNS[2]))
            
    def fill_table(self, cur, itr):
        ''' 
        Populates the table which cur points to using a list of tuples.
        '''
        cur.executemany('''
            INSERT INTO running 
            (Date,Miles,Trail)
            VALUES (?,?,?)''',itr)
            
    def print_table(self):
        '''
        Prints the SQL table a row at a time.
        '''
        
        for row in self.db.execute("SELECT * FROM " + self.TABLE_NAME):
            print row
        print '\n' + '*' * 10, 'Done', '*' * 10 + '\n'
        
    def init_db2(self, cur):
        cur.execute('CREATE TABLE nutrition ({0} DATE, {1} VARCHAR(50))'.format('Date', 'Food'))
        
    def fill_table2(self,cur,itr):
        cur.executemany('''
         INSERT INTO nutrition
         (Date,Food)
         VALUES (01-05-2013, 'Lasagna')'''
         )
        
        
#Running the code using an SQLInterface object to comvert information from
#Python in to SQL commands. A running_table database is also                
base = sql_database()
base.cur.execute(sp.sql_insert(base.TABLE_NAME,base.COLUMNS,['2014-06-30',14,'Chunk Rock']))
base.print_table()
print sp.sql_update(base.TABLE_NAME,['Miles'], [80] ,['Miles'], ['>'], [10])
base.db.execute(sp.sql_update(base.TABLE_NAME,['Miles'], [80] ,['Miles'], ['>'], [10]))
base.print_table()
base.db.execute(sp.sql_update(base.TABLE_NAME, ['Miles'], [15]))
base.print_table()
#dp.insert_into_database(['5', '4','3','2','1'])

        