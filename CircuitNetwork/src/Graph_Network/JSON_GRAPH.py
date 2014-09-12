import os 
import argparse
import database_pytools as dp 
import node_positions as np
def main(file_name):
    path  = os.path.abspath(dp.__file__)
    path_const = path.split('\\')
    del path_const[len(path_const) - 1]
    #concatentate path constituents
    file_path = path_const[0]
    for constituents in path_const:
        file_path = file_path + '\\' + constituents 
    #checking if path exists    
    if not os.path.exists(file_path):
        raise argparse.ArgumentTypeError("readable_dir:{0} is not a valid path".format(file_path))
        return
    else:
        #concatenating file path and file name         
        absolute_path = os.path.join(file_path,str(file_name))
    node_positions = np.generate_positions()
    with open(absolute_path,'w') as graph_net_file:
        graph_net_file.write('{\n')
        graph_net_file.write('    "data" : {\n')
        graph_net_file.write('    "selected" : true,\n')
        graph_net_file.write('    "name" : "Network_Graph"\n')
        graph_net_file.write('    },\n')
        graph_net_file.write('    "elements":{\n')

#******************************************************************************************** Device_Node_Constructor
        graph_net_file.write('        "nodes":[\n')
        devices = dp.select('plasmid', ['id','name', 'miriam_id', 'title', 'authors','journal','year']) 
        for device in devices:
            device_coordinates = node_positions[device[1]]
            x_coord = device_coordinates[0]
            y_coord = device_coordinates[1]
#************************************************************** Generating SBOL_PATHS for each device 
            device_id = device[0]
            opr_table = dp.select('opr',['id','operon_id','plasmid_id'])
            operon_table = dp.select('operon',['id', 'name', 'sbol_image_path'])
            operon_id = []
            sbol_paths = []
            operon_counter = 0
            for operons in opr_table:
                if device_id == operons[2]:
                    operon_id.append(operons[1])
            while operon_counter != len(operon_id):
                for device_operons in operon_table:
                    if operon_id[operon_counter] == device_operons[0]:
                        operon_counter+=1
                        sbol_paths.append(device_operons[2])
            sbol_tuple = tuple(sbol_paths)
#***************************************************************
            graph_net_file.write('            {\n')
            graph_net_file.write('                "data":{\n')
            graph_net_file.write('                    "class": "Device Species",\n')
            graph_net_file.write('                    "SUID": %d,\n'%int(device[0]))
            graph_net_file.write('                    "ID": "%d",\n'%int(device[0]))
            graph_net_file.write('                    "Name": "%s",\n'%device[1])
            graph_net_file.write('                    "Composition":[ %s, %s, %s]\n'%sbol_tuple)
            graph_net_file.write('                    "Miriam_ID": "%s",\n'%device[2])
            graph_net_file.write('                    "Title": "%s",\n'%device[3])
            graph_net_file.write('                    "Authors": "%s",\n'%device[4])
            graph_net_file.write('                    "Journal": "%s"\n'%device[5])
            graph_net_file.write('                    "Year": "%s"\n'%device[6])
            graph_net_file.write('                },\n')
            graph_net_file.write('                "position":{\n')
            graph_net_file.write('                    "x": %d,\n'%int(x_coord))
            graph_net_file.write('                    "y": %d\n'%int(y_coord))
            graph_net_file.write('                },\n')
            graph_net_file.write('                "selected": false\n')
            graph_net_file.write('            },\n') 

#********************************************************************************************* Interactor_Node_Constructor 
        operators = dp.select('interactor', ['id','name','type'])
        for operator in operators:
            operator_coordinates = node_positions[operator[1]]
            x_coord = operator_coordinates[0]
            y_coord = operator_coordinates[1]
            graph_net_file.write('            {\n')
            graph_net_file.write('                "data":{\n')
            graph_net_file.write('                    "class": "Chemical Species",\n')
            graph_net_file.write('                    "SUID": %d,\n'%int(operator[0]))
            graph_net_file.write('                    "ID": "%d",\n'%int(operator[0]))
            graph_net_file.write('                    "Name": "%s",\n'%operator[1])
            graph_net_file.write('                    "Type": "%s"\n'%operator[2])
            graph_net_file.write('                },\n')
            graph_net_file.write('                "position":{\n')
            graph_net_file.write('                    "x": %,\n'%int(x_coord))
            graph_net_file.write('                    "y": #\n'%int(y_coord))
            graph_net_file.write('                },\n')
            graph_net_file.write('                "selected": false\n')
            graph_net_file.write('            },\n') 


#**************************************************************** Transition_Node_Constructor 
        #for loop 
        graph_net_file.write('            {\n')
        graph_net_file.write('                "data":{\n')
        graph_net_file.write('                    "class": "Transition Species",\n')
        graph_net_file.write('                    "SUID": #,\n')
        graph_net_file.write('                    "ID": "#",\n')
        graph_net_file.write('                    "Type": ""\n')
        graph_net_file.write('                },\n')
        graph_net_file.write('                "position":{\n')
        graph_net_file.write('                    "x": #,\n')
        graph_net_file.write('                    "y": #\n')
        graph_net_file.write('                },\n')
        graph_net_file.write('                "selected": false\n')
        graph_net_file.write('            },\n') 













#*************************************************************** Edge_Constructor
        graph_net_file.write('        "edges":[\n')
        #for loop
        graph_net_file.write('            {\n')
        graph_net_file.write('                "data":{\n')
        graph_net_file.write('                    "ID": "chemical species",\n')
        graph_net_file.write('                    "source": #,\n')
        graph_net_file.write('                    "target": "#",\n')
        graph_net_file.write('                },\n')
        graph_net_file.write('                "selected": false\n')
        graph_net_file.write('            },\n') 
        
#************************************************************** Close Braces and Brackets         
        graph_net_file.write('')