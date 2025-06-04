'''This code sets up a graphical user interface (GUI) for a sudoku solver using pygame. It creates a window, draws a sudoku grid, and handles
basic event management to keep the application running until quitting the program. It serves as a basic framework and foundation for 
adding further functionality, such as user interaction or solving logic'''

import pygame
import sys
from puzzles_tutorial import get_example_board
from solver_tutorial import solve_gui
from solver_tutorial import is_valid

# Window dimensions
WIDTH = 540 # sets the pixels to 540 as width
HEIGHT = 660 # 540 pixels for the grid + 3 buttons (40px each + spacing)
CELL_SIZE = WIDTH // 9 # It's divisible by 9, to ensure an uniform size of 60x60 pixels

# Colors
WHITE = (255, 255, 255) # We specify the colors, these are defined as RGB tuples
BLACK = (0, 0, 0)
THIN_LINE = 1 # We specify two different thickness of lines
THICK_LINE = 3

# Button dimensions and colors
BUTTON_HEIGHT = 60 # size of the button
BUTTON_COLOR = (50, 150, 255)  # Blue color for the button
BUTTON_HOVER_COLOR = (30, 120, 220)  # Darker blue when hovered
BUTTON_TEXT_COLOR = (255, 255, 255)  # White text color

def main():
    '''Function to create a window with pygame'''
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Specified dimensions using constants and saved into the screen variable (as a tuple)
    pygame.display.set_caption("Sudoku Solver")  # Title
    
    screen.fill(WHITE)  # Sets the white background
    draw_grid(screen)  # Pass the screen variable to draw_grid()
    board = get_example_board()  # Get the Sudoku board
    temp_board = [row[:] for row in board]  # Temporary board for user edits
    original_board =[row[:] for row in board] # Store the original fixed board to determine which numbers are part of the original board and are always valid
    pygame.display.flip()  # Updates the display to show the drawn grid

    # Main loop
    running = True  # Keeps the application running and listens for events like closing the window
    solving = False  # Flag to ensure solving starts only once
    selected = None # Tracks the current selected cell witht he mouse (None because no cell is selected)

    while running:  # Keeps the application running
        for event in pygame.event.get():  # Listens for events
            if event.type == pygame.QUIT:  # If a QUIT event is detected, then the loop exits
                running = False

            # Handle mouse clicks to select cell
            if event.type == pygame.MOUSEBUTTONDOWN: # This event is triggered when the user clicks the mouse
                mouse_x, mouse_y = pygame.mouse.get_pos() # Get the position of the mouse click as (x, y)
                
                if solve_button.collidepoint(mouse_x, mouse_y) and not solving: # If mouse click the solve button before solving...
                    solving = True
                    board = [row[:] for row in temp_board]  # Copy the user-edited board
                    solve_gui(board, screen, draw_func)  # Call solve_gui to solve the Sudoku with animations
                    temp_board = [row[:] for row in board]  # Update temp_board with the solved board
                    solving = False  # Reset the solving flag to reuse the "Solve" button

                elif customize_button.collidepoint(mouse_x, mouse_y): # If mouse click the customize button...
                    temp_board = [[0 for _ in range(9)] for _ in range(9)]  # Clear all cells creating a 9x9 grid filled with 0s

                elif reset_button.collidepoint(mouse_x, mouse_y): # If mouse click the reset button...
                    temp_board = [row[:] for row in original_board]  # Resets the temporal board to the original board
                    selected = None  # Deselect any selected cell

                else:
                    col = mouse_x // CELL_SIZE # Calculation to determine the column of the clicked cell
                    row = mouse_y // CELL_SIZE # Calculation to determine the row of the clicked cell
                    if 0 <= row < 9 and 0 <= col < 9:  # Ensure the click is within the grid
                        selected = tuple([row, col])  # Convert the row and column into a tuple
                    else:
                        selected = None  # Deselect if the click is outside the grid

            # Handle Keyboard Input
            ''' If a cell is selected and the user presses a number 1-9, the number is added to the temp_board at the selected
            cell, if the Backspace key is pressed, the selected cell is cleared by setting its value to 0'''
            if event.type == pygame.KEYDOWN:  # Detects key presses
                if selected and not solving: # Only allow input if a cell is selected and solving hasn't started
                    row, col = selected # Get the selected cell
                    if event.unicode in "123456789": # Check if the key pressed is a number 1-9
                        num = int(event.unicode) # Convert the key to an integer
                        temp_board[row][col] = num # Update the temporary board
                    elif event.key == pygame.K_BACKSPACE: # Check if BACKSPACE is pressed
                        temp_board[row][col] = 0 # Clear de selected cell

                # Start the solver when the SPACE key is pressed
                if event.key == pygame.K_SPACE and not solving:  # If SPACE is pressed and solving hasn't started
                    solving = True  # Set solving flag to True
                    board = [row[:] for row in temp_board]  # Copy the user-edited board
                    solve_gui(board, screen, draw_func)  # Call solve_gui to solve the Sudoku with animations                  
        
        # Update the screen dynamically after every user interaction
        screen.fill(WHITE) # Clear the screen
        draw_grid(screen) # Redraw the grid
        draw_numbers(screen, temp_board, original_board, selected) # Draw the updated numbers, passes parameters, and highlight the selected cell
        solve_button = draw_button(screen, "Solve", 270) # Draw the "Solve" button, centered horizontally, plus we pass the x center coordinates to the function
        customize_button = draw_button(screen, "Customize", 90)  # Draw the "Clear" button, Left-aligned
        reset_button = draw_button(screen, "Reset", 450)  # Draw the "Reset" button, Right-aligned
        pygame.display.flip() # Update the display

    pygame.quit()  # If the loop exits, we terminate the program with these two functions
    sys.exit()

