import time
import random


def print_pause(sentence):
    print(sentence)
    time.sleep(2)


def intro():
    print_pause("You find yourself in a dark dungeon.")
    print_pause("In front of you are two passageways.")


def choice():
    print_pause("What would you like to do?")


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


def intro():
    print_pause("You find yourself in a dark dungeon.")
    print_pause("In front of you are two passageways.")


def dungeon(items):
    print_pause("What would you like to do?")
    direction = input("1. Go left\n2. Go right\n")
    while direction != "1" and direction != "2":
        direction = input("Please enter 1 or 2.\n")
    if direction == "1":
        magic_room(items)
    elif direction == "2":
        lake(items)


def magic_room(items):
    chest = [" a magic book", " a shining sword"]
    print_pause("You enter a room seems like an old library.")
    if len(items) == 0:
        print_pause("You notice that there is a treasure chest!")
        items.append(random.choice(chest))
        print_pause("You tried to find something in the chest,"
                    "and finally you got" + items[0] + "!")
    print_pause("You can't find anything else so you return to the dungeon.")
    dungeon(items)


def lake(items):
    print_pause("You find yourself standing before a lake."
                "It seems that there is no other way to go.")
    if " a magic book" in items:
        print_pause("You sit down and read the magic book."
                    "The book teaches you a kind of magic"
                    " which can make you breath in the water !")
        items.append("magic")
    print_pause("So you dive into the lake.")
    print_pause("You notice there is something shining"
                " in the bottom of the lake.")
    deeper = input("Want to get closer?\nEnter Yes or No\n").lower()
    while ("yes" not in deeper) and ("no" not in deeper):
        deeper = input("Please enter Yes or No.\n").lower()
    if "yes" in deeper:
        if "magic" in items:
            print_pause("So lucky, you got a cloak of invisibility!")
            items.append("cloak")
        else:
            print_pause("It's too deep to achieve.")
    print_pause("You swim forward.")
    print_pause("You find a large hole that you can pass through."
                "You pass through the hole, get to the shore"
                "and you find yourself in front of a dragon!")
    dragon(items)


def dragon(items):
    if "cloak" in items:
        print_pause("You get scared and take on the cloak."
                    "You bypass the dragon quietly, "
                    "the dragon doesn't notice you.")
    else:
        fight = input("Would you like to (1) fight or (2) run away?")
        while fight != "1" and fight != "2":
            fight = input("Please enter 1 or 2.\n")
        if fight == "1":
            if " a shining sword" in items:
                print_pause("You take out your sword. "
                            "The sword shines brightly."
                            "You rush to the dragon,stab it."
                            "A huge explosion !")
                print_pause("You knock down the dragon !")
            else:
                print_pause("It's not a good idea to fight with a"
                            " dragon with nothing in hand."
                            "The dragon get angry and kill you.")
                game_over()
        elif fight == "2":
            print_pause("You got scared, so you escape "
                        "and return to the dungeon.")
            dungeon(items)
    print_pause("You notice that there is the exit !")
    print_pause("Congratulations ! You escape from the dungeon !")
    game_again()


def game_over():
    print_pause("Game Over")
    game_again()


def game_again():
    print_pause("Do you want to play again?")
    again = input("Please enter Yes or No.\n").lower()
    while ("yes" not in again) and ("no" not in again):
        again = input("(Please enter Yes or No.)\n").lower()
    if "yes" in again:
        print_pause("Loading...")
        play_game()
    elif "no" in again:
        print_pause("Thank you for playing.")
        exit()


def play_game():
    items = []
    intro()
    dungeon(items)


play_game()
