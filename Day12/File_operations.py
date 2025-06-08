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