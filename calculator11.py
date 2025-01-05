#demonstrate defining a function with a return value
def main():
    x = int(input("what's x ?"))
    print("x squared is",xsquared(x))

#define xsquared function
def xsquared(n):
    return n * n

main()