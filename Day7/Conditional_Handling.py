# giving argument in terminal to check if block
#import sys
#type = sys.argv[1]
#if type == "t2.micro":
#    print("create Instance")

# directly checking if block
import sys
if len(sys.argv) > 1:
    instance_type = sys.argv[1]
    if instance_type == "t2.micro":
        print("create Instance")
    else:
        print("Unsupported instance type")
else:
    print("No instance type provided.")