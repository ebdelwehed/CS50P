grade = int(input("grade :"))
#check if grade is between 90 and 100
if grade >= 90 and grade <= 100:
    print("A")
elif grade >= 80 and grade <= 89:
    print("B")
elif grade >= 70 and grade <=79:
    print("D")
elif grade >= 60 and grade <= 69:
    print("E")
else:
    print("F")