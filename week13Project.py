#!bin/bash

import os 
import glob
cwd = os.getcwd() #Prints working directory
print(cwd)

ls = os.listdir()  
print(ls) #this will list your files in the directory

Dir = [] #creates empty list

<<<<<<< HEAD
filenames = glob.glob('/home/ec2-user/environment/Python1/*.py') #retrieve filenames
=======
filenames = glob.glob('/home/ec2-user/environment/Python1/*') #retrieve filenames
>>>>>>> origin/main

for file in filenames: #this will get your file size 
    size = os.stat(file)
    Dict = {
    file: size[6] #This makes a dictionary
    }
    Dir.append(Dict)
<<<<<<< HEAD
print(*Dir, sep='\n') #prints out the file with corresponding size
=======
print(*Dir, sep='\n') #prints out the file with corresponding size
>>>>>>> origin/main
