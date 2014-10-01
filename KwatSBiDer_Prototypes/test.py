import sys

arg_list = sys.argv

print "\nThe args list contains", len(arg_list), "variables."
print "The arg list variables are ", arg_list, ".\n"

print "\nThe user input is being extracted from the commandline args.\n"
user_input = arg_list[1::]
print "The user_input is currently stored as a list: ", user_input
user_input = " ".join(user_input)
print "The user_input list is being pasted together."
print "The user_input is now: ", user_input
print "Is this the format that we require to run the traversal?"