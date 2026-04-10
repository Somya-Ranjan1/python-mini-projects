import random

print("🎯 GUESSING NUMBER GAME")

number = random.randrange(1, 100)
player_won = False
guesses = []

print("Guess a number between 1 and 100")
print("You have 5 attempts\n")

for i in range(5):
    try:
        guess = int(input("Enter your guess: "))
        guesses.append(guess)

        if guess == number:
            print("🔥 Wow! You guessed it correctly!")
            player_won = True
            break

        elif guess > number:
            print("📉 Too high!")

        else:
            print("📈 Too low!")

        attempts_left = 4 - i
        if attempts_left > 0:
            print(f"You have {attempts_left} attempts left\n")

    except ValueError:
        print("❌ Please enter a valid number!\n")

# Final result
if player_won:
    print("✅ You won!")

else:
    print(f"❌ You lost! The number was {number}")

print("Your guesses were:", guesses)