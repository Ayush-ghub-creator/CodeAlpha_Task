import random

words = ["python", "apple", "school", "computer", "hangman"]
word = random.choice(words)

guessed = ["_"] * len(word)
wrong_guesses = 0
guessed_letters = []

print("Welcome to Hangman!")

while wrong_guesses < 6 and "_" in guessed:
    print("\nWord:", " ".join(guessed))
    print("Wrong guesses:", wrong_guesses, "/ 6")

    letter = input("Guess a letter: ").lower()

    if letter in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(letter)

    if letter in word:
        print("Correct!")

        for i in range(len(word)):
            if word[i] == letter:
                guessed[i] = letter
    else:
        print("Wrong!")
        wrong_guesses += 1

if "_" not in guessed:
    print("\nYou won! The word was:", word)
else:
    print("\nYou lost! The word was:", word)