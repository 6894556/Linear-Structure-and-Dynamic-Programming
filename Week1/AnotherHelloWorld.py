# Object-oriented program
# - HelloWorld is an object
# - __init__, __del__, and performAverage are methods
# Largely in two parts
# - Definition part
# - Execution part

class HelloWorld:
    def __init__(self): # constructor
        print("Hello World! Just one more time")
    def __del__(self): # deconstructor
        print("Good bye!")
    def performAverage(self, val1, val2):
        average = (val1 + val2) / 2.0
        print("The Average of the scores is : ", average)
def main():
    world = HelloWorld()
    score1, score2 = input("Enter two scores separated by a comma : ").split(",")
    world.performAverage(int(score1), int(score2))

main()