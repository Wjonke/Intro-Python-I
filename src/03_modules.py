# method 1 to get host name
import socket
# method 2 to get host name
from Scripts._socket import gethostname

import sys
import os
import platform
import getpass

"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
for things in sys.argv:
    print(things)

# Print out the OS platform you're using:
# YOUR CODE HERE

print(platform.system(), platform.release())

# Print out the version of Python you're using:
# YOUR CODE HERE

print("Python Version", sys.version)

# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
print(os.getpid())

# Print the current working directory (cwd):
# YOUR CODE HERE
print(os.getcwd())

# Print out your machine's login name
# YOUR CODE HERE

username = getpass.getuser()
print("I misspelled my username on my own computer :) ---->", username)

# method 1 to get host name
print(gethostname())


# method 2 to get host name
def get_host_name_IP():
    try:
        host_name = socket.gethostname()
        print("Hostname ----> :  ", host_name)
    except:
        print("Unable to get Hostname and IP")


get_host_name_IP()
