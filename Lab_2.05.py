'''
############################
Lab 2.05 - Tic-Tac-Toe
############################
In your Notebook
1. Predict what will be printed. Then run the program and confirm
Example 1
---------
a = ['a', 'b', 'c', 'd', 'e']
print(a[0:3]) 
print(a[1:4]) 

Prediction: ['a','b','c'] and ['a','b','c','d']
Actual: Same as prediction

Example 2
---------
a = ['a', 'b', 'c', 'd', 'e']
print(a[1:len(a) - 3])

Prediction: ['b']
Actual: Same as prediction

Example 3
---------
a = ['a', 'b', 'c', 'd', 'e']
b = a.remove('b')
print(a)
print(b)

Prediction: ['a','c', 'd', 'e'] and None, since only pop returns the deletd value
Actual: Same as prediction

Example 4
---------
a = ['a', 'b', 'c', 'd', 'e']
a[0] = 'haha'
b = a.pop()
print(a)
print(b)

Prediction: ['haha','b','c','d'] (since pop() removes the last value if no specfied index) and 'e'
Actual: Same

Example 5
---------
a = ['a', 'b', 'c', 'd', 'e']
b = a + ['abc']
print(a)
print(b)

Prediction: ['a','b','c','d','e'] and ['a','b','c','d','e','abc']
Actual: Same

Example 6
---------
a = ['a', 'b', 'c', 'd', 'e']
b = a.append('f')
print(a)
print(b)

Prediction: ['a','b','c','d','e','f'] and 'f'
Actual: ['a','b','c','d','e','f'] and None (append is like remove in what it returns, not like pop)

2. In script mode (Type your program below the multi-line comment)
We are going to start implementing Tic-Tac-Toe using a single list.
1. The user picks a location on the board according to the number:
    1 | 2 | 3
    ---------
    4 | 5 | 6
    ---------
    7 | 8 | 9
2. Depending on the position that the user inputs, update the position of the board to an "X" to reflect
that.
    Example:
        1 | 2 | 3
        ---------
        4 | 5 | X
        ---------
        7 | 8 | 9
3. Print the updated board out, but don't worry about making it look pretty.
4. Only need to implement one turn of the game
'''

#Tic-Tac-Toe Game
a = ['1','2','3','4','5','6','7','8','9']
print("This is a two player Tic-Tac-Toe game so there will be alternating turns. The board diagram is shown below. Enter the number of the square you wish to put your X or O.")
print(f" {a[0]} | {a[1]} | {a[2]} \n --------- \n {a[3]} | {a[4]} | {a[5]} \n --------- \n {a[6]} | {a[7]} | {a[8]}")
for i in range(5):
    p1_i_turn = int(input("Player 1, select a square: "))
    a[p1_i_turn-1] = 'X'
    board = f" {a[0]} | {a[1]} | {a[2]} \n --------- \n {a[3]} | {a[4]} | {a[5]} \n --------- \n {a[6]} | {a[7]} | {a[8]}"
    print(board)
    p2_i_turn = int(input("Player 2, select a square: "))
    a[p2_i_turn-1] = 'O'
    board = f" {a[0]} | {a[1]} | {a[2]} \n --------- \n {a[3]} | {a[4]} | {a[5]} \n --------- \n {a[6]} | {a[7]} | {a[8]}"
    print(board)



    
    
    



