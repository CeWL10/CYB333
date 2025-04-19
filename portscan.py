#!/usr/bin/python3

#Above: Shebang and path to binary that allows program to be called without
#specifying "Python3"

import socket #imports the standard socket module from Python that includes
#utilitites for "low-level network interfaces."
import sys #imports the standard sys module from Python that includes
#functionality to allow access to "system-specific parameters."

def main(): #Defines the body of the script as a function called main (best practices).

#The following section creates variables for the IP address, the lower port number, the
#higher port number, the port range, and lists of open and closed ports. The user is
#prompted for input to populate the IP and ports, the ports are converted to integers,
#the integer ports are populated in the port range variable, and the lists of open and
#closed ports are initialized as empty lists. Exception handling is incorporated for
#keyboard interrupts (i.e. graceful shutdown in the case the user presses ctrl+c) and
#general error handling using try/except clauses.
	try:
		ipAdd = input("\nEnter the target IP (or website) you want to scan: ")
		print("\nEnter the port range you want to scan: \n")
		lowPort = input("\nLowest: ")
		lowPort = int(lowPort)
		hiPort = input("\nHighest: ")
		hiPort = int(hiPort)
		portRange = range(lowPort, hiPort)
		listOfOpenPorts = []
		listOfConnRefus = []
	except KeyboardInterrupt:
		print(f"\nScan of {ipAdd} cancelled.\n")
		quit()
	except:
		print("\nSyntax error. Check you IP and ports and try again.\n")
		quit()

#The following section performs a check on the ports provided by the user to confirm
#a) if the ports are between 0 and 65535 and b) if the low port is lower than the
#high port. Errors are provided for each kind of problem within conditional statements,
#and try/except clauses are used to report errors and provide for graceful shutdown.
	def rg_check():
		try:
			if 0 <= lowPort <= 65535:
				pass
			else:
				print("Error: low port must be between 0 and 65,535.")
			if 0 <= hiPort <= 65535:
				pass
			else:
				print("Error: high port must be between 0 and 65,535")
			if lowPort > hiPort:
				print("Error: low port is higher than high port.")
			else:
				pass
		except:
			print("error")
			quit()

#The following section creates a function for scanning ports by using the socket.socket
#utility. The socket connection is stored under the local variable "conn," the timeout
#is set to 1.0 seconds to ensure the system has time to respond but doesn't get bogged
#down, a connection is attempted with the user-provided IP address and port and then closed,
#and status codes of 0 are noted as success.

	def scan_ports(ipAdd, port, status=1):
		try:
			conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			conn.settimeout(1.0)
			s = conn.connect_ex((ipAdd, port))
			if s == 0:
				status = s
			conn.close()
		except Exception as ex:
			pass
		return status

	rg_check() #The previously defined range check function is called to confirm the ports.

#In the following section, a for loop uses the content of the variable portRange to check
#the standard output of the scan_ports function for each IP and port pair, appending err
#codes of 0 to the open ports lists, and results with status codes greater than 0 to a
#list of closed ports or refused connections.
	for i in portRange:
		sys.stdout.flush()
		feedback = scan_ports(ipAdd, i)
		if feedback == 0:
			listOfOpenPorts.append(i)
		if feedback > 0:
			listOfConnRefus.append(i)

#The following section creates a conditional statement that checks if the open port list has
#content (and if so prints the list of closed and open ports), and if not just reports to the
#user that no open ports were found on the target.

	if len(listOfOpenPorts) >0:
		print("\nThe following is a list of open ports: ")
		print(sorted(listOfOpenPorts))
		print("\nThe following ports were closed or the host was unreachable: ")
		print(sorted(listOfConnRefus))
		print("\n")
	else:
		print("\nNo open ports were found on the target.")

#Below: Python best practices to ensure the function is properly
#from others that might be loaded into memory.

if __name__ == '__main__':
        main()
