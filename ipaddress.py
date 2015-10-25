"""A script which finds the ip address of the user using the ifconfig command"""
from __future__ import print_function
import sys
from subprocess import Popen, PIPE

def main():
	"""Find out the user's ip address using the ifconfig command and parsing
	 its output"""
	try:
		# Create a terminal and run ifconfig to get network information
		terminal = Popen("ifconfig", shell=True, stdin=PIPE, stdout=PIPE)
		ifconfig_out = terminal.communicate()

		# If ifconfig yiels an error then end the program
		if ifconfig_out[1] != None:
			warning(ifconfig_out[1])
			return 1
		elif ifconfig_out[0] == '':
			warning("ifconfig command returned no output")
			return 1

		# If ifconfig worked, then parse its output for the ip address
		have_not_found_address = True
		current_index = 0
		search_string = ifconfig_out[0]
		ipaddress_string = "inet addr:"
		ipaddress = ""

		# Find the ip address within the ifconfig output
		while have_not_found_address:
			# Reset the possible ip address
			ipaddress = ""

			# Find a possible location of the ip address
			current_index = search_string.find(ipaddress_string)
			current_index = current_index + len(ipaddress_string)

			# Take in the address at the possible location
			while search_string[current_index] != " ":
				ipaddress = ipaddress + search_string[current_index]
				current_index = current_index + 1

			# Make sure that the ip address is not a local address
			if ipaddress[0:7] != "127.0.0":
				have_not_found_address = False
			else:
				search_string = search_string[current_index:]

		# Return the ip address found
		sys.stdout.write(ipaddress + "\n")
	except Exception as ex:
		# Indicate that an error occured
		warning(ex.message)
		return 1
	else:
		# Indicate that the program ran sucessfully
		return 0

# Function used to print errors
def warning(*objs):
	"""Send error messages to the terminal's stderr"""
	print("Error: ", *objs, file=sys.stderr)

# Run the main method of the program
if __name__ == '__main__':
	main()
