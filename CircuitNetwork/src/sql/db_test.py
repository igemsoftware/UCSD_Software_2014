from database_pytools  import *

DEVICES_COLS = ['Name', 'Components', 'Authors', 'Article', 'Journal', 'Image_Path']

new_row = ['ram', 'horns+hooves+hair', 'Jemiah, Clen', 'The Day Programming Pissed Me off','vhertical', '/go/hang/out/peace/alskdldkjf.jpf']

insert_into_database(devices_row = new_row)
