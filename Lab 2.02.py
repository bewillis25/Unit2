'''
##################################
Lab 2.02 Booleans & Expressions
##################################
In your Notebook
Predict if each of the following examples will produce a True or False output. Check your answers in interactive mode.
                 
Example 1
    >>> a = 100
    >>> b = "science"
    >>> a > 75 and b == "science"       Prediction: true                     Actual: true
Example 2
    >>> a = 100
    >>> b = "science"
    >>> a > 75 and b != "science"       Prediction: false                     Actual: false
Example 3
    >>> a = 100
    >>> b = "science"
    >>> a > 75 or b != "science"        Prediction:  true                   Actual: true
Example 4
    >>> a = 100
    >>> b = "science"
    >>> c = True
    >>> not c and a > 75 and b == "science"     Prediction: false                 Actual: false

In your Console

Complete the following coding challenge
Create a "Can I be President?" program, which determines if the user meets the minimum requirements for becoming the President of the United States. 
Have the user input the information needed.

The minimum requirements to be president of the United States are:

1. Older than 35

2. Resident of US for 14 Years

3. Natural born citizen

Print True if the person could be president and False if they can't be president.

Create a "I can't be President?" program. Print True if the user cannot be President and False if they can be President.

Create a "Can I ride the roller coaster?" program. A roller coaster has the rule that a rider has to be over the height of 50 inches. Because of a legal loophole, if you are over the age of 18 you can ride regardless of your height. If you are allowed to ride, the coaster costs 4 quarters (although the operator accepts tips so more money is appreciated).

Also, the theme park sells frequent rider passes: with a frequent rider pass the roller coaster costs only 2 quarters. Ask the user how tall they are in inches, their age, how many quarters they have, and if they have a frequent rider pass. Print True if the person can ride and False if they can't.


Are the following expressions equivalent? Research DeMorgan's Laws and write why you think they are the same or why they are not the same
not(x or y) == not x and not y   I think this is true, since if 'x or y' is True, not(x or y) will be False, and so will 'not x and not y' because either x or y had to be True, and not(True) == False and 'False and (True or False)' is False just like not(x or y). The same logic applies if 'x or y' is False, where both x and y have to be False, so 'not x and not y' will be True because 'not(False) and not(False)' == True, just like not(x or y).

not(x and y) == not x or not y   I think this is true as well, since if 'x and y' is True, then not(x and y) == False, and because both x == True and y == True, 'not x or not y' will also be False, since 'not(True) or not(True)' is False. The same logic also applies if 'x and y' is False, where not(x and y) == True, and because either x or y is False, we know either 'not x' or 'not y' will be True, and 'not(False) or not(False or True)' will be True, just like not(x and y).
'''
# Can I be president
age1 = int(input("What is your age? "))
resident_time = int(input("How many years have you been a resident of the US? "))
natural_born_citizen = input("Are you are natural born citizen of the US, yes or no: ")
can_be_president = age1 > 35 and resident_time >= 14 and natural_born_citizen == 'yes'
if can_be_president == True:
    print("You can be president.")
elif can_be_president == False:
    print("You can't be president.")

# Can I ride the roller coaster
age2 = int(input("What is your age? "))
height = int(input("What is your height in inches? "))
money = int(input("How many quarters do you have? "))
rider_pass = input("Do you have a frequent rider pass, yes or no: ")
can_i_ride = (age2 >= 18 or height > 50) and ((rider_pass == 'yes' and money >= 2) or money >= 4)
if can_i_ride == True:
    if rider_pass == 'yes':
        print("That will cost 2 quarters. Have a fun ride. ")
    elif rider_pass == 'no':
        print("That will cost 4 quarters. Have a fun ride.")
if can_i_ride == False:
    print("Sorry, but you can't ride.")

