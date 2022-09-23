import sys

def start():
    print("\n Type esc to exit\n")
    while True:
        guess = input("Rock(r), Paper(p), Scissors(s): ")
        if guess == "esc".lower():
            print("\n----------------\n\nGAME OVER")
            sys.exit()

start()