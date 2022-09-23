import sys
import random

def start():
    print("\n Type esc to exit\n")
    print("\n----------------\n\nLet's Start")
    print("\n----------------\n\nRock Paper Scissors Go!!!: ")
    while True:
        ion = -1
        ion_pc = random.randrange(0, 3)
        guess = input("     Rock(r), Paper(p), Scissors(s): ")


        if guess == "esc".lower():
            print("\n----------------\n\nGAME OVER")
            sys.exit()

        if guess.lower() in ["rock", "r"]:
            ion = 0
            
        if guess.lower() in ["paper", "p"]:
            ion = 1

        if guess.lower() in ["scissors", "s"]:
            ion = 2
        

        if ion == -1:
            print("         select valid word or character")

        elif ion == ion_pc:
            print("         Match")


        

start()