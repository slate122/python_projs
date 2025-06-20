import sys,time

# Typewriter effect for game narration
def slow_type(text):
    for i in text:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.06)

# Inventory system
items = []
def add_item(item):
    global items
    if item not in items:
        items.append(item)
        slow_type(f"\nYou picked up the {item}!\n")
    else:
        slow_type("\nYou already have this item\n")

# Game state flags
esc = False
dead = False
clown = True
current_room = 0

def move_room(r):
    global current_room
    current_room = r

# Bedroom logic
def bedroom():
    while True:
        global current_room
        slow_type("What do you want to do? \n(open door: 1 , search nightstand: 2, search closet: 3, search bed: 4)")
        do = input("-> ")

        if do == "1":
            if 'flashlight' not in items:
                slow_type("It's too dark to see anything...\nYou turn back around.\n")
            else:
                move_room(2)
                break

        elif do == "2":
            slow_type("You walk over to the nightstand and notice a drawer is slightly ajar.\n you slide it open with a loud screech\n\n")
            if "flashlight" not in items:
                slow_type("Inside you find a flashlight...\n")
                add_item("flashlight")
            else:
                slow_type("The drawer is empty.")

        elif do == "3":
            slow_type("You open the closet... dirty undies everywhere\n")
            slow_type("Do you...\nSearch the pile of dirty undies: 1, turn back:2")
            closet = input("-> ")
            if closet == '1' and "tuna can" not in items and "empty can" not in items:
                slow_type("You find a tuna can.\n")
                add_item("tuna can")

        elif do == "4":
            if "flashlight" not in items:
                slow_type("Too dark to see under the bed.\n")
            else:
                slow_type("Nothing but dustbunnies under the bed.\n")

# Hall navigation
def hall():
    while True:
        slow_type("You stand in the hallway. Doors are all around you.\n")
        slow_type("What do you want to do? \n(1: bedroom, 2: left door, 3: opposite door, 4: diagonal door, 5: end of hall)")
        do = input("-> ")

        if do in ["1", "2", "3", "4", "5"]:
            move_room(int(do))
            break

# Bathroom logic
def bath():
    fog = False
    while True:
        slow_type("What do you want to do?\n(1: toilet, 2: mirror, 3: shower, 4: return)")
        do = input("-> ")

        if do == "1":
            slow_type("No toilet paper. Shame.\n")

        elif do == "2":
            if not fog:
                slow_type("Can't see your reflection.\n")
            else:
                slow_type("Fog reveals: 5 7 1 6\n")

        elif do == "3":
            while True:
                slow_type("Use cold water: 1, hot water: 2, go back: 3")
                foginp = input("-> ")

                if foginp == '1':
                    slow_type("Just cold water. Nothing happens.\n")
                    break
                elif foginp == '2':
                    slow_type("Room fogs up from hot water.\n")
                    fog = True
                    break
                elif foginp == '3':
                    break

        elif do == "4":
            move_room(2)
            break

# Kitchen logic
def kitchen():
    while True:
        slow_type("(1: table, 2: cat/cabinets, 3: return)")
        do = input("-> ")

        if do == '1':
            if "knife" not in items:
                slow_type("You take the knife.\n")
                add_item("knife")
            else:
                slow_type("Nothing on the table.\n")

        elif do == '2':
            if "tuna can" not in items and "empty can" not in items:
                slow_type("The cat hisses. Can't get to the cabinet.\n")
                break
            elif "tuna can" in items:
                slow_type("You feed the cat and get a key.\n")
                add_item("key")
                items.remove("tuna can")
                items.append("empty can")
                break
            else:
                slow_type("Nothing more to do here.\n")
                break

        elif do == '3':
            move_room(2)
            break

# Closet encounter
def closet():
    global clown, dead

    if clown:
        slow_type("You see a clown. He charges.\n")
        slow_type("Fight: 1, Run: 2")
        do = input("-> ")

        if do == '1':
            if "knife" not in items:
                slow_type("You die.\n")
                dead = True
            else:
                slow_type("You kill the clown.\n")
                clown = False
                move_room(2)

        elif do == '2':
            slow_type("You try to run but die.\n")
            dead = True

    else:
        slow_type("Just a dead clown here.\n")
        move_room(2)

# Escape logic
def escape():
    global esc

    if "key" not in items:
        slow_type("Door won't budge. Need something.\n")
        move_room(2)
        return

    slow_type("You use the key, but there's a code lock.\n")
    code = input("Enter 4-digit code: ")

    while code != "5716":
        slow_type("Incorrect. Try again: 1, Return: 2")
        choice = input("-> ")
        if choice == '2':
            move_room(2)
            return
        code = input("Enter 4-digit code: ")

    slow_type("You escaped. Congrats!\n")
    esc = True
