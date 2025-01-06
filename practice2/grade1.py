grade = int(input("grade :"))
if 90 <= grade and grade <= 100:
    print("A")
elif 80 <= grade and grade <= 89:
    print("B")
elif 70 <= grade and grade <= 79:
    print("C")
elif 60 <= grade and grade <= 69:
    print("E")
else:
    print("F")
