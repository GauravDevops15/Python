#Operators
#Arithmetic,Assignment,Relational,Bitwise,Precedence,Identity,Logical,Membership

#Flaot Division
A=3//2
print(A)

B=3/2
print(B)

#Identity operator

a=5
b=5

print(a is b)

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)      # True (same object in memory)
print(a is c)      # False (same values, different objects)
print(a == c)      # True (values are equal)
print(a is not c)  # True (different objects)

