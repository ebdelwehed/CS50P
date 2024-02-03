#Demonstrates defining a function with parameter with a default value
def hello(to="world"):
    print("hello, ",to)
name = input("what's your name? ")
hello(name)