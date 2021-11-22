#Test.py exercises various Python features
import TestSet
x = 1
xRef = x
x <<= 8
xVal = int(str(x))
y = int("256")
b = "2"
c = 1
d = """"double" and 'single' quotes"""
e = "'single' quotes"
f = '"double"'
if d != f + " and " + e:
	print("E: string escaping fail")
if x is not x or x is xRef or x is not xVal:
	print("E: referencing fail")
if x + int(b) != 258:
	print("E: int/str conversion fail")
if y in ["256"]:
    print("E: 'in' should compare address, not value")
if 1 != xRef:
    print("E: reference should be to original value only")

