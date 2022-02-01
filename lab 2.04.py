'''
###########################
Lab 2.04
###########################
1. In your notebook
For each example below, predict what will be printed. Run the program and write down the output in your notebook.

Example 1
    a = ['a', 'b', 'c', 'd', 'e']
    print(a[0])
    print(a[3])

    prediction: print(a[0]) will print a, print(a[3]) prints d                                           
    actual:  same as prediction

Example 2
    a = ['a', 'b', 'c', 'd', 'e']
    print(a[len(a) - 3])

    prediction: print(a[len(a)-3]) is print(a[2]) which is the middle value of a which is c.
    actual: c

Example 3
    a = ['a', 'b', 'c', 'd', 'e']
    print(a[len(a) - 6])

    prediction: goes left of a which loops back to e, so it prints e.
    actual: e

Example 4
    a = ['a', 'b', 'c', 'd', 'e']
    a[3] = 'haha'
    print(a)

    prediction: ['a','b','c','haha','e'], replaces a[3] which was 'd' with 'haha'
    actual: ['a','b','c','haha','e']

2. Create this game again using lists and indexes
--------------------------------------------------
Declare 10 prizes (prize0, prize1, prize2 at the top of your file), but store them all in a list.

User picks a number.

Print prize associated with the door user picked.

# Game show using lists
a = ['car','new house','nothing','free pizza','free vacation','trip to the superbowl','new laptop','free carwashes for a year','a cat','a lamp']
name = input('Hello, thanks for coming to our game show tonight. What is your name? ')
num = int(input(f"That's great! Thanks for being here {name}. Tonight you have the chance to win of of ten mystery prizes. As you see before you, there are ten doors labeled one to ten, and what you're going to do is pick a number and you will win whatever's behind that door. Okay, pick a number from 1-10. "))
if num == 1:
    print(f"You win {a[0]}!")
elif num == 2:
    print(f"You win {a[1]}!")
elif num == 3:
    print(f"You win {a[2]}!")
elif num == 4:
    print(f"You win {a[3]}!")
elif num == 5:
    print(f"You win {a[4]}!")
elif num == 6:
    print(f"You win {a[5]}!")
elif num == 7:
    print(f"You win {a[6]}!")
elif num == 8:
    print(f"You win {a[7]}!")    
elif num == 9:
    print(f"You win {a[8]}!")
elif num == 10:
    print(f"You win {a[9]}!")
else:
    print("Did you even read the instructions?!")


3. Create a quiz
--------------------------------------------------
Create a food quiz using lists and indexes.

List of 6 different foods.

Ask the user 8 vague questions to find out what their favorite food is using the list.

Update the score and print their top 2 favorite foods.

Hint: Use a search engine to find the largest number in a python list.

----------------------
​Starter code here​:
----------------------
food = ['donuts', 'pancakes', 'bacon', 'waffles','eggs','baggles']
score = [0,0,0,0,0,0]

print('Please answer each questions with "y" for "yes" and "n" for "no."')
user_input = input('Do you like food with holes? ')
if user_input == 'y':
  score[0] = score[0] + 1
  score[5] = score[5] + 1

##############################
Together in class:
##############################
Research nested lists and work through the following Examples:

Bonus Example 1
a = ['a', 'b', 'c', ['d', 'e']]
print(len(a))
Bonus Example 2
a = ['a', 'b', 'c', ['d', 'e']]
b = a[3]
print(b)
Bonus - In your Notebook
How would you access d from the list a?
'''
food = ['donuts', 'pancakes', 'bacon', 'waffles','eggs','baggles']
score = [0,0,0,0,0,0]

print('Please answer each questions with "y" for "yes" and "n" for "no."')
user_input1 = input('Do you like food with holes? ')
if user_input == 'y':
  score[0] = score[0] + 1
  score[5] = score[5] + 1
else:
    pass
user_input2 = 

