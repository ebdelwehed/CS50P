#Demonstrates formatting after the decimal place
x = int(input("what's x ?"))
y = int(input("what's y ?"))

z = x / y
#printing numbers of digit after decimal below 2f
#will print .22 , if 3f , it will print .222
print(f"{z:.2f}")
              