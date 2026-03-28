# ----- class3 ------

#Assignment1

# text = str(input("type a word: "))
# reversed_text = ""
# i = len(text)-1

# while i >= 0:
    # reversed_text = reversed_text + text[i]
    # i = i - 1
    # print(reversed_text)

#-----------------------------------------

#Assignment2

# text = str(input("enter your text: "))

# if text == text[::-1]:
#     print("True (palindrome)")
# else:
#     print("False (palindrome)")

#-----------------------------------------

#Assignment3

# text = input("Enter a string: ")

# count = {}

# for char in text:
#     if char in count:
#         count[char] += 1
#     else:
#         count[char] = 1
# for char in count:
#     print(f"{char}:{count[char]}")

#-----------------------------------------

#Assignment4

# text = input("Enter a string: ")

# compressed = ""
# count = 1

# for i in range(len(text)):
#     if i < len(text) - 1 and text[i] == text[i + 1]:
#         count += 1
#     else:
#         compressed += text[i] + str(count)
#         count = 1

# if len(compressed) < len(text):
#     print("Compressed:", compressed)
# else:
#     print("Original:", text)


#-----------------------------------------  
    
#Assignment5

# text = input("Enter a sentence: ")

# words = text.split()
# result = ""

# for word in words:
#     result += word.capitalize() + " "

# print(result.strip())