#demonstrate defining a function with a parameter with default value
def hello(to="world"):
    print("hello ",to)

hello()
name = input("what's your name ?")
hello(name)