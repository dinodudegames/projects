# ------------------------ HANGMAN -------------------------
import random
from collections import Counter

somewords = [
    "apple", "river", "cloud", "tiger", "pencil", "mountain", "ocean", "banana", "mirror", "forest",
    "planet", "rocket", "guitar", "window", "castle", "dragon", "camera", "flower", "school", "bottle",
    "bridge", "cookie", "desert", "engine", "feather", "garden", "hammer", "island", "jungle", "kitten",
    "ladder", "magnet", "notebook", "orange", "pillow", "quartz", "rainbow", "shadow", "thunder", "umbrella",
    "volcano", "whisper", "xylophone", "yogurt", "zebra", "anchor", "basket", "candle", "dolphin", "emerald",
    "fountain", "glacier", "helmet", "igloo", "jacket", "kangaroo", "lantern", "marble", "narwhal", "orchid",
    "penguin", "quiver", "rabbit", "scooter", "tornado", "unicorn", "violet", "walnut", "xenon", "yacht",
    "zeppelin", "astronaut", "backpack", "compass", "diamond", "elephant", "firefly", "galaxy", "horizon", "iceberg",
    "jellyfish", "keyboard", "lighthouse", "moonlight", "necklace", "octopus", "parachute", "question", "raindrop", "spaceship",
    "treasure", "vacation", "waterfall", "yearbook", "zipper", "avocado", "blueberry", "cheetah", "dinosaur", "espresso"
]

stages = [
    # Stage 0 (start)
    """
  +---+
  |   |
      |
      |
      |
      |
=========
""",

    # Stage 1
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",

    # Stage 2
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",

    # Stage 3
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",

    # Stage 4
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",

    # Stage 5
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",

    # Stage 6 (game over)
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
"""
]

if __name__ == "__main__":
    print("Welcome to Hangman!")
    word = random.choice(somewords)

    for _ in word:
        print("_", end=" ")
    print("\n")
    
    guessed_letters = []
    wrong_guesses = 0

    print(stages[wrong_guesses])

    for _ in range(len(word)):
        print("_", end=" ")

    while wrong_guesses < len(stages) - 1:
        guess = input("\nGuess a letter: ").lower()
        guessed_letters.append(guess)

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters[:-1]:
            print("You already guessed that letter.")
            continue
            
        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
            for letter in word:
                if letter in guessed_letters:
                    print(letter, end=" ")
                else:
                    print("_", end=" ")
            print("\n")
        else:
            wrong_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.")
            print(stages[wrong_guesses])
            for letter in word:
                if letter in guessed_letters:
                    print(letter, end=" ")
                else:
                    print("_", end=" ")
            print("\n")

        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations! You've guessed the word '{word}' correctly!")
            break

    else:
        print(f"Game over! The word was '{word}'. Better luck next time!")