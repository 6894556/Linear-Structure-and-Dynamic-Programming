# String variable statements
# Both of ' and " work as wrappers.
strTest = "Hello World! ISE"
print(strTest)
strTestComp = "Hello World! ISE"

# String value equivalence test, quite simple!
print(strTestComp, strTest == strTestComp)

# String variable is actually a linear collection of letters,
# and the letters have indexes.
print(strTest[0], strTest[1])
print(strTest[-1], strTest[-2])

# See how the string operators work!
print(len(strTest))
print(strTest+" "+"Dept")
print(strTest*2)
print("ISE" in strTest)
print("ISE" not in strTest)
