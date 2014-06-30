import random

def make_random_edge_list_file(file_name, number_of_edges):
    '''
    Generates a .txt test file.
    @param file_name: name of test file to be generated.
    @type file_name: string.
    @param number_of_edges: number of edges in test file.
    @type number_of_edges: int.
    '''
    
    # Opens an empty .txt file.
    f = open(file_name + ".txt", "w")
    # Writes lines onto the file using for loop.
    for i in range(number_of_edges):
        # List that holds a line, or an edge.
        a_list=[]
        # Randomly generates three digits, node 1, node 2, and the weight for each edge.
        for j in range(3):
            a_random_num = random.randint(1, 10)
            a_list.append(a_random_num)
            # Writes a line, or an edge.
        f.write("%d, %d, %d\n" % (a_list[0], a_list[1], a_list[2]))
    f.close()