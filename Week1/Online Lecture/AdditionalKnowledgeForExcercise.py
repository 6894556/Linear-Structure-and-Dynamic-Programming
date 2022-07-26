# sentidata = []
# for loop (sentidata.append(row))
# - Create a 2-D array
a = [[1,2,3],[4,5,6]]
print(a)
# number of rows
print(len(a))
# number of elements in the specified row
# In this case it's the number of elements in the first row.
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

# Type Casting
# Index of an array should be integer.
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


# these are for the video lecture.


# Sentiment Analysis are very popular these days.

# We can identify bad reviews.
# And We can use those to improve our product by fixing those complains.

# classification task
# We are going to use numbers to distinguish pos and neg product reviews.
# How can we turn these articles in numbers?
# We can create a vector and solve the above problem. e.g. <1,0,0,1>, <I, cool, Lcd, >
# numerical representation of this text. ------> called bag of words


# RECALL conditional probability

# At th end of the day we are going to put some text at 'E' of P(H bar E)
# and calculate the probablity of being pos or neg.

# Many Words slide's formular is our final formular of our numberical part.
# You dont have to understand the final formular not yet.
# 다음주에도 Sentiment A.를 이어서 할건데 excercise 하다보면 우리가 뭐를 하는건지 이해할 수 있을 것이다.