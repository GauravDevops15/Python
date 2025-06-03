#Lists

students_names = ["Abhi","Gaurav","Mansi","varsha","xyz"]
print(students_names)

## Helps in printing s3 buckets, Ec2 instances

#Tuple

###tuples are immutable,means can't be resized

admins = ("Abhi","Gaurav")
print(admins)

S3_bucket_lists = ("abhi_demo_bucket","ramu_demo_bucket")
print(S3_bucket_lists)

print(type(S3_bucket_lists))#check type
print(type(admins))#check type
print(type(students_names))#check type

#add element in existing tuple

#S3_bucket_lists.append("new_S3_bucket")#gives error coz can't add element in tuple

#add element in existing list

students_names.append("ABC_new_element")

print(students_names)

#remove element from list

students_names.remove("ABC_new_element")
print(students_names)
#count elements in list
count = len(students_names)
print (count)

#print one of element from list
print(S3_bucket_lists[0])

#slice of list
new_list = students_names[0:2]##it will create new list, from 0 to 2....3 being uppr bound
print(new_list)
