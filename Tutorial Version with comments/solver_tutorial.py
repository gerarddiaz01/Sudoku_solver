'''This code is to set the backtracking logic and check valid moves'''
import pygame
import time

def is_valid(board, num, pos):
    '''We validate sudoku rules, checking for the same number in rows and columns, then inside the 3x3 box'''
    # Row
    for i in range(len(board[0])): # We iterate all columns in a specific row
        if board[pos[0]][i] == num and pos[1] != i: # We check for duplicates of num (if row 0 from [0,0] to [0,8]), ignoring current position
            return False # If duplicates are found return that num is wrong
        
    # Column
    for i in range(len(board)): # We iterate all rows of a specific column
        if board[i][pos[1]] == num and pos[0] != i: # We check for duplicates of num (if column 1 from [0,1] to [8,1]), ignoring current position
            return False # If duplicates are found return that num is wrong
        
    # 3x3 Box: it ensures that the number does not already exist within the 3x3 box, we identify the box and check that the num is not there
    box_x = pos[1] // 3 # We divide row and column by 3 (because 3x3) using the integer division //
    box_y = pos[0] // 3 # Rows are the y axis and the row index is pos[0], Columns are the X axis and the column index is pos[1], (board[row][column])
    for i in range(box_y*3, box_y*3 + 3): # The range for each loop is calculated by multiplying box_y and box_x by 3 to get the starting row...
        for j in range(box_x*3, box_x*3 + 3): # ...and column of the box, and adding 3 to include all rows and columns within the box
            if board[i][j] == num and (i, j) != pos: # We check if current cell is the same number as num, if it is then wrong number
                return False
    return True

def find_empty(board):
    '''We look for empty cells, if none are found then the sudoku is solved'''
    for i in range(len(board)): # len(board) = number of rows
        for j in range(len(board[0])): # len(board[0]) number of columns of each row
            if board[i][j] == 0: 
                return (i, j) # If a position is found being empty (0) then return the position as a tuple
    return None # If no empty cells are found then the sudoku is solved, used to terminate the backtracking process

def solve_gui(board, screen, draw_func):
    '''Function with the logic of backtracking and recursivity to solve the sudoku applying the rules to validate a number inside a cell.
       It includes animations to visually display the solving process.'''
    # Step 1: Find an empty cell
    find = find_empty(board)  # You get a tuple with the position [row][column]
    if not find:  # If no empty cells, the board is solved
        return True  # If it's the case, the backtracking and recursivity stop
    row, col = find

    # Step 2: Try numbers 1-9, attempt to place each number in an empty cell
    for num in range(1, 10):  # For each number, it calls is_valid() to check if placing the number in this position violates Sudoku rules
        if is_valid(board, num, (row, col)):
            board[row][col] = num  # If the number is valid, we temporarily place the number in the cell and go to the next step

            # Animation Step: Visually display the placement of the number
            draw_func(screen, board, (row, col), num, "place")  # Call the draw function to render the number
            pygame.display.update()  # Update the display to show the changes
            pygame.time.delay(40)  # Add a small delay to create an animation effect

            # Step 3: Recursively solve the rest of the board, attempting to solve the rest of the board with the current placement
            if solve_gui(board, screen, draw_func):  # Base Case: If using this placement, the rest of the board is solved (no empty cells found), then return True and the board is solved
                return True  # This propagates the success up the recursion stack and ends the backtracking process, exit function and board is solved
            
            # Step 4: Backtrack if placing the number didn't work (previous step is False), set the cell to 0 and go to the next empty cell
            board[row][col] = 0  # Undo the placement by resetting the cell to 0

            # Animation Step: Visually display the removal of the number (backtracking)
            draw_func(screen, board, (row, col), 0, "remove")  # Call the draw function to visually show the backtracking
            pygame.display.update()  # Update the display to show the changes
            pygame.time.delay(40)  # Add a small delay to create an animation effect

    # Step 5: If none of the numbers 1-9 can be placed in the current empty cell without violating Sudoku rules, then it triggers backtracking
    return False  # This activates the backtracking, to systematically explore all possibilities by undoing invalid placements and trying 
                  # alternatives
                  # If return False propagates all the way to the top of the recursion stack (the very first call to solve_gui()), it means
                  # that no valid solution exists for the given Sudoku puzzle. In this case, the function returns False to indicate that the 
                  # puzzle is unsolvable
