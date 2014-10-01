import os
import argparse 

def file_path(file_path, file_name):
   #checking if file path exists     
    if not os.path.exists(str(file_path)):
        raise argparse.ArgumentTypeError("readable_dir:{0} is not a valid path".format(str(file_path)))
        return
    else:
       abs_path = os.path.join(str(file_path),str(file_name))
       return abs_path


def module_path(module_name, file_name):
    path  = os.path.abspath(module_name.__file__)
    path_const = path.split('\\')
    del path_const[len(path_const) - 1]
    path_const.append(str(file_name))
    abs_path = ''
    for constituents in path_list:
        abs_path = os.path.join(abs_path,constituents)
    if not os.path.exists(abs_path):
        raise argparse.ArgumentTypeError("readable_dir:{0} is not a valid path".format(abs_path))
        return
    else:
        return abs_path    
