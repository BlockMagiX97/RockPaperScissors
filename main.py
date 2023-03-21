import random

def start():
    print("\n Type esc to exit\n")
    print("\n----------------\n\nLet's Start")
    print("\n----------------\n\nRock Paper Scissors Go!!!: ")
    while True:
        user_input_index = -1
        machine_input_index = random.randrange(0, 3)
        guess = input("     Rock(r), Paper(p), Scissors(s): ")


        if guess.lower() == "esc":
            print("\n----------------\n\nGAME OVER")
            break

        if guess.lower() in ["rock", "r"]:
            user_input_index = 0
            
        if guess.lower() in ["paper", "p"]:
            user_input_index = 1

        if guess.lower() in ["scissors", "s"]:
            user_input_index = 2
        
        # evaluating part
        if user_input_index == -1:
            print("         select valid word or character")

        elif user_input_index == machine_input_index:
            print("         Match")
        
        elif (user_input_index + 1) % 3 == machine_input_index:
            print("         You lose")
        
        else:
            print("         You win")


        

start()
