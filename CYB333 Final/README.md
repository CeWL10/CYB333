# About:
# HoneyCat is a tool that creates a directory tree and shares it on an unsecure http server
# (i.e. it looks like some dummy is sharing their home directory accidentally), and when a
# curious observer decides to take a look at what looks like a juicy target, HoneyCat logs
# their IP. When the server is closed, HoneyCat extracts the IP from the log and inserts it 
# into #a bash script containing UFW (uncomplicated firewall) rules, which the user can then
# run in the terminal to automatically block the blacklisted IPs (i.e. to "kill the curious
# cats").



# Usage:
# Run 'python3 honeycat.py' or './honeycat.py' in the directory you want to work from.
# HoneyCat will prompt you for a port number. By default it is set to the localhost
# address, but this can be changed in the script when you're ready to take it for a spin.
# Hit CTRL+C at any time to end the program. After HoneyCat is done, it will produce a 
# file called "blacklist.sh." Once this file is moved to the system were your firewall is
# active, change the permissions on the file to make it executable (i.e. 'chmod 700
# blacklist.sh'), then run it with 'sudo ./blacklist.sh.' Don't worry if there are repeats
# because UFW will skip them. You can check that the rules were properly assigned with 
# 'sudo ufw status verbose.' Note that HoneyCat is intended to be run in the DMZ or outside
# of the border firewall. An ideal setup would be on a RaspberryPi with a minimal Linux
# install.


# Dependencies:
# This has only been test and is intended to be used in Python 3.12.7+. Run "python3 -V"
# in the terminal to see what you have.
# This script will import a number of different modules, to include os, http.server,
# socketserver, sys, shutil, and functools. All should be available from standard libraries.
