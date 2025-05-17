import random

def roll_dice():
    return random.randint(1, 10000)

def play_game():
    print("Shake the button & win a Jackpot!\nWanna try your luck??\n\t1. Yes  2. No")
    choice = input("Enter your choice (1 or 2): ").strip()
    
    if choice == "2":
        print("You missed your chance :(")
        return
    
    print("\nHere is your number: ")
    first_roll = roll_dice()
    print(f"\t{first_roll}")
    
    print("\nGuess if the next number is Higher or Lower:\n1. HIGH  2. LOW")
    guess = input("Enter your guess (1 or 2): ").strip()
    
    print("......\n.....")
    second_roll = roll_dice()
    print(f"\t{second_roll}")
    
    if (first_roll < second_roll and guess == "1") or (first_roll > second_roll and guess == "2"):
        print("\n🎉 You Won! 🎉")
    else:
        print("\nBetter luck next time!")

# Start the game
play_game()