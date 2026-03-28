# Assignment1

text = str(input("type a word: "))
reversed_text = ""
i = len(text)-1

while i >= 0:
    reversed_text = reversed_text + text[i]
    i = i - 1
    print(reversed_text)