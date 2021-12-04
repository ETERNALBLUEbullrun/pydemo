#TestSet.ph tests builtin containers
import sys
y = int("256")
if y in [1, "256", int("3")]: #in list/array
	raise Exception("E: 'in' must compare address, not value")
array = ["not an array", [], [], []]
array[1] = [1, 2, 4, 8]
uSet1 = {1, 2, 4, 8}
uSet2 = {1, 2, 3, 4}
uSet2Ref = uSet2 #these are treated as the same object
uSet2Ref |= {5}
uSet3 = uSet2.copy()
uSet3 ^= uSet1
if uSet3 != {3, 5, 8}: # compare sets/dictionaries
	raise Exception("E: uSet3 = " + str(uSet3))
uSet3 &= uSet1
if uSet3 != {8}:
	raise Exception("E: uSet3 & uSet1 = " + str(uSet3))
uSet4 = uSet1 ^ uSet2
if uSet4 != {3, 5, 8}:
	raise Exception("E: uSet1 ^ uSet2 = " + str(uSet1 ^ uSet2))
uSet3 ^= uSet4
if uSet3 != {3, 5}:
	raise Exception("E: uSet3 & uSet4 = " + str(uSet3))
if uSet1.isdisjoint(uSet2):
	raise Exception("E: uSet1 & uSet2 = {}, ie uSet1 <=")
if uSet1.issubset(uSet2):
	raise Exception("E: uSet1 - uSet2 = {}")
if uSet1 < uSet2:
	raise Exception("E: uSet1 - uSet2 = {}, and uSet1 != uSet2")
if uSet2 > uSet1:
	raise Exception("E: uSet2 - uSet1 = {}, and uSet1 != uSet2")
array[2] = ["x", 123, 0, ['a', 3]]
x = 3
while x >= 0:
	array[2][x] = 1 << x
	x -= 1
if array[1] != array[2]:
	raise Exception("E: array2 = " + str(array[2]))
else:
	if array[1][1:3] != [2, 4]:
		raise Exception("E: array[1][1:3] = " + str(array[1][1:3]))
	array[3] = array[1][:3] + array[1][1:]
	if array[3] != [1, 2, 4] + [2, 4, 8]:
		raise Exception("E: array[1][1:] + [:3] = " + str(array[3]))
	array[3] = array[1][-1:] + array[1][-2:]
	if array[3] != [8] + [4, 8]:
		raise Exception("E: array[1][-1:] + [-2:] = " + str(array[3]))
	array[3] = array[1][:-1] + array[1][:-2]
	if array[3] != [1, 2, 4] + [1, 2]:
		raise Exception("E: array[1][:-1] + [:-2] = " + str(array[3]))
	array[3] = array[1][::2]
	if array[3] != [1, 4]:
		raise Exception("E: array[1][::2] = " + str(array[3]))
	array[3] = array[1][::-1]
	if array[3] != [8, 4, 2, 1]:
		raise Exception("E: array[1][::-1] = " + str(array[3]))
uSet = {"<html>", "<head>", "not a tag"} #unordered
uSet.remove("not a tag")
uSet.discard("not even in the set") #.remove is error here
uSet.add("<body>")
if "not a tag" in uSet:
	raise Exception("E:" + uSet)
if "<body>" not in uSet:
	raise Exception("E: <body> should have been in set of HTML tags")
uMap = {1: "0b1", 2: "0b10", 4: "0b100", 8: "0b1000"} #unordered
if uMap[8] != "0b1000":
	raise Exception("E: uM[8] = " + uMap[8])
if len(uMap) != 4:
	raise Exception("E: len(uM) = " + str(len(uMap)))
uMap.clear()
if len(uMap) != 0:
	raise Exception("E: len(uM) = " + str(len(uMap)))
print("done")

