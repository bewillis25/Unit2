'''
##########################################
Lab 2.03 - Game Show
##########################################
In your Notebook
Follow the flow of execution in the following programs and predict what will happen for each
one
---------------------------------------
Example 1
---------------------------------------
a = input("What... is your quest")
b = "to seek the holy grail"
if a != b:
    print("Go On. Off you go")
else:
    b = input("What...is the air-speed velocity of an unladen swallow?")
    if b == "What do you mean? An African or European swallow?":
        print("I don't know that...AHHH [Bridgekeeper was thrown over bridge]")
    else:
        print("[you were thrown over bridge]")

Prediction: Asks 'what is your quest'. If the answer isn't 'to seek the holy grail' it says'off you go' and if the user answers 'to seek the holy grail' it asks 'what the spped of a swallow'. If the user answers 'european or african' it says the bride guard died. If they say anything else, it says the user dies.
Actual: 

---------------------------------------
Example 2
---------------------------------------
user_input = input("What is your favorite color")
if user_input == 'blue':
    print("Blueskadoo")
elif user_input == "red":
    print("Roses are red!")
elif user_input == "yellow":
    print("Mellow Yellow")
elif user_input == "green":
    print("Green Machine")
elif user_input == "orange":
    print("Orange you glad I didn't say banana.")
elif user_input == "black":
    print("I see a red door and I want it painted black")
elif user_input == "purple":
    print("And we'll never be royalllssss")
elif user_input == "pink":
    print("Pinky- and the Brain")
else:
    print("I don't recognize that color. Is it even...??")

Prediction: Asks for a favorite color. If user's answer is blue, red,yellow, green, orange, black, purple, or pink it prints a funny message corresponding to the color. If any other color is said it prints 'is that even a color'
Actual:

---------------------------------------
In your Notebook
---------------------------------------
Translate this Snap! program into a Python program
***Refer to the image provided on Moodle located below the Lab 2.03 link***
Write program below:

---------------------------------------
Create a game show program
---------------------------------------
Declare 10 prizes (prize1, prize2, prize 3 at the top of your file)
User picks a number
The prize corresponding with that door is printed for the user.
Write code below the multiline comment
'''
# Snap Triangle Program
side1 = int(input("What is the length of side 1? "))
side2 = int(input("What is the length of side 2? "))
side3 = int(input("What is the length of side 3? "))
if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    print(f"The perimeter of the triangle is {side1 + side2 + side3}")
    if side1^2 + side2^2 == side3^2:
        print("This is a right triangle")
    elif side1 == side2 == side3:
        print("This is an equilateral triangle")
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print("This is an isosceles triangle")
    else:
        print("This is a scalene triangle")
else:
    print("These inputs don't make a triangle")

# Game show program 
prize1 = 'a new car'
prize2 = 'a lamp'
prize3 = '1 million dollars'
prize4 = 'a cat'
prize5 = 'a new house'
prize6 = 'nothing'
prize7 = 'a pencil'
prize8 = 'a free vacation'
prize9 = 'a new computer'
prize10 = 'a book'
name = input('Hello, thanks for coming to our game show tonight. What is your name? ')
num = int(input(f"That's great! Thanks for being here {name}. Tonight you have the chance to win of of ten mystery prizes. As you see before you, there are ten doors labeled one to ten, and what you're going to do is pick a number and you will win whatever's behind that door. Okay, pick a number from 1-10. "))
if num == 1:
    print(f"You win {prize1}!")
elif num == 2:
    print(f"You win {prize2}!")
elif num == 3:
    print(f"You win {prize3}!")
elif num == 4:
    print(f"You win {prize4}!")
elif num == 5:
    print(f"You win {prize5}!")
elif num == 6:
    print(f"You win {prize6}!")
elif num == 7:
    print(f"You win {prize7}!")
elif num == 8:
    print(f"You win {prize8}!")    
elif num == 9:
    print(f"You win {prize9}!")
elif num == 10:
    print(f"You win {prize10}!")
else:
    print("Did you even read the instructions?!")