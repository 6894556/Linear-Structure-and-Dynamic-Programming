# This index xapplies to strings as well as tuples, lists
# -> Applies to any sequence variables

strTest = 'Hello World! ISE'
print(strTest)
# Simple index of a sequence, or any array
print(strTest[1], strTest[2], strTest[3])
# x:y -> from x to y
print(strTest[1:3])
print(strTest[3:])
print(strTest[:3])
# x:y:z -> from x to y with z steps
print(strTest[1:9:2])
print(strTest[1:len(strTest):2])
print(strTest[1::2])
# Default : y = the length of the sequence,  z = 1
print(strTest[5::-1])