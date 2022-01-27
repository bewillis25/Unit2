'''
##############################
User Input Challenge
##############################

Create a program that asks the user to enter their name and their age. Print out a message 
addressed to them that tells them the year that they will turn 100 years old.

Add on to the previous program by asking the user for another number and printing out that 
many copies of the previous message. (Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. 
(Hint: the string "\n" is the same as pressing the ENTER button)
'''

# Original year you will turn 100 program.
name1 = input("What is your name? ")
age1 = int(input("What is your age? "))
current_year = int(2021)
year_you_will_turn_100 = (current_year-age1)+(100)
print(f"{name1}, you will turn 100 in the year {year_you_will_turn_100}.")

# Copied year you will turn 100 program.
name2 = input("What is your name? ")
age2 = int(input("What is your age? "))
copy_number = int(input("Enter a number: "))
current_year = int(2021)
year_you_will_turn_100 = (current_year-age2)+(100)
print(f"{name2}, you will turn 100 in the year {year_you_will_turn_100}. \n" * copy_number)


