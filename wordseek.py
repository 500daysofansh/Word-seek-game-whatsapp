import random

# Load words
with open('words.txt', 'r') as file:
    WORDS = [word.strip().lower() for word in file if len(word.strip()) == 5]

# Choose a random target word
target = random.choice(WORDS)

def check_word(guess, target):
    result = []
    for i in range(5):
        if guess[i] == target[i]:
            result.append("🟩")
        elif guess[i] in target:
            result.append("🟨")
        else:
            result.append("🟥")
    return ''.join(result)

print("🧩 WordSeek Game 🧩")
print("Guess the 5-letter word!")

while True:
    guess = input("Your guess: ").lower()
    if len(guess) != 5:
        print("Please enter a 5-letter word.")
        continue
    if guess not in WORDS:
        print(f"{guess} is not a valid word.")
        continue

    result = check_word(guess, target)
    print(result, guess.upper())

    if guess == target:
        print("🎉 Correct! You guessed the word.")
        break
