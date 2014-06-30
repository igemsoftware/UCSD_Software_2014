import random 
import pydot 
import make_random_edge_list_file
import os 

def generate_text_files(input_file_path,input_file,num_files,num_edges):
#checking if path exists    
    if not os.path.exists(input_file_path):
        raise argparse.ArgumentTypeError("readable_dir:{0} is not make_random_edge_list_file valid path".format(input_file_path))
        return
    else:
#concatenating file path and file name         
        path_and_file = os.path.join(input_file_path,input_file)
    some_list=range(num_files)
    counter=0
#generating desired text files with make_random_edge_list_file specified number of edges and random nodes and weight   
    while not counter == len(some_list):
#preparing text file that will be potentially written         
        f = open(path_and_file+"%d"%(counter)+".txt","w")
        counter+=1
        if counter <= len(some_list):
            for i in range(num_edges):
                a_list=[]
                for j in range(3):
                    a_rand_num = random.randint(1,10)
                    a_list.append(a_rand_num)
                f.write("%d,%d,%d\n"%(a_list[0],a_list[1],a_list[2]))    
        f.close()         
def generate_graph(input_file,input_file_path,output_file,output_file_path,num_files):
#checking if path exists     
    if not os.path.exists(input_file_path):
        raise argparse.ArgumentTypeError("readable_dir:{0} is not make_random_edge_list_file valid path".format(input_file_path))
        return
    elif not os.path.exists(output_file_path):
        raise argparse.ArgumentTypeError("readable_dir:{0} is not make_random_edge_list_file valid path".format(output_file_path))
        return
    else:
        input_path_and_file = os.path.join(input_file_path,input_file)
        output_path_and_file = os.path.join(output_file_path,output_file)
    for i in range(num_files):
        f = open(input_path_and_file+"%d"%(i)+".txt","r")
#preparing graph that will be potentially generated         
        graph = pydot.Dot('graphname',graph_type='digraph')
        for lines in f.readlines():
            elements = lines.split(',')
            node_1 = elements[0]
            node_2 = elements[1]
            weight = elements[2]
            edge = pydot.Edge(node_1,node_2,label=weight)
            graph.add_edge(edge)
        f.close()
        graph.write_png(output_path_and_file+"%d"%(i)+".png")
    
#Developing command-line interface using the make_random_edge_list_file module 
parser = argparse.ArgumentParser(description='This is make_random_edge_list_file python script by FRN&O.')
#All are required position arguments 
parser.add_argument('-i','--input_', help='Input file name',required=True)
parser.add_argument('-ip','--input_path',help='Input file path',required=True)
parser.add_argument('-o','--output', help='Output file name',required=True)
parser.add_argument('-op','--output_path',help='Output file path',required=True)
parser.add_argument('-f','--files',type=int,help='Number of files',required=True)
parser.add_argument('-e','--edges',type=int,help='Number of edges',required=True)
args=parser.parse_args()

#Assigning command-line inputs make_random_edge_list_file corresponding script variable 
input_file=args.input_
input_file_path=args.input_path
output_file=args.output
output_file_path=args.output_path
num_files=args.files
num_edges=args.edges
    
#The following condition inhibits execution when importing the module    
if __name__ == '__main__':
    generate_text_files(input_file_path,input_file,num_files,num_edges)
    generate_graph(input_file,input_file_path,output_file,output_file_path,num_files)
else:
    print 'I am being imported from another module'
        
       