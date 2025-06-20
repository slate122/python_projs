import sys,time

#Global Vraibles
items=[]
dead = False
esc = False
clown = True
current_room = 1

#All Necessary Functions
def slow_type(text):
    for i in text:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.05)  # Adjust the speed of typing here

def add_item(item):
    global items
    if item not in items:
        items.append(item)
        slow_type(f"\nYou picked up the {item}!\n")
    else:
        slow_type(f"\nYou already have this item\n")

def move_room(r):
    global current_room
    current_room = r

def bedroom():
    while True:
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
                slow_type("Inside you find a flashlight and turn it on... \nnothing happens. You give it a hard bang on the nightstand and it flickers on\n\n... you have added the flashlight into your inventory.\n")
                add_item("flashlight")
            else:
                slow_type("The drawer is empty.")
        elif do == "3":
            slow_type("You open the closet door and are greeted with the smell of fish and cockroaches scurrying out form a pile of dirty undies\n")
            slow_type("Do you...\nSearch the pile of dirty undies: 1, turn back:2")
            closet = input("-> ")
            if closet == '1':
                if "tuna can" not in items and "empty can" not in items:
                    slow_type("You toss aside some dirty undergarments and your hand feels somthing wet and squishy\nYou grab at it and feel a metal can.\n Upon pulling it out of the mess you see it's a tuna can... may come in handy?\n\n... you have added the tuna can into your inventory.\n")
                    add_item("tuna can")
                    slow_type("You step away from the foul smelling undies\n")
            else:
                slow_type("You back away from the foul smelling undergarments.\n")
        elif do == "4":
            if "flashlight" not in items:
                slow_type("It's a bit dark under here, hard to see anything\nYou get up from looking under the bed\n")
            else:
                slow_type("You click on the flashlight and look under the bed. Nothing but dustbunnies under there.\nYou stand back up\n")
        else:
            pass

def hall():
    while True:
        slow_type("From the center of the hallway, the door to the bedroom is behind you.\nThere is a door directly to the left on the same wall as the bedroom, one in front of you,\n one across the hall diagonally, and one at the very end of the hall with a faint green glow.\n\n")
        slow_type("What do you want to do? \n(open bedroom door: 1 , open door to the left of the bedroom: 2, open the door across the bedroom: 3, open the door diagonal to the bedroom: 4, open the door at the end of the hall: 5)")
        do = input("-> ")
        if do == "1":
            move_room(1)
            break
        elif do == "2":
            move_room(3)
            break
        elif do == "3":
            move_room(4)
            break
        elif do == "4":
            move_room(5)
            break
        elif do == "5":
            move_room(6)
            break
        else:
            continue
        

def bath():
    fog = False
    while True:
        slow_type("what do you want to do? \n(use the toilet: 1, look at the mirror: 2, examine the shower: 3, return to the hallway: 4)")
        do = input("-> ")
        if do =="1":
            slow_type("Man, a toilet! You have been needing to go for a long time! \nYou sit down and drop a fat deuce... but to your horror... there is no toilet papper.\nYou stand up in shame, feeling awful about your life choices.\n ")
        elif do =="2":
            if fog == False:
                slow_type("You look into the mirror, but for some reason, can't see your reflection... Wierd.\n")
            else:
                slow_type("Suddenly a message seems to appear due to the steam fogging the mirror.\n It seems like numbers...\n 5 7 1 6\n\n hmmn, I should probably remember those.")
        elif do == "3":
            while True:
                slow_type("Seems like a normal shower, what should I do?\n(turn on the cold water: 1, turn on the hot water: 2, go back: 3)")
                foginp = input("-> ")
                if foginp == '1':
                    slow_type("You turn on the cold water.\n The water thats coming out is cold... shocker\n Better not to waste water, so you turn it off.\nYou step away from the tub")
                    break
                elif foginp == '2':
                    slow_type("You turn on the hot water\n normally you don't want to waste water....\nbut the room is filling up with steam and it feels good.\nYou step away from the tub\n")
                    fog = True
                    break
                elif foginp=='3':
                    break
                else:
                    continue
        elif do == "4":
            move_room(2)
            break

