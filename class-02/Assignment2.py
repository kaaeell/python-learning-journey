#Assignment2

text = str(input("enter your text: "))

if text == text[::-1]:
    print("True (palindrome)")
else:
    print("False (palindrome)")