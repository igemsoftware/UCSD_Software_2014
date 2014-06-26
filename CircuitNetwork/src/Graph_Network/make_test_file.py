import random

# This function generates a random test file.
# @param file_name	name of the file.
# @param number_of_edges	number of the edges.
def make_test_file(file_name, number_of_edges):
	
	# Creates an empty file.
	f = open(file_name + ".txt", "w")
	
	# Writes lines onto the file using a for loop.
        for i in range(number_of_edges):
 	
		# List that holds a line to be written.
		a_list=[]
	
		# Randomly generates three digits, which are the node 1, node 2, and
		# the weight of each edge.
       		for j in range(3):
            	a_random_num = random.randint(1, 10)
            	a_list.append(a_random_num)
        	f.write("%d, %d, %d\n" % (a_list[0], a_list[1], a_list[2]))
    	
	f.close()
