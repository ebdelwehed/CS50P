# # print("hello world!")
# name = input("what is your name ?")
# print("hello !")
# print(name)

# name = input("what is your name ?")
# print("hello !",end=" ")
# print(name)

# name = input("what is your name ?")
# print("hello " + name)

# name = input("what is your name ?")
# print(f"hello {name}")

# input()

#create function
# def hello(price):
#     print("price is ",price)
# #ask for price
# mango = int(input("how much is mango"))
# hello(mango)

#create function named greed
# def greet(name):
#     print("welcome dear ", name)
# #ask for their name and store variable named customer

#create function calculate_area
# def calculate_area(length,width):
#     balac = length*width
#     print(balac)

# calculate_area(2,30)

# greet("customer")
# greet("caasho")

#creat function named mad lips
# def mad_lips(noun,adjective,verb):
#     print(f" THERE WILL BE SHOWN HERE {noun} {adjective} {verb}")
# mad_lips("SHE","IS","RUNNER")


# def main():

#     # Output using our own function
#     name = input("What's your name? ")
#     hello(name)

#     # Output without passing the expected arguments
#     hello()


# # Create our own function
# def hello(to):
#     print("hello,", to)


# main()


# #SAMEE FUNCTION MAIN LA DHAHO
# def main():
#     name = input("what is your name ?")
#     hello(name)
#     hello()

# def hello(to="world"):
#     print(f"hello people from earth ",to)

# main()



# #same funcion main la dhaho
# def main():
#     x = int(input("what is x ?"))
#     print("x squared is ",xsquared(x))

# def xsquared(n):
#     return n*n

# main()

# def main():
#     x = int(input("what is x ?"))
#     print(f"x squared is",xsquared(x))
# def xsquared(n):
#     return n * n
# main()

    
#make function that take three parameter
# def silly(kow,labo,sadax):
#     print(f"rag waxa ugu liita",kow,labo,sadax)

# silly(2,3,5)

#make function that takes firstname 
# def main():
#     magac = input("what is your name?")
    
#     email()

# def email(sufix="@gmail.com"):
#     print(f"your email is{magac}",email(sufix))
    

# main()


# #samee function main la dhaho
# def main():
#     #howsheena hoose waa in ay qadata magac 
#     name = input("what is your name ?")
#     #waxa raba magaca in ay raacdo @gmail.com
#     email(suffix="@gmail.com")

# def email(suffix):
#     print(f"your email is ",suffix)


# def main():
#   """Prompts user for input, stores it in 'magac', and prints it with @gmail.com."""
#   magac = input("Enter your username: ")
#   print(magac + "@gmail.com")

# if __name__ == "__main__":
#   main()

# magac = input("Username: ")
# print(magac + "@gmail.com")

# def email():
#     name = input("what is your name ?")
#     print(name + "@gmail.com")
# email()
# email()

# def main():
#     user = input("username: ")
#     email(user)

# def email(gmail):
#     print(gmail + "@gmail.com")
# main()

# def main():


# def calc():
#     x = int(input("what is x ?"))
#     y = int(input("what is y ?"))
#     z = x * y
#     print(f"result is {z}")

#     calc()

# # main()
# def addlastname(kow):
#     name = input("magacaa ?")
#     print(f"{name} daahir",kow)

# addlastname("libaax")


# def main():
#     name = input("magacaa: ")
#     print("aniga waa",name)


# main()

# Create a function named greet
# def greet(name):
#     print(f"waa ku salaamay"name)

# greet("ali")
# greet("farah")
# greet("asha")

# define main function
# def main():
#     name = input("what's your name?")
#     hello(name)

# def hello(to):
#     print("this line will have name",to)

# main()


# define main function
# def main():
#     username = input("type username: ")
#     get_user(username)

# def get_user(name):
#     print(f"your email is {name}@aramex.com")

# main()





# def main():
#     current_year = 2024
#     x = int(input("which year you were born?"))
#     age_calc(current_year,x)
    

# def age_calc(a,b):
#     print("you are ",a-b,"years old")


# main()

# name = input("what is your name ?")
# # first,last = name.split(" ")
# print(name)


# sentence = "this is sentence"
# word1,word2,word3 = sentence.split(" ")
# print(word1,word2,word3)
# print(len(word3)+3)


#same main function
# def main():
# #howshi ay qaban la heyd hoos ku qor , sida printer iyo waxkale kuna dar function kale
#     magaca = input("waa kumaa ?")
# #ka dibna samee function kor aad ku soo sheegtay haddi ay parameter ka heyd hoosna gali.
#     print(f"kk " ," !" )
# #halkaan uga yeer 
# def name(magaca):
#     print("walashaa cun",magaca)

# main()

#function main samee
def main():
    amount = int(input("amount: "))
    print(f"exchange rate of {amount} QR","is ",dollar(amount))

def dollar(amount):
    return amount * 3.73
main()



