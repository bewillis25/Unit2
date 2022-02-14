
#Text Monster Game 

#Initial variable settings and floor plan
floor_1 = ['nothing','sword','sword','monster','up stairs']
floor_2 = ['down stairs','sword','monster','magic stone','up stairs']
floor_3 = ['down stairs','monster','sword','boss monster','prize']
user_room = 0
user_floor = 0
floor_list = [floor_1,floor_2,floor_3]
inventory = []
print("Welcome to this text themed adventure game. You may enter in 8 commands: \n 'left' allows you to move one room to the left \n 'right' allows you to move one room to the right \n 'up' allows you to move up an up staircase \n 'down' allows you to move down a down staircase \n 'fight' allows you to fight a monster if you encounter one \n 'grab' allows you to pick up an item and put in in your 3 slot inventory \n 'help' brings up this menu again \n 'quit' ends the game ")
action = ''
# main game loop
while action != 'quit':
    # If item in room is a monster loop
    if floor_list[user_floor][user_room] == 'monster':
        monster_action = input("There is a monster in this room. You can choose 'fight' to try and defeat the monster, 'leave' to go back the way you came, or 'run' to try and run past the monster, which one do you choose? ")
        if monster_action == 'fight':
            if 'sword' in inventory:
                print("You defeated the monster with your sword, but it broke in the process. The monster's body vanishes in front of you.")
                floor_list[user_floor][user_room] = 'nothing'
                inventory.remove("sword")
            elif 'sword' not in inventory:
                print("You tried to fight the monster unarmed and were slain")
                print("GAME OVER")
                break 
        elif monster_action =='leave':
            print("You left the room the way you came in.")
            user_room = user_room - 1
        elif monster_action == 'run':
            print("You tried to run past the monster but he caught and ate you.")
            print("GAME OVER")
            break
        else:
            print("Please enter 'fight', 'leave', or 'run'.")
    # If item in room is the boss monster loop
    elif floor_list[user_floor][user_room] == 'boss monster':
        boss_monster_action = input("You have reached the boss monster who guards the treasure in the other room. You can try to use 'fight' to defeat him, 'leave' to go back the way you came, or 'run' to run past the boss monster. Which one do you choose? ")
        if boss_monster_action == 'fight':
            if 'sword' and 'magic stone' in inventory:
                print("You have defeated the boss monster and vanquished him back to the shadow realm. Your sword and magic stone have also vanished.")
                floor_list[user_floor][user_room] = 'nothing'
                inventory.remove("sword")
                inventory.remove("magic stone")
            elif 'sword' in inventory:
                print("You tried to fight the boss monster without the magic stone and were cut in half.")
                print("GAME OVER")
                break 
            elif 'magic stone' in inventory:
                print("You tried to defeat the boss monster without a sword and were crushed.")
                print("GAME OVER")
        elif boss_monster_action == 'leave':
            print("You leave the room the way you came in.")
            user_floor = user_floor - 1
        elif boss_monster_action == 'run':
            print("You really thought running past the boss monster would work?")
            print("GAME OVER")
            break 
        else:
            print("Please enter 'fight', 'leave', or 'run'.")
    # If the item in the room isn't a monster or a boss monster
    else:
        print(f"You are in room {str(user_room + 1)} on floor {str(user_floor + 1)}")
        print(f"The item in this room is: {floor_list[user_floor][user_room]}")
        action = input("    Enter a command: ")
        # Conditionals for actions done in game
        if action == 'left':
            if user_room == 0:
                print("I'm sorry, there is no room to the left.")
            elif user_room != 0:
                user_room = user_room - 1
        elif action == 'right':
            if user_room == 4:
                print("I'm sorry, there is no room to the right.")
            elif user_room != 4:
                user_room = user_room + 1  
        elif action == 'up':
            if floor_list[user_floor][user_room] != 'up stairs':
                print("I'm sorry, there are no stairs to go up.")
            elif floor_list[user_floor][user_room] == 'up stairs':
                user_floor = user_floor + 1
                user_room = 0
        elif action == 'down':
            if floor_list[user_floor][user_room] != 'down stairs':
                print("I'm sorry, there are no stairs to go down.")
            elif floor_list[user_floor][user_room] == 'down stairs':
                user_floor = user_floor -1
                user_room = 5
        elif action == 'help':
            print("Welcome to this text themed adventure game. You may enter in 8 commands: \n 'left' allows you to move one room to the left \n 'right' allows you to move one room to the right \n 'up' allows you to move up an up staircase \n 'down' allows you to move down a down staircase \n 'fight' allows you to fight a monster if you encounter one \n 'grab' allows you to pick up an item and put it in your 3 slot inventory \n 'help' brings up this menu again \n 'quit' ends the game ")
        elif action == 'grab':
            if len(inventory) <= 3:
                if floor_list[user_floor][user_room] == 'nothing':
                    print("There is nothing to pick up.")
                elif floor_list[user_floor][user_room] == 'sword':
                    inventory.append(floor_list[user_floor][user_room])
                    print("You picked up a sword.")
                    print(f"Your inventory is now: {inventory}")
                    floor_list[user_floor][user_room] = 'nothing'
                elif floor_list[user_floor][user_room] == 'magic stone':
                    inventory.append(floor_list[user_floor][user_room])
                    print("You picked up a magic stone.")
                    print(f"Your inventory is now: {inventory}")
                    floor_list[user_floor][user_room] = 'nothing'
                elif floor_list[user_floor][user_room] == 'prize':
                    print("You have defeated all the monsters and won the prize. I congratulate you on your success.")
                    print("YOU WON!")
                    break                   
                else:
                    print("You can't pick that up.")
        elif action == 'fight':
            print("There is no monster to fight here.")
        else:
            print("Please enter a valid command.")
            