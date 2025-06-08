#Dictionaries help in storing diff properties of entity in single data type
##It has Key:Value pair to store values

student = {
        "name":"Varsha",
        "Age":"24",
        "job":"HR"
    }

print(student["job"])

##we can create list of dictionaries

###eg- student_info= [{},{},{}]

ec2_instances = [
    {
        "id":"instance_001",
        "type":"t2.micro",
    },
    {
        "id":"instance_002",
        "type":"t2.dedium"
    }
]

print(ec2_instances[1]["type"])