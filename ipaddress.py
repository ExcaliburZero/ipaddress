from __future__ import print_function
import sys

def main():
	try:
		sys.stdout.write("Test\n")
	except Exception as ex:
		# Indicate that an error occured
		warning(ex.message)
		return 1
	else:
		# Indicate that the program ran sucessfully
		return 0

# Function used to print errors
def warning(*objs):
	print("Error: ", *objs, file=sys.stderr)

# Run the main method of the program
if __name__ == '__main__':
	main()
