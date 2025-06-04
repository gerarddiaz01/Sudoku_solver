# Let's break down the context of recursion and backtracking using this project as reference

This document explains the concepts of recursion and backtracking using this Sudoku solver project as a practical reference. These terms can feel abstract — but when applied step-by-step, they become intuitive.

We’ll explore:
- What recursion is and how it works
- What backtracking means and why it’s powerful
- How these two combine to solve Sudoku
- A full walkthrough of how the script flows, using actual code line references from solver_tutorial.py and main_tutorial.py

## Recursion

**Recursion** is when a function calls itself to solve a smaller instance of the same problem. In the context of this Sudoku solver, recursion is used to try filling the board one cell at a time, calling the same function (`solve_gui`) to attempt to solve the rest of the board after each placement.

Think of it like this:
"To solve this puzzle, I’ll try something, and if it doesn’t work, I’ll go back and try a different option — using the same method again and again."

**In the code:**  
- See `solve_gui` in `solver_tutorial.py` (lines 34–70).
- After placing a number in an empty cell, the function calls itself:  
  ```python
  if solve_gui(board, screen, draw_func):
      return True
This means: "If placing this number leads to a solution for the rest of the board, we're done!"

**Why use recursion here?**
Recursion allows us to break down the big problem ("solve the whole board") into smaller problems ("solve the rest of the board after this move"), until we reach a base case (no empty cells left).


## Backtracking
**Backtracking** is a strategy for finding solutions by trying out possible options and undoing ("backtracking") them if they lead to a dead end. In Sudoku, if a number placement leads to a contradiction later, we remove it and try the next possible number.

**In the code:**  
- Still in `solve_gui` in `solver_tutorial.py` (see line 66).
  ```python
  board[row][col] = 0
If none of the numbers 1–9 work for a cell, the function returns False (line 60), which triggers backtracking in the previous recursive call.

**Why use backtracking here?**
Sudoku is a constraint satisfaction problem. Backtracking lets us systematically explore all possible number placements, undoing choices that don't work, until we find a valid solution or exhaust all options.


## How Recursion and Backtracking Work Together in This Project
1. Find an empty cell (find_empty, lines 18–25 in solver_tutorial.py).
2. Try numbers 1–9 in that cell.
3. For each number:
    - Check if it's valid (is_valid, lines 5–17).
    - If valid, place the number and recursively try to solve the rest of the board.
    - If the recursive call returns False, remove the number (backtrack) and try the next one.
4. If all numbers fail, return False to backtrack further.
This combination is a classic and efficient way to solve puzzles like Sudoku.


## Why This Approach?
- Recursion simplifies the logic: each call is responsible for solving a smaller part of the puzzle.
- Backtracking ensures we don't get stuck: if a choice leads to a dead end, we undo it and try something else.
- This combination is a classic and efficient way to solve puzzles like Sudoku.


## Script Flow Walkthrough
Let's clarify how the main components interact:

1. Program starts (main_tutorial.py, main() function):
Initializes the GUI and loads the example board.
Sets up the main event loop.

2. User Interaction:
User can select cells, input numbers, and click buttons ("Solve", "Customize", "Reset").
All changes are made to temp_board, which represents the current state of the board.

3. Solving the Puzzle:
When "Solve" is clicked, solve_gui is called with a copy of the current board.
solve_gui uses recursion and backtracking to fill the board, updating the GUI at each step for visualization.

4. Key Functions:
- is_valid(board, num, pos): Checks if a number can be placed at a given position.
- find_empty(board): Finds the next empty cell.
- solve_gui(board, screen, draw_func): The recursive backtracking solver with GUI updates.
- draw_func(screen, board, pos, num, action): Handles the animation of placing/removing numbers during solving.

5. Event Loop:
Handles user input (mouse and keyboard).
Redraws the grid and numbers after every interaction.

6. Board State:
- original_board: The starting puzzle (unchanged).
- temp_board: The current board (user edits and solving).
After solving, temp_board is updated with the solution.


## Example: Step-by-Step
**Suppose you click "Solve"**
1. The program copies your current board and calls solve_gui.
2. solve_gui finds the first empty cell.
3. It tries numbers 1–9 in that cell, checking validity.
4. For each valid number, it places it and recursively tries to solve the rest.
5. If a dead end is reached, it removes the number (backtracks) and tries the next.
6. This continues until the board is solved or all options are exhausted.
You’ll see this happening live in the GUI: each number placement and removal is drawn in real time.


## Final Thoughts for Beginners

I created this walkthrough because recursion was difficult for me at first — I often felt lost in the logic.
So I broke it into:
🔹 Find a base case (is the puzzle solved?)
🔹 Try every possible number
🔹 Validate it
🔹 Recurse to the next cell
🔹 If it fails, go back

That’s it. It may look complex in code, but it’s just smart trial-and-error — with memory.

Hope this helped you see recursion + backtracking in action!