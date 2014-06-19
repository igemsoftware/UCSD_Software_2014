import argparse
parser = argparse.ArgumentParser(description="description of this program goes here.")



#1
'''
parser.parse_args()
'''



#2
'''
# Adds argument echo.
parser.add_argument("echo")

# Parses arguments from the command line, and returns thsi argument's data.
args = parser.parse_args()

# Prints the argument.
print(args.echo)
'''



#3
'''
parser.add_argument("echo", help="echo the string you use here")
args = parser.parse_args()
print(args.echo)
'''



#4
'''
parser.add_argument("square", help="display a square of a given number", 
		    type=int)
args = parser.parse_args()
print(args.square**2)
'''



#5
'''
# Adds option, --verbosity.
parser.add_argument("--verbosity", help="increase output verbosity")
args = parser.parse_args()

# If optional --verbosity is not used, then args.verbosity is None, and None 
# fails the truth test of the if statement.
if args.verbosity:
	print("verbosity turned on")
'''



#6
'''
# If --verbose is used, then args.verbose is True, and False otherwise.
parser.add_argument("--verbose", help="increase output verbosity",
		    action="store_true")
args = parser.parse_args()
if args.verbose:
	print("verbosity turned on")
'''



#7
'''
parser.add_argument("-v", "--verbose", help="increase output verbosity",
		    action="store_true")
args = parser.parse_args()
if args.verbose:
	print("verbosity turned on")
'''



#8
'''
parser.add_argument("square", type=int,
		    help="display a square of a given number")
parser.add_argument("-v", "--verbose", action="store_true",
		    help="increase output verbosity")
args = parser.parse_args()
answer = args.square**2
if args.verbose:
	print("the square of {} equals {}".format(args.square, answer))
else:
	print(answer)
'''



#9
'''
parser.add_argument("square", type=int,
		    help="display a square of a given number")
parser.add_argument("-v", "--verbosity", type=int,
	            help="increase output verbosity")
args = parser.parse_args()
answer = args.square**2
if args.verbosity == 2:
	print("the square of {} equals {}".format(args.square, answer))
elif args.verbosity == 1:
	print("{}^2 == {}".format(args.square, answer))
else:
	print(answer)
'''



#10
'''
parser.add_argument("square", type=int,
		    help="display a square of a given number")
parser.add_argument("-v", "--verbosity", type=int, choices=[0, 1, 2],
		    help="increase output verbosity")
args = parser.parse_args()
answer = args.square**2
if args.verbosity == 2:
	print("the square of {} equals {}".format(args.square, answer))
elif args.verbosity == 1:
	print("{}^2 == {}".format(args.square, answer))
else:
	print(answer)
'''



#11
'''
parser.add_argument("square", type=int,
		    help="display the square of a given number")

# Count counts the number of occurance of a specific optional argument.
# If this option is not used, it becomes None.
parser.add_argument("-v", "--verbosity", action="count",
		    help="increase output verbosity")
args = parser.parse_args()
answer = args.square**2
if args.verbosity == 2:
	print("the square of {} equals {}".format(args.square, answer))
elif args.verbosity == 1:
	print("{}^2 == {}".format(args.square, answer))
else:
	print(answer)
'''



#12
'''
parser.add_argument("square", type=int,
		    help="display the square of a given number")

# Count counts the number of occurance of a specific optional argument.
# If this option is not used, it becomes None.
parser.add_argument("-v", "--verbosity", action="count",
		    help="increase output verbosity")
args = parser.parse_args()
answer = args.square**2

# bugfix: replace == with >=.
if args.verbosity >= 2:
	print("the square of {} equals {}".format(args.square, answer))
elif args.verbosity == 1:
	print("{}^2 == {}".format(args.square, answer))
else:
	print(answer)
'''



#13
'''
parser.add_argument("square", type=int,
		    help="display the square of a given number")

# Count counts the number of occurance of a specific optional argument.
# If this option is not used, it becomes None.
parser.add_argument("-v", "--verbosity", action="count", default=0,
		    help="increase output verbosity")
args = parser.parse_args()
answer = args.square**2

# bugfix: replace == with >=.
if args.verbosity >= 2:
	print("the square of {} equals {}".format(args.square, answer))
elif args.verbosity == 1:
	print("{}^2 == {}".format(args.square, answer))
else:
	print(answer)
'''



#14
'''
parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")
parser.add_argument("-v", "--verbosity", action="count", default=0)
args = parser.parse_args()
answer = args.x**args.y
if args.verbosity >= 2:
	print("{} to the power {} equals {}".format(args.x, args.y, answer))
elif args.verbosity >= 1:
	print( "{}^{} == {}".format(args.x, args.y, answer))
else:
	print(answer)
'''



#15
'''
parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")
parser.add_argument("-v", "--verbosity", action="count", default=0)
args = parser.parse_args()
answer = args.x**args.y
if args.verbosity >= 2:
	print("Running '{}'".format(__file__))
if args.verbosity >= 1:
	print("{}^{} == ".format(args.x, args.y))
print(answer)
'''



#16
'''
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")
args = parser.parse_args()
answer = args.x**args.y

if args.quiet:
	print(answer)
elif args.verbose:
	print("{} to the power {} equals {}".format(args.x, args.y, answer))
else:
	print("{}^{} == {}".format(args.x, args.y, answer))
'''
