#Test.py exercises various Python features
import sys
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
if True:
    pass
elif False:
    print("E: 'pass' should allow empty statement after 'if...:'", file=sys.stderr)
if d != f + " and " + e:
	print("E: string escaping fail", file=sys.stderr)
if x is not x or x is xRef or x is not xVal:
	print("E: referencing fail", file=sys.stderr)
if x + int(b) != 258:
	print("E: int/str conversion fail", file=sys.stderr)
if y in ["256"]:
    print("E: 'in' should compare address, not value", file=sys.stderr)
if 1 != xRef:
    print("E: reference should be to original value only", file=sys.stderr)

