import pygame
import sys
from puzzles import get_example_board
from solver import solve_gui, is_valid

# Window dimensions
WIDTH = 540
HEIGHT = 660
CELL_SIZE = WIDTH // 9

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
THIN_LINE = 1
THICK_LINE = 3

# Button dimensions and colors
BUTTON_HEIGHT = 60
BUTTON_COLOR = (50, 150, 255)
BUTTON_HOVER_COLOR = (30, 120, 220)
BUTTON_TEXT_COLOR = (255, 255, 255)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku Solver")
    
    screen.fill(WHITE)
    draw_grid(screen)
    board = get_example_board()
    temp_board = [row[:] for row in board]
    original_board = [row[:] for row in board]
    pygame.display.flip()

    running = True
    solving = False
    selected = None

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                
                if solve_button.collidepoint(mouse_x, mouse_y) and not solving:
                    solving = True
                    board = [row[:] for row in temp_board]
                    solve_gui(board, screen, draw_func)
                    temp_board = [row[:] for row in board]
                    solving = False

                elif customize_button.collidepoint(mouse_x, mouse_y):
                    temp_board = [[0 for _ in range(9)] for _ in range(9)]

                elif reset_button.collidepoint(mouse_x, mouse_y):
                    temp_board = [row[:] for row in original_board]
                    selected = None

                else:
                    col = mouse_x // CELL_SIZE
                    row = mouse_y // CELL_SIZE
                    if 0 <= row < 9 and 0 <= col < 9:
                        selected = tuple([row, col])
                    else:
                        selected = None

            if event.type == pygame.KEYDOWN:
                if selected and not solving:
                    row, col = selected
                    if event.unicode in "123456789":
                        num = int(event.unicode)
                        temp_board[row][col] = num
                    elif event.key == pygame.K_BACKSPACE:
                        temp_board[row][col] = 0

                if event.key == pygame.K_SPACE and not solving:
                    solving = True
                    board = [row[:] for row in temp_board]
                    solve_gui(board, screen, draw_func)
                    temp_board = [row[:] for row in board]
                    solving = False
        
        screen.fill(WHITE)
        draw_grid(screen)
        draw_numbers(screen, temp_board, original_board, selected)
        solve_button = draw_button(screen, "Solve", 270)
        customize_button = draw_button(screen, "Customize", 90)
        reset_button = draw_button(screen, "Reset", 450)
        pygame.display.flip()

    pygame.quit()
    sys.exit()

def draw_grid(screen):
    for i in range(10):
        line_width = THICK_LINE if i % 3 == 0 else THIN_LINE
        pygame.draw.line(screen, BLACK, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), line_width)
        pygame.draw.line(screen, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, 540), line_width)

def draw_numbers(screen, board, original_board, selected=None):
    pygame.font.init()
    font = pygame.font.Font(None, 40)
    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num != 0:
                if isinstance(original_board, list) and all(isinstance(row, list) for row in original_board):
                    color = (0, 0, 0)
                else:
                    raise ValueError("original_board is not a valid 2D list")
                text = font.render(str(num), True, color)
                x = j * CELL_SIZE + CELL_SIZE // 2 - text.get_width() // 2
                y = i * CELL_SIZE + CELL_SIZE // 2 - text.get_height() // 2
                screen.blit(text, (x, y))
    if selected and isinstance(selected, tuple) and len(selected) == 2:
        row, col = selected
        pygame.draw.rect(screen, (255, 0, 0), (
            col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE
        ), 3)

def draw_func(screen, board, pos, num, action):
    x = pos[1] * CELL_SIZE
    y = pos[0] * CELL_SIZE
    font = pygame.font.Font(None, 40)
    pygame.draw.rect(screen, WHITE, (x + 1, y + 1, CELL_SIZE - 2, CELL_SIZE - 2))
    if num != 0:
        color = (0, 0, 255) if action == "place" else (200, 0, 0)
        text = font.render(str(num), True, color)
        screen.blit(text, (
            x + CELL_SIZE // 2 - text.get_width() // 2,
            y + CELL_SIZE // 2 - text.get_height() // 2
        ))
    pygame.draw.line(screen, BLACK, (x, 0), (x, HEIGHT), THIN_LINE)
    pygame.draw.line(screen, BLACK, (x + CELL_SIZE, 0), (x + CELL_SIZE, HEIGHT), THIN_LINE)
    pygame.draw.line(screen, BLACK, (0, y), (WIDTH, y), THIN_LINE)
    pygame.draw.line(screen, BLACK, (0, y + CELL_SIZE), (WIDTH, y + CELL_SIZE), THIN_LINE)

def draw_button(screen, text, center_x, y_offset=545):
    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, BUTTON_TEXT_COLOR)
    button_rect = pygame.Rect(center_x - 90, y_offset, 180, 40)
    mouse_pos = pygame.mouse.get_pos()
    color = BUTTON_HOVER_COLOR if button_rect.collidepoint(mouse_pos) else BUTTON_COLOR
    pygame.draw.rect(screen, color, button_rect, border_radius=6)
    screen.blit(
        text_surface,
        (button_rect.centerx - text_surface.get_width() // 2,
         button_rect.centery - text_surface.get_height() // 2)
    )
    return button_rect

if __name__ == "__main__":
    main()