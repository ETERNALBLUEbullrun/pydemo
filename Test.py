#Test.py exercises various Python features
import sys
import TestSet
import TestIo
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
if True:
    pass
elif False:
    raise Exception("E: 'pass' should allow empty statement after 'if...:'")
if d != f + " and " + e:
	raise Exception("E: string escaping fail")
if x is not x or x is xRef or x is not xVal:
	raise Exception("E: referencing fail")
if x + int(b) != 258:
	raise Exception("E: int/str conversion fail")
if y in ["256"]:
    raise Exception("E: 'in' should compare address, not value")
if 1 != xRef:
    raise Exception("E: reference should be to original value only")

