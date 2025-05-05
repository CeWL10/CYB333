#!/usr/bin/python3

#Above: Shebang and path to binary that allows program to be called without
#specifying "Python3"

import socket #imports the standard socket module from Python that includes
#utilities for "low-level network interfaces"

#The following section creates variables for the listener IP address, port
#number, and buffer size, and prompts the user for input for each one.
#try and except are used here to provide a graceful shutdown in the event an
#error is created by improper input from the user.

def main():
	try:
		ipAdd = input('\nEnter the listener IP in x.x.x.x format: ')
		portNum = input('\nEnter the listener port in numbers, i.e. "1234": ')
		portNum = int(portNum)
		buff = input('\nEnter the desired buffer size (default is 1024): ')
		buff = int(buff)
	except:
		print("\nSyntax error. Try again.\n")
		quit()

#The following section creates a variable for the listener socket (called
#list), defines the socket type, binds it to the user-specified IP and port,
#and sets it to listen, with the directive to process no more than 1x
#message backlog.

	list = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	list.bind((ipAdd, portNum))
	list.listen(1)

#The following provides a message that tells the user the listener is
#listening, and how to exit gracefully if required.
	print("\n\nFlux capacitor is fluxing (i.e. listening for incoming connections...)")
	print("\nPress 'ctrl+c' at any time to quit\n")

	try: #Uses "try" and "except" for error handling

#Below: Creates a while loop that announces the accepted connection when the
#condition is true, utilizes the desired buffer size, and decodes and prints
#any data received.
		while True:
		    connection, address = list.accept()
		    print(f"Connection established with {address}!")
		    data = connection.recv(buff)
		    print("Received data: ", data.decode())
		    if not data:
		        break
		    message = "Hello client, thank you for connecting to the server.".encode()
		    connection.send(message)

		list.close() #closes the connection

#First and stage exception handling - closes the connection and quits if the
#user presses "ctrl+C" or if an error occurs.

	except KeyboardInterrupt:
		print("\nGoodbye!\n")
		list.close()
		quit()

	except:
		print("\nError received: Check IP, port, and buffer size.\n")
		list.close()
		quit()

#Third stage exception handling - any other error will also result in
#closing the connection and quitting the program.
	else:
		list.close()
		quit()

#Below: Python best practices to ensure the function is properly
#from others that might be loaded into memory.

if __name__ == '__main__':
        main()




