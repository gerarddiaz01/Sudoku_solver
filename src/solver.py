import pygame
import time

def is_valid(board, num, pos):
    """Check if num can be placed at pos without violating Sudoku rules."""
    # Row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
    # Column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    # 3x3 Box
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False
    return True

def find_empty(board):
    """Return the position of the first empty cell, or None if full."""
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None

def solve_gui(board, screen, draw_func):
    """Solve the Sudoku board using backtracking, with GUI updates."""
    find = find_empty(board)
    if not find:
        return True
    row, col = find

    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num
            draw_func(screen, board, (row, col), num, "place")
            pygame.display.update()
            pygame.time.delay(40)

            if solve_gui(board, screen, draw_func):
                return True

            board[row][col] = 0
            draw_func(screen, board, (row, col), 0, "remove")
            pygame.display.update()
            pygame.time.delay(40)
    return False