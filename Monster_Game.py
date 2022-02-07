floor_1 = ['nothing','sword','nothing','monster','up stairs']
floor_2 = ['down stairs','nothing','monster','magic stone','up stairs']
floor_3 = ['down stairs','monster','nothing','boss monster','prize']
room = [0,1,2,3,4]
user_room = room[0]
user_floor = floor_1
item = user_floor[user_room]
dead_or_alive = 'alive'
action = input("What would you like to do? Enter 'help' for info: ")
while dead_or_alive == 'alive':
    if action == 'help':
        print(f" The action 'left' moves you one room to the left. \n The action 'right' moves you one room to the right. \n The action 'up' will take you up a staircase. \n The action 'down' will take you down a staircase. \n The action 'grab' lets you pick up an item in a room. \n The action 'fight' lets you try to defeat a monster. \n The action 'help' allows you see this menu. ")
        action
    if action == 'left':
        user_room = user_room + 1
        print(f"The item in this room is {item}.")
        action
        if user_room == 0:
            print(f"There is no room to the left. ")
            action
    elif action == 'right':
        user_room = user_room + 1
        print(f"The item in this room is {item}. ")
        action
        if user_room == 4:
            print(f"There is no room to the right.")
            action
    

        


       




