# Sudoku Solver

This project is a fully interactive Sudoku solver written in Python using pygame, with a dynamic graphical interface and a recursive backtracking algorithm. It’s designed both as a functional puzzle app and a learning tool — ideal for beginners (like me when I started) trying to grasp the tricky logic behind recursion and algorithmic problem solving.

It includes:
- Real-time animated solving
- Custom puzzle input
- A extra folder with the same scripts but beginner-friendly with deep in-line explanations
- A bonus walkthrough on how recursion + backtracking works (because that part was hard to learn for myself)

---

## Learning Context

Created in May 2025 — this was my most challenging and rewarding Python project so far. It helped me cross the bridge between beginner syntax and algorithmic problem solving.

---

## Project Structure

Sudoku_solver/
├──src
   ├── main.py             # Main script for the GUI and program logic
   ├── solver.py           # Backtracking and recursion logic for solving the Sudoku
   └──puzzles.py          # Example Sudoku board
├──Tutorial version with comments
   ├── main_tutorial.py             # Main script with plenty of comments in order to understand every single line
   ├── solver_tutorial.py           # Backtracking and recursion logic for solving the Sudoku with plenty of comments
   ├── puzzles_tutorial.py          # Example Sudoku board
   └── Explanations.md           # Markdown to explain Bakctracking and Recursivity, and how I implement it in the code
└── README.md           # Project documentation


---

## How to Run the Program

1. **Install Dependencies**:
   - Ensure you have Python installed on your machine.
   - Install the required libraries using the following command:
     ```
     pip install pygame
     ```

2. **Run the main Program**:
     ```
     python [main.py]
     ```

---

## Features

- Example board ready to solve.
- Custom puzzle input — click "Customize" and type your own board.
- Reset to default board.
- Animated solving process using recursion and backtracking.
- Interactive UI — highlight cells, see visual number placements and backtracking in real-time.
- For learners trying to understand backtracking and recursivity, a fully commented code version, with every line explained.

---

## Tools and Strategies Used

- pygame: Built the GUI grid, buttons, and animations
- Backtracking + recursion: Core solving logic with detailed explanation
- Validation logic: Checks for valid number placement by row, column, and box
- Real-time rendering: Animates each number placement and backtrack visually
- Custom board logic: Tracks user input separately to preserve UI state

---

## Challenges Encountered and Solutions

### Challenge 1: Understanding Recursion and Backtracking
I hit a wall understanding how recursion and backtracking solve Sudoku — especially how the call stack unwinds. To overcome it, I annotated every line in solver_tutorial.py and main_tutorial.py, and wrote a walkthrough in Recursion_Explained.md to help others too.

### Challenge 2: Building a Responsive UI
Creating a live GUI that doesn't freeze during the solving process was tricky. I used pygame.time.delay() with step-by-step updates to show each move, without blocking the app.

### Challenge 3: Preventing Conflicts Between User Input and Solver
I needed a way to let users enter their own puzzles while keeping track of the default board. I used a temp_board to track changes and restored the original board for solving.

### Challenge 4: Logic Duplication + UI Bugs
The "Solve" button logic was duplicated and caused bugs. I isolated solving to a single block and debugged with state flags to ensure the board and flags updated correctly.

---

## What I Learned

- Built confidence with recursive thinking and step-by-step debugging
- Learned to use pygame for GUI grids, buttons, mouse events, and real-time rendering
- Developed an animated algorithm visualizer that teaches others what recursion looks like
- Practiced clean architecture by separating GUI, logic, and data
- Wrote educational code with intentional, thorough comments for learners like me

---

## Want to Understand Recursion and Backtracking?

I struggled to learn how these terms work, so I documented it in:
Recursion_Explained.md — Plain-language breakdown + walkthrough of the algorithm logic inside solver_tutorial.py and main_tutorial.

---

## Conclusion

This project is a great starting point for anyone interested in learning about Sudoku solvers, backtracking, recursivity, and GUI development in Python. The detailed comments and beginner-friendly design make it accessible to learners, while the dynamic visualization and interactive features make it engaging and fun to use. My goal was not just to make things work, but to understand and explain them clearly to anyone that struggled like I did.

Thank you for reading, this is the kind of project that taught me what real problem-solving feels like in code!