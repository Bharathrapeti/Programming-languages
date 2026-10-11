# Starting the game
print("Welcome to the Adventure Game!")
print("You are at the entrance of a mysterious cave.")
print("What do you want to do?")
print("1. Enter the cave")
print("2. Walk along the river")
print("3. Return to the village")

# Player's first choice
choice1 = input("Enter your choice (1, 2, or 3): ")

if choice1 == "1":
    print("\nYou step into the cave and see a sleeping dragon!")
    print("What will you do?")
    print("1. Fight the dragon")
    print("2. Sneak past the dragon")
    print("3. Run away")
    choice2 = input("Enter your choice (1, 2, or 3): ")
    if choice2 == "1":
        print("\nYou bravely fight the dragon but unfortunately, it wakes up and defeats you. Game over!")
    elif choice2 == "2":
        print("\nYou carefully sneak past the dragon and find a pile of gold! You win!")
    elif choice2 == "3":
        print("\nYou run out of the cave and return to safety. Game over!")
    else:
        print("\nInvalid choice. The dragon wakes up and chases you out of the cave. Game over!")
elif choice1 == "2":
    print("\nYou walk along the river and find a treasure chest!")
    print("What will you do?")
    print("1. Open the chest")
    print("2. Ignore the chest and continue walking")
    choice2 = input("Enter your choice (1 or 2): ")
    if choice2 == "1":
        print("\nYou open the chest and find a magical sword. You are now ready for any danger!")
    elif choice2 == "2":
        print("\nYou ignore the chest and miss out on the treasure. Game over!")
    else:
        print("\nInvalid choice. You slip into the river and are swept away. Game over!")
elif choice1 == "3":
    print("\nYou return to the village and meet a wise old man.")
    print("He tells you, 'The dragon in the cave guards a great treasure, but you must be clever to obtain it.'")
    print("Hint: Sneaking is often wiser than fighting!")
else:
    print("\nInvalid choice. Please restart the game and choose a valid option.")