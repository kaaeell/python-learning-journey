result = int(input("what's your score?: "))

if result <= 59:
    print("E")
elif 60 <= result <= 69:
    print("D")
elif 70 <= result <= 79:
    print("C")
elif 80 <= result <= 89:
    print("B")
elif 90 <= result <= 100:
    print("A")
else:
    print("Invalid score, must be between 0 and 100")