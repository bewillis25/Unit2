floor_1 = ['nothing','sword','sword','monster','up stairs']
floor_2 = ['down stairs','sword','monster','magic stone','up stairs']
floor_3 = ['down stairs','monster','sword','boss monster','prize']
user_room = 0
user_floor = 0
floor_list = [floor_1,floor_2,floor_3]
inventory = []
print("Welcome to this text themed adventure game. You may enter in 8 commands: \n 'left' allows you to move one room to the left \n 'right' allows you to move one room to the right \n 'up' allows you to move up an up staircase \n 'down' allows you to move down a down staircase \n 'fight' allows you to fight a monster if you encounter one \n 'grab' allows you to pick up an item and put in in your 3 slot inventory \n 'help' brings up this menu again \n 'quit' ends the game ")
action = ''
while action != 'quit':
    print(f"You are in room {str(user_room + 1)} on floor {str(user_floor + 1)}")
    print(f"The item in this room is: {floor_list[user_floor][user_room]}")
    action = input("    Enter a command: ")
    if action == 'left':
        if user_room == 0:
            print("I'm sorry, there is no room to the left.")
        elif user_room != 0:
            user_room = user_room - 1
    if action == 'right':
        if user_room == 4:
            print("I'm sorry, there is no room to the right.")
        elif user_room != 4:
            user_room = user_room + 1  
    if action == 'up':
        if floor_list[user_floor][user_room] != 'up stairs':
            print("I'm sorry, there are no stairs to go up.")
        elif floor_list[user_floor][user_room] == 'up stairs':
           user_floor = user_floor + 1
           user_room = 0
    if action == 'down':
        if floor_list[user_floor][user_room] != 'down stairs':
            print("I'm sorry, there are no stairs to go down.")
        elif floor_list[user_floor][user_room] == 'down stairs':
            user_floor = user_floor -1
            user_room = 0
    if action == 'help':
        print("Welcome to this text themed adventure game. You may enter in 8 commands: \n 'left' allows you to move one room to the left \n 'right' allows you to move one room to the right \n 'up' allows you to move up an up staircase \n 'down' allows you to move down a down staircase \n 'fight' allows you to fight a monster if you encounter one \n 'grab' allows you to pick up an item and put it in your 3 slot inventory \n 'help' brings up this menu again \n 'quit' ends the game ")
    if action == 'grab':
        if len(inventory) < 3:
            if floor_list[user_floor][user_room] == 'nothing':
                print("There is nothing to pick up.")
            elif floor_list[user_floor][user_room] == 'sword' or 'magic stone':
                inventory.append(floor_list[user_floor][user_room])
                print(f"Your inventory is now: {inventory}")
                floor_list[user_floor][user_room] = 'nothing'
            else:
                print("You can't pick that up.")
        elif len(inventory) >= 3:
            replace = int(input(f"Your inventory, {inventory}, is full. Enter '1' to replace the first item, '2' to replace the second item, '3' to replace the third item, and '0' to leave your inventory as is is."))
            if replace == 1:
                inventory[0] = floor_list[user_floor][user_room]
            elif replace == 2:
                inventory[1] = floor_list[user_floor][user_room]
            elif replace == 3: 
                inventory[2] = floor_list[user_floor][user_room]
            elif replace == 0:
                pass
            else:
                print(f"That is not an allowed command. Try again: {replace}")
    if action == 'fight':
        if floor_list[user_floor][user_room] == 'monster':
            if 'sword' in inventory:
                print("You defeated the monster with your sword, but it broke in the process. The monster has vansihed due to the magic of the boss monster lying in wait for you on thr top floor.")
                floor_list[user_floor][user_room] = 'nothing'
            elif 'sword' not in inventory:
                no_sword_monster_action = input("You have no sword to fight the monster with. Would you like to leave the room using 'leave' or try to run past the monster using 'run'? ")
                if no_sword_monster_action == 'leave':
                    print("You leave the room in the same direction you came from.")
                    user_room = user_room - 1
                elif no_sword_monster_action == 'run':
                    print("You attempted to run past the monster unarmed and were slain.")
                    break
        else:
            print("There is nothing to fight here.")









            
    

        
