# Task 1: Code Correction

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    print("You find a hidden treasure!")

#Task 2: Setting the Scene
if place == "cave":
    action = input("light a torch or proceed in the dark?")
    if action == "light a torch":
        print("The pathway is lit, proceed!")
    elif action == "proceed in the dark":
        print("Proceed with caution!")
    #Task 3: Default Path
    elif action == "final flash frieza":
        pass 