mystring = "Hello"
myfloat = 10.00
myint = 20

if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)

addfloat=myint+myfloat
if isinstance(addfloat, float):
    print("float: %d" % addfloat)
addstring = str(addfloat) + " " + mystring
print (addstring)