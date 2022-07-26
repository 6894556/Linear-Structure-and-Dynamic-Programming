# A loop statement
# The most common loop statement in programming languages
# - for variable in sequence:
#       Statements for loop
#   else:
#       when for-loop is finished without a break
# Some useful statements for loops
# - continue
# - break

for itr in range(10):
    print(itr, end=' ')
print()

sum = 0
for itr in range(1,11):
    sum += itr
print(sum)

for itr in range(1, 100, 10):
    if itr == 51:
        continue
    else:
        print(itr, end=' ')
print()