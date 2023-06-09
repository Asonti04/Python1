#!bin/bash

import os 
import glob
cwd = os.getcwd() #Prints working directory
print(cwd)

ls = os.listdir() 
print(ls)

Dir = [] #creates empty list

filenames = glob.glob('/home/ec2-user/environment/Python1/*.py') #retrieve filenames

Dir.sort() #Puts file in order by name
Dir.append(filenames) #adds the filenames to the empty list

for file in filenames:
    size = os.stat(file)
    print('File names: ', file, '  File size:  (', size[6], ')')