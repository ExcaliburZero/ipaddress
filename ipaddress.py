"""A script which finds the ip address of the user using the /sbin/ifconfig command"""
from __future__ import print_function
import sys
from subprocess import Popen, PIPE

def main():
	"""Find out the user's ip address using the /sbin/ifconfig command and parsing
	 its output"""
	try:
		# Create a terminal and get network information using /sbin/ifconfig
		terminal = Popen("/sbin/ifconfig", shell=True, stdin=PIPE, stdout=PIPE)
		
		# Get the output from the terminal command
		ifconfig_out = terminal.communicate()

		# If /sbin/ifconfig yields an error then end the program
		if ifconfig_out[0] == '':
			warning("/sbin/ifconfig command returned no output")
			return 1

		# If /sbin/ifconfig worked, then parse its output for the ip address
		have_not_found_address = True
		current_index = 0
		search_string = ifconfig_out[0]
		ipaddress_string = "inet addr:"
		ipaddress = ""

		# Find the ip address within the /sbin/ifconfig output
		while have_not_found_address:
			# Reset the possible ip address
			ipaddress = ""

			# Find a possible location of the ip address
			if search_string.find(ipaddress_string) != -1:
				current_index = search_string.find(ipaddress_string)
				current_index = current_index + len(ipaddress_string)
			else:
				# End the program, since no valid ip address was found
				warning("No valid ip address found")
				return 0

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
