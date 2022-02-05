'''
#################
Lab 2.06
#################
1. In your Notebook
-------------------
Predict what will be printed then type the program in your console to confirm
Example 1
    a = 0
    while a < 10:
        print(a)

prediction: 0, and it will keep on printing this forever, unless a > 10.
actual: Same as prediction

Example 2
    a = 0
    while a < 10:
        a = a + 1
        print(a)

prediction: 1 \n 2 \n 3 \n 4 \n 5 \n 6 \n 7 \n 8 \n 9 \n 10
actual: Same as prediction

2. In your Notebook
-------------------
Create a set of test cases for the following sample code and predict the behavior
    a = input("Would you like to quit: ")
    while a != "y" and a != "n" :
        a = input("Would you like to quit: ")

test cases: 'y', 'n', 'q', 'cat'
Code will terminate if a = 'y' or a = 'n', but if a = 'cat' or 'q' it will keep asking "Would you like to quit"

3. Implement the Tic Tac Toe game using a while loop
----------------------------------------------------
Allow users to keep playing (max 9 times).

Use variables to decide whose turn it is, and greet them as Xs or Os.

User picks a location on the board according to the number:
        1 | 2 | 3
        ---------
        4 | 5 | 6
        ---------
        7 | 8 | 9


Depending on the position user gave, update the corresponding position of the board to reflect that.

Print the updated board out.

You will not need to determine the winner at this point.
(Copy and paste your previous tic-tac-toe version and modify the code to implement the above)
'''

# New Tic-Tac-Toe Game With While Loop
a = ['1','2','3','4','5','6','7','8','9']
print("This is a two player Tic-Tac-Toe game so there will be alternating turns. The board diagram is shown below. Enter the number of the square you wish to put your X or O.")
print(f" {a[0]} | {a[1]} | {a[2]} \n --------- \n {a[3]} | {a[4]} | {a[5]} \n --------- \n {a[6]} | {a[7]} | {a[8]}")
i = 1
while i < 5:
    p1_i_turn = int(input("Player 1, select a square: "))
    a[p1_i_turn-1] = 'X'
    board = f" {a[0]} | {a[1]} | {a[2]} \n --------- \n {a[3]} | {a[4]} | {a[5]} \n --------- \n {a[6]} | {a[7]} | {a[8]}"
    print(board)
    p2_i_turn = int(input("Player 2, select a square: "))
    a[p2_i_turn-1] = 'O'
    board = f" {a[0]} | {a[1]} | {a[2]} \n --------- \n {a[3]} | {a[4]} | {a[5]} \n --------- \n {a[6]} | {a[7]} | {a[8]}"
    print(board)
    i = i + 1  
p1_i_turn = int(input("Player 1, select a square: "))
a[p1_i_turn-1] = 'X'
board = f" {a[0]} | {a[1]} | {a[2]} \n --------- \n {a[3]} | {a[4]} | {a[5]} \n --------- \n {a[6]} | {a[7]} | {a[8]}"
print(board)

    










