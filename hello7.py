#Demonstrates str functions
name = input("what's your name ? ").strip().title()
first, last = name.split(" ")
print(f"hello , {last}")

