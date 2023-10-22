"""

Write a code in Python which will copy the content of a text file „in.txt‟
into another text file „out.txt‟.

"""




import os

#For user driven file copying system
#filename_input = input("Enter the file name you want to work with : ")
#filename_output = input("Enter a new name for the output file :  ")

#default names
filename_input = 'in.txt'
filename_output = 'out.txt'

folder_path = input("Enter the file destination folder  : ")

if os.path.exists(filename_input):
    input_file_with_path = filename_input
else:
    input_file_with_path = os.path.join(folder_path, filename_input)

if os.path.exists(filename_output):
    output_file_with_path =filename_output
else:
    output_file_with_path = os.path.join(folder_path, filename_output)

#Reading a provided file
with open(input_file_with_path, 'r') as file:
    inputFile = file.read()

print(inputFile)

with open (output_file_with_path, 'w') as file:

    file.write(inputFile)


#OUTPUT
"""
Enter the file destination folder  : C:\Users\joydip\OneDrive\Desktop
this is a demo file 1 
this is a demo file 2
this is a demo file 3
this is a demo file 4

"""



