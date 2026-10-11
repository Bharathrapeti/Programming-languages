print("-----welcome to advantures-----")
print("you are in entrance of a mysterious cave.")
print("what do you want to do ?")
print("1.Go into the cave.")
print("2.Walk along the river nearby.")
print("3.Return to the village.")
choice1 = input("Enter your choice (1,2or3)?")
if choice1 == "1":
    print("you step into  the cave and see the sleeping dragon.")
    print("what you will u do ?")
    print("1.fight with the dragon.")
    print("2.sneak past")
    print("3.you can run away")
    choice2 = input("Enter your choice (1,2or3)?")
    if choice2 == "1":
        print("you go towards the dragon and bravely fight with the dragon.")
    elif choice2 == "2":
        print("you carefully sneak past the dragon and find a pile of gold!you win!")
    elif choice3 == "3":
        print("you can run away form the dragon quickly.")
    else:
        print("invalid choice.")
elif choice1 == "2":
    print("ok let's walk along the river and find the treasure chest.")
    print("what will you do ?")
    print("1.you can open it.")
    print("2.you can leave it.")
    choice2 = input("Enter your choice (1or2)?")
    if choice2 == "1":
        print("open the treasure and take it come back.")
    elif choice2 == "2":
        print("you can ignore it.")
    else:
        print("invalid choice.")
elif choice1 == "3":
    print("you return to the village and meet a wise old man.")
    print("he tells you,The dragon in the vace guards a great treasure,but you must be clever to obtain it.")
    print("Hint:sneaking is often wiser than fighting!")
else:
    print("invalid choice you selected,please select correct option.")

print("****GAME OVER****")
