# My Daily Toolkit - PLP Python Week 8 Final

## What my toolkit does
This is a 3-in-1 command-line toolkit. 1) Number Guessing Game for fun with hints, 2) To-Do List Manager to add/view/remove tasks, 3) Simple Calculator for basic math. All run from one looping menu.

## How to run it
1. Make sure Python 3 is installed
2. Run: `python toolkit.py`
3. Choose 1-4 from menu. Menu loops until you choose 4 to Quit.

## Tools and Concepts Covered
- Looping: while loop in main menu and guessing game, for loop to show tasks
- List that changes: tasks list in To-Do manager with append() and pop()
- Conditionals: if/elif/else for menu choice, guess high/low, calculator ops
- F-strings: all user messages use f-strings for clarity

## Reflection (5-8 sentences)
The hardest part was Part B making the menu loop return after each tool without crashing. At first my program exited after one tool. I fixed it by putting the menu inside a while True loop and using break only for Quit. The longest bug was ValueError when user typed letters instead of numbers in the guessing game - it crashed. I fixed it with try/except. I learned how to combine all concepts together instead of separate files. With one more week I would add file saving for the to-do list so tasks save to tasks.txt and add a fourth tool like countdown timer with time module.