def draw_grid(screen):
    '''Function to render the grid, we draw 10 lines horizontally and 10 lines vertically (9 cells = 10 lines)'''
    for i in range(10): # 0 through 9 lines (including boundary)
        line_width = THICK_LINE if i % 3 == 0 else THIN_LINE # Every third line is drawn thicker to visually separate the 3x3 subgrids
        # Horizontal line
        pygame.draw.line(screen, BLACK, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), line_width) # Draw the lines in the screen
        # Vertical line
        pygame.draw.line(screen, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, 540), line_width) # Ensuring the grid is evenly spaced and visually clear

def draw_numbers(screen, board, original_board, selected=None):
    '''Function to render the numbers from a sudoku board onto the screen using pygame'''
    pygame.font.init() # We initialize the Pygame font module
    font = pygame.font.Font(None, 40) # We create a font, None = default font, 40 = size

    for i in range(9): # Rows
        for j in range(9): # Columns
            num = board[i][j] # For each cell it retrieves the value num at board[i][j]
            if num!= 0: # If the cell is not empty we create a Pygame surface with font.render() containing the rendered text
                # We add a check to ensure that original_board is a 2D list before accessing its elements
                if isinstance(original_board, list) and all(isinstance(row, list) for row in original_board):
                    color = (0, 0, 0)  # All numbers are black
                else:
                    raise ValueError("original_board is not a valid 2D list")
                
                # Render the number with the appropiate color
                text = font.render(str(num), True, color) # True = smoother text and choose appropiate color
                x = j * CELL_SIZE + CELL_SIZE // 2 - text.get_width() // 2 # We center the number in its cell by adjusting its position
                y = i * CELL_SIZE + CELL_SIZE // 2 - text.get_height() // 2 # We calculate x and y to center the numbers
                screen.blit(text, (x, y)) # We blit (draw) the number onto the screen in the position of x and y
    
    # Make it so if a cell is selected, highlight it drawing a red rectangle around the selected cell
    if selected and isinstance(selected, tuple) and len(selected) == 2: # Make sure selected is a tuple and not Nonw before unpack
        row, col = selected
        pygame.draw.rect(screen, (255, 0, 0), (
            col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE
        ), 3) # Draw a red rectangle

def draw_func(screen, board, pos, num, action):
    '''Function to visually update a single cell during the solving process, also ensuring that the grid remains visually consistent'''
    x = pos[1] * CELL_SIZE  # Calculate the x-coordinate of the cell
    y = pos[0] * CELL_SIZE  # Calculate the y-coordinate of the cell

    font = pygame.font.Font(None, 40)  # Create a font object with the default font and size 40

    # Erase the cell by drawing a white rectangle over it, slightly smaller than the cell size
    pygame.draw.rect(screen, WHITE, (x + 1, y + 1, CELL_SIZE - 2, CELL_SIZE - 2))

    # If the number is not 0, render it with the appropriate color, "place" = blue, anything else (like "remove") = red
    if num != 0:
        color = (0, 0, 255) if action == "place" else (200, 0, 0)  # Blue for placing, red for removing
        text = font.render(str(num), True, color)  # Generates a surface containing the rendered number
        screen.blit(text, ( # We blit (draw) the number in the center of the cell
            x + CELL_SIZE // 2 - text.get_width() // 2,  # Center the number horizontally
            y + CELL_SIZE // 2 - text.get_height() // 2  # Center the number vertically
        ))

    # Redraw only the affected cell's grid lines, to avoid redawing all the gird over again and ensuring the visual integrity of the board
    # It draws vertical and horizontal lines using pygame.draw.line, ensuring that only the lines surrounding the updated cell are redrawn
    # This approach minimizes unnecessary rendering and improves performance
    pygame.draw.line(screen, BLACK, (x, 0), (x, HEIGHT), THIN_LINE)  # Vertical line
    pygame.draw.line(screen, BLACK, (x + CELL_SIZE, 0), (x + CELL_SIZE, HEIGHT), THIN_LINE)  # Next vertical line
    pygame.draw.line(screen, BLACK, (0, y), (WIDTH, y), THIN_LINE)  # Horizontal line
    pygame.draw.line(screen, BLACK, (0, y + CELL_SIZE), (WIDTH, y + CELL_SIZE), THIN_LINE)  # Next horizontal line

def draw_button(screen, text, center_x, y_offset=545):
    '''Function to draw a button with hover effects and flexible positioning'''
    font = pygame.font.Font(None, 36) # Create a font object
    text_surface = font.render(text, True, BUTTON_TEXT_COLOR) # Render the button text
    button_rect = pygame.Rect(center_x - 90, y_offset, 180, 40) # Define the button's rectangle position and size

    # Check if the mouse is hovering over the button
    mouse_pos = pygame.mouse.get_pos() # Gives a (x, y) position
    if button_rect.collidepoint(mouse_pos): # If the mouse is over the button
        color = BUTTON_HOVER_COLOR # Use the hover color
    else:
        color = BUTTON_COLOR # Use the default color if not hovering over the button
    
    # Draw the button rectangle
    pygame.draw.rect(screen, color, button_rect, border_radius=6)

    # Draw the button text centered within the button
    screen.blit(
        text_surface,
        (button_rect.centerx - text_surface.get_width() // 2,
         button_rect.centery - text_surface.get_height() // 2)
    )
    return button_rect # Return the button's rectangle for click detection


if __name__=="__main__":
    main()