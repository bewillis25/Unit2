floor_1 = ['nothing','sword','nothing','monster','up stairs']
floor_2 = ['down stairs','nothing','monster','magic stone','up stairs']
floor_3 = ['down stairs','monster','nothing','boss monster','prize']
user_room = 0
user_floor = 0
floor_list = [floor_1,floor_2,floor_3]
inventory = ['','','']
user_status = 'alive'
print("Welcome to this text themed adventure game. You may enter in 8 commands: \n 'left' allows you to move one room to the left \n 'right' allows you to move one room to the right \n 'up' allows you to move up an up staircase \n 'down' allows you to move down a down staircase \n 'fight' allows you to fight a monster if you encounter one \n 'grab' allows you to pick up an item and put in in your 3 slot inventory \n 'help' brings up this menu again \n 'quit' ends the game ")
action = ''
while user_status == 'alive' and action != 'quit':
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
    if action == 'down':
        if floor_list[user_floor][user_room] != 'down stairs':
            print("I'm sorry, there are no stairs to go down.")
        elif floor_list[user_floor][user_room] == 'down stairs':
            user_floor = user_floor -1
    if action == 'help':
        print("Welcome to this text themed adventure game. You may enter in 8 commands: \n 'left' allows you to move one room to the left \n 'right' allows you to move one room to the right \n 'up' allows you to move up an up staircase \n 'down' allows you to move down a down staircase \n 'fight' allows you to fight a monster if you encounter one \n 'grab' allows you to pick up an item and put it in your 3 slot inventory \n 'help' brings up this menu again \n 'quit' ends the game ")
    if action == 'grab':
        if floor_list[user_floor][user_room] == 'monster' or 'boss monster' or 'up stairs' or 'down stairs':
            print("You can't add these things to your inventory.")
        else:
            inventory[0] = floor_list[user_floor][user_room]
            print(f"{inventory}")





            
    

        
