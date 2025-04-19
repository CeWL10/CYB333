#!/usr/bin/python3

#Above: Shebang and path to binary that allows program to be called without
#specifying "Python3"


import socket #imports the standard socket module from Python that includes
#utilities for "low-level network interfaces"


#The following section creates variables for the target IP address and port
#number, and prompts the user for input for each one. Try and except are used
#here to provide a graceful shutdown in the event an error is created by
#improper input from the user.

def main(): #Defines the body of the script as a function called main (best practices).
	try:
		target = input("Enter the IP address of the target you want to connect to: ")
		port = input("Enter the port number for the target connection: ")
		port = int(port)

	except KeyboardInterrupt: #specifies course of action for ctrl+c
		print("\nGoodbye!\n")
		quit()

	except: #specifies course of action for all other errors.
		print("\nError: check your syntax and try again\n")
		quit()

#Below: creates a socket connection to the specified target, uses the ip and
#port number from the variables above (user-defined), and sends a banner to
#the server to which it is connecting. The while loop is used to sustain the connection until
#the user presses q or ctrl+c. Within the while loop, try and except statements are used for
#error/exception handling and to direct the user to a graceful shutdown. the *.send statement
#is used to relay messages from the client to the server. Lastly, the client also receives a
#one-time message from the server (i.e. a banner). 

	try:
		while True:
			targetConn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			targetConn.connect((target, port))
			print("Press q or type 'ctrl+c' to quit")
			try:
				messageToServer = input("Send to server: ")
				if messageToServer == "q":
					print("Goodbye")
					targetConn.close()
					quit()
			except KeyboardInterrupt:
				targetConn.close()
				quit()
			targetConn.send(messageToServer.encode())
			message = targetConn.recv(1024).decode()
			print(f"Message from the server: {message}.")

		targetConn.close()
	except KeyboardInterrupt:
		print("\nGoodbye. Have a nice day!\n")
		targetConn.close()
		quit()

	except:
		print("Server is not active. :( Try again later.")
		targetConn.close()
		quit()

#Below: Python best practices to ensure the function is properly
#from others that might be loaded into memory.

if __name__ == '__main__':
	main()
