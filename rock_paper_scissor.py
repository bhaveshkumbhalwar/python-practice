import random

options = ("rock", "paper", "scissor")

isRunning = True

while isRunning:
    player = input("Enter a choice (rock, paper, scissor): ").lower()

    if player not in options:
        print(" Invalid input! Try again.")
        continue

    bot = random.choice(options)

    print(f"You: {player}")
    print(f"Bot: {bot}")

    if player == bot:
        print("It's a tie!")

    elif (player == "rock" and bot == "paper") or \
         (player == "paper" and bot == "scissor") or \
         (player == "scissor" and bot == "rock"):
        print(" You lose!")

    else:
        print(" You win!")

    play_again = input("Play again? (y/n): ").lower()
    if play_again != 'y':
        isRunning = False

print("Thanks for playing!")