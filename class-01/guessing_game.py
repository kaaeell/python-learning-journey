import random
print("="*30)
print("Guess the number between 1 and 100 🎯")
print("="*30)

rand = random.randint(1, 100)
guesses = 0

while True:
    guesses += 1
    x = int(input("Enter your guess: "))

    if x < rand:
        print("Too low!")
    elif x > rand:
        print("Too high!")
    else:
        print(f"Correct! You guessed it in {guesses} tries.")
        break
