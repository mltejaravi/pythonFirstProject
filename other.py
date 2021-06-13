#Bitwise
# &, | , ^ , ~ , << , >>
list = [10,20,30,40,50]
a=20
b=20
def bitwise():
    if(a == 20  & b == 20):
        print(True)
    else:
        print(False)
#Logical
# and, or, not
def logical():
    if(a == 20  and b == 20):
        print(True)
    else:
        print(False)
#Membership
#in ,not in
def membership():
    if(a in list):
        print(True)
    else:
        print(False)
#Identity
#is , is not
def identity():
    if(a is b):
        print(True)
    else:
        print(False)

bitwise()
logical()
membership()
identity()
