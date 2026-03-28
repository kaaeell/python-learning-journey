#Assignment3

text = input("Enter a string: ")

count = {}

for char in text:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1
for char in count:
    print(f"{char}:{count[char]}")