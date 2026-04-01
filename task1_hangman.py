import random

# ─────────────────────────────────────────────
#  TASK 1 — Hangman Game
# ─────────────────────────────────────────────

def hangman():
    words = ["python", "guitar", "mango", "laptop", "bridge"]
    word = random.choice(words)
    guessed = []
    attempts = 6

    print("=" * 40)
    print("       Welcome to HANGMAN!")
    print("=" * 40)

    while attempts > 0:
        # Display current word state
        display = " ".join([letter if letter in guessed else "_" for letter in word])
        print(f"\nWord: {display}")
        print(f"Attempts left: {attempts}")
        print(f"Guessed letters: {', '.join(sorted(guessed)) if guessed else 'None'}")

        # Check win condition
        if all(letter in guessed for letter in word):
            print(f"\n🎉 You WIN! The word was '{word}'!")
            return

        # Get player input
        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("⚠ Please enter a single letter.")
            continue

        if guess in guessed:
            print(f"⚠ You already guessed '{guess}'. Try another.")
            continue

        guessed.append(guess)

        if guess in word:
            print(f"✅ '{guess}' is in the word!")
        else:
            attempts -= 1
            print(f"❌ '{guess}' is NOT in the word!")

    print(f"\n💀 Game Over! The word was '{word}'.")

hangman()