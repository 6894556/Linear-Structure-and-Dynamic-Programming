# sentidata = []
# for loop (sentidata.append(row))
# - Create a 2-D array
a = [[1,2,3],[4,5,6]]
print(a)
print(len(a))
print(len(a[0]))

# zip(v1, v2)
# - Call elementwise pair of vector v1 and v2
v1 = [1,2,3]
v2 = [4,5,6]
for x, y in zip(v1, v2):
    print((x,y))

# enumerate(list)
# - Call index and value together
v1 = ['a', 'b', 'c']
for index, value in enumerate(v1):
    print(index, value)

# sum(list)
# - Sum of list
v = [1,2,3,4,5]
print(sum(v))

# int(float(x))
# - Convert a string type x into integer type
x = '1.0'
print(x, type(x))
x1 = float(x)
print(x1, type(x1))
x2 = int(float(x))
print(x2, type(x2))

# List comprehension
# - Make a list of value that satisfies the condition
# - list = [value for loop (condition)]
v1 = [[1, 2, 3, 4],
      [5, 6, 7, 8],
      [9, 10, 11, 12]]
v2 = [sum(row) for row in v1]
print(v2)