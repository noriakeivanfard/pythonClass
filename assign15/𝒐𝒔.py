
"""os.listdir() method in Python is used to get the 
list of all files and directories in the specified directory.
If we don’t specify any directory, then the list of files and directories 
in the current working directory will be returned."""

# Python program to explain os.listdir() method
	
# importing os module
import os

# Get the list of all files and directories
# in the root directory
path = "/"
dir_list = os.listdir(path)

print("Files and directories in '", path, "' :")

# print the list
print(dir_list)

#___________________________________________________________________________________

"""Consider Current Working Directory(CWD) as a folder, where the Python is operating.
Whenever the files are called only by their name, Python assumes that it starts 
in the CWD which means that name-only reference will be successful only if the file is in the Python’s CWD.
Note: The folder where the Python script is running is known as the Current Directory.
This is not the path where the Python script is located."""


# Python program to explain os.getcwd() method 
          
# importing os module 
import os 
      
# Get the current working 
# directory (CWD) 
cwd = os.getcwd() 
      
# Print the current working 
# directory (CWD) 
print("Current working directory:", cwd) 

#______________________________________________________________

"""To change the current working directory(CWD) os.chdir() method is used. 
This method changes the CWD to a specified path. 
It only takes a single argument as a new directory path.
Note: The current working directory is the folder 
in which the Python script is operating."""


# Python program to change the 
# current working directory 
    
    
import os 
    
# Function to Get the current  
# working directory 
def current_path(): 
    print("Current working directory before") 
    print(os.getcwd()) 
    print() 
    
# Driver's code 
# Printing CWD before 
current_path() 
    
# Changing the CWD 
os.chdir('../') 
    
# Printing CWD after 
current_path() 

#_____________________________________________________________________

""" os.error: All functions in this module raise OSError in the case of invalid or
inaccessible file names  and paths, or other arguments that have the correct type,
but are not accepted by the operating system. 
os.error is an alias for built-in OSError exception. """

import os


try:
	# If the file does not exist,
	# then it would throw an IOError
	filename = 'GFG.txt'
	f = open(filename)
	text = f.read()
	f.close()

# Control jumps directly to here if
# any of the above lines throws IOError.	
except IOError:

	# print(os.error) will <class 'OSError'>
	print('Problem reading: ' + filename)
	
# In any case, the code then continues with
# the line after the try/except

#_____________________________________________________________________

"""os.path.exists(): 
This method will check whether a file exists or 
not by passing the name of the file as a parameter. 
OS module has a sub-module named PATH by using which 
we can perform many more functions."""

import os
#importing os module

result = os.path.exists("file_name") #giving the name of the file as a parameter.

print(result)

#______________________________________________________________________


