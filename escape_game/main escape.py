from escapegame_funcs import *

# Main game loop
while True:
    # Reset global state
    items = []
    dead = False
    esc = False
    clown = True
    current_room = 0

    # Game intro
    slow_type(
        "You jolt awake in a dusty bedroom.\n"
        "There’s no memory of how you got here.\n\n"
        "The door is shut, and outside the window, it’s just fog.\n"
        "You feel like someone — or something — has trapped you here.\n"
        "But they clearly didn't try very hard.\n\n"
        "You must escape.\n\n"
        "All you have is your wits, your socks, and the faint smell of tuna.\n\n"
        "You look around the room.\n"
        "There’s a dusty bed, an old nightstand, a closet, and a door that seems to lead to a hallway.\n"
    )

    # Gameplay loop until win or death
    while not dead:
        if current_room == 0:
            bedroom()
        elif current_room == 1:
            slow_type("You return to the dusty bedroom.\n")
            bedroom()
        elif current_room == 2:
            slow_type("You enter the long dark hallway, counting 5 total doors.\n")
            hall()
        elif current_room == 3:
            slow_type("You enter the moldy bathroom.\nYou see a shower, a toilet, and a mirror.\n")
            bath()
        elif current_room == 4:
            slow_type("You enter the kitchen.\nA table and a cat guard the cabinets.\n")
            kitchen()
        elif current_room == 5:
            slow_type("You slowly open the closet door...\n")
            closet()
        elif current_room == 6 and not esc:
            slow_type("Seems like I should try this final door.\n")
            escape()
        if esc or dead:
            break

    # End screen and replay prompt
    slow_type("Thanks for playing. Would you like to play again?\nYes: 1, No: 2")
    playagain = input("-> ")
    if playagain != '1':
        break