def kitchen():
    while True:
        slow_type("What do you want to do?\n(examine the table: 1, go to the cabinents where the cat is: 2, return to the hall: 3)")
        do = input("-> ")
        if do=='1':
            if "knife" not in items:
                slow_type("There is a huge knife laid out on the table...\nbetter i take it for protection\n")
                add_item("knife")
            else:
                slow_type("There appears to be nothing on the table\n")
        elif do =='2':
            if "tuna can" not in items and "empty can" not in items:
                slow_type("As I start to approach the cabinents, the cat starts to growl and hiss at me.\n I take one step closer and it swats at me, almost scratching me...\n hmm i need to find a way to get it to move.\n")
                break
            elif "tuna can" in items:
                slow_type("This cat seems hungry, maybe I can offer it that tuna can I found.\nYou throw the can down and slide it to the side.\nthe cat licks his lips and walks over to the can.\n You are able to access the cabinents and within side you find a rusty key!\n\n")
                add_item("key")
                items.remove("tuna can")
                items.append("empty can")
                break
            else:
                slow_type("hmm, not sure if there is anything else for me here.\n")
                break
        elif do =='3':
            move_room(2)
            break

def closet():
    global clown, dead
    if clown  == True:
        slow_type("The closet goes much deeper than you expected it to.\n It's almost like it's on hallway.\n At the end of the other side, you see a dark shadowy figure slowly turning around toward you.\n He has clown makeup on.\nIt starts to move quickly toward you!!\n")
        slow_type("What will you do?\n(fight: 1, run: 2)")
        do = input("-> ")
        while True:
            if do == '1':
                if "knife" not in items:
                    slow_type("You decide to try and fight this clown.\n You throw a punch but he easily catches it.\n The next thing you know you see a giant clownshoe headed directly at your face.\n You attampt to duck but are too slow\n the world fades to black...\n\nGAME OVER!")
                    dead = True
                    break
                else:    
                    slow_type("You decide to try and fight this clown.\n You throw a punch but he easily catches it.\n The next thing you know you see a giant clownshoe headed directly at your face.\n You are able to duck the kick and pull out the knife\nyou run towards the clown and plant the knife firmly in his neck\nThe clown falls to the ground.\n")
                    clown = False
                    slow_type("With nothing more to see in the closet, you return to the hall\n\n")
                    move_room(2)
                    break
            elif do =='2':
                slow_type("You turn and run as fast as you can.\n sadly, you're not very fast.\n The clown easily catches up and splits your skull with a karate chop\n the world fades to black \n\nGAME OVER!!\n")
                dead = True
                break
            else:
                continue
    elif clown == False:
        slow_type("There is just a dead clown, lets move to the hall.\n\n")
        move_room(2)
                
def escape():
    global esc
    if "key" not in items:
        slow_type("The door won't budge...\nI must be missing something\nYou step back to the hallway\n")
        move_room(2)
    else:
        slow_type("You insert the key into the door but it won't budge.\nYou notice a keypad to the side.\nMaybe there is also a code\n")
        slow_type("Please input the 4 digit code (no spaces)\n")
        code = input("-> ")
        while code != "5716":
            slow_type("Code incorrect. What would you like to do?\nTry again: 1, Go back: 2\n")
            tryagain = input("-> ")
            if tryagain == '2':
                slow_type("Returning to hall\n")
                move_room(2)
                break
            else:
                slow_type("Trying again\n")
                code = input("Input Code -> ")
        if current_room == 6:
            slow_type("You have entered the correct code and escaped\n CONGRATULATIONS, YOU HAVE WON!!\n\n")
            esc = True 

#Main Game Loop
while True:
    slow_type("You jolt awake in a dusty bedroom.   \nThere’s no memory of how you got here.    \n\nThe door is shut, and outside the window, it’s just fog.    \nYou feel like someone — or something — has trapped you here.    \nBut they clearly didn't try very hard.    \n\nYou must escape.    \n\nAll you have is your wits, your socks, and the faint smell of tuna.\n")
    slow_type("\n\nYou look around the room.    \nThere’s a dusty bed, an old nightstand,a closet, and a door that seems to lead to a hallway.    \n You consider your options.\n\n")

    while dead == False:
        if current_room==1:
            slow_type("You return to the dusty bedroom.\n")
            bedroom()
        elif current_room == 2:
            slow_type("You enter the long dark hallway, counting 5 total doors.\n")
            hall()
        elif current_room == 3:
            slow_type("You enter the moldy bathroom.\n You see a shower, a toilet and a mirror.\n")
            bath()
        elif current_room == 4:
            slow_type("You enter the kitchen.\n You see a table and some cabinents with a cat sat in front of them.\n")
            kitchen()
        elif current_room == 5:
            slow_type("You make your way over to the closet door, opening it very slowly...\n")
            closet()
        elif dead == True:
            break
        elif current_room == 6 and esc == False:
            slow_type("Seems like i should try and go through this door.\n")
            escape()
        elif esc == True:
            break
    slow_type("Thanks for playing, would you like to play again?\nYes: 1, No: 2")
    playagain = input("-> ")
    if playagain == '2':
        break
    elif playagain == '1':
        items = []
        dead = False
        esc = False
        clown = True
        current_room = 1
        continue