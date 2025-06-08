#python script helps more in windows machine and shell script helps in linux machine

##Modes:
###"r" – Read (default); file must exist.

###"w" – Write; creates a new file or overwrites an existing file.

###"a" – Append; adds to the end of the file if it exists.

###"b" – Binary mode (e.g., "rb", "wb").

###"x" – Create; fails if file already exists.

###"+" – Read and write (e.g., "r+", "w+").

import os

if os.path.exists("Day12/gaurav.txt"):
    print("File exists")
else:
    print("File does not exist")

file = open("Day12/gaurav.txt", "r")



content = file.read()# Reads entire file
print(content)
file.close()



file = open("Day12/gaurav.txt", "r")

line = file.readline()  # Reads one line
print(line)
file.close()



file = open("Day12/gaurav.txt", "r")
lines = file.readlines()       # Reads all lines into a list
print(lines)
file.close()