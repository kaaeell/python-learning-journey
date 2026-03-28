#Assignment5

text = input("Enter a sentence: ")

words = text.split()
result = ""

for word in words:
    result += word.capitalize() + " "

print(result.strip())