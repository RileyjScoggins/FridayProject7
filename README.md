# FridayProject7
# Python Interactive Projects Collection

This repository contains six beginner-friendly interactive Python projects that help you practice fundamental concepts such as conditionals, loops, functions, and user input. Each project is designed to be simple, fun, and educational.

---

## Table of Contents
1. [Mad Lib Game](#mad-lib-game)
2. [PowerBall Number Generator](#powerball-number-generator)
3. [Number Guessing Game](#number-guessing-game)
4. [Trivia Game](#trivia-game)
5. [Text Color Changer](#text-color-changer)
6. [Bank Account Manager](#bank-account-manager)

---

## 1. Mad Lib Game
### Overview
The Mad Lib Game lets users create a funny story by filling in blank spaces with their own words. The program prompts the user for different types of words (like nouns, verbs, and adjectives) and inserts them into a predefined story template.

### Key Features
- Uses user input to create a personalized story.
- Simple prompts for different parts of speech (noun, verb, etc.).
- Displays the completed story with the user's inputs.

### Instructions
1. Run the script.
2. Follow the prompts to enter words as specified (e.g., noun, verb).
3. Enjoy the final humorous story with your chosen words!

---

## 2. PowerBall Number Generator
### Overview
This program simulates generating random PowerBall lottery numbers. It picks five random white ball numbers (from 1 to 69) and one red PowerBall number (from 1 to 26).

### Key Features
- Uses `random.randint()` to generate random numbers.
- Displays PowerBall numbers with appropriate spacing between numbers.
- Greets and thanks the user for participating.

### Instructions
1. Run the program.
2. The script will automatically generate and display PowerBall numbers.

---

## 3. Number Guessing Game
### Overview
This is a guessing game where the computer randomly selects a number between 1 and 10. The user tries to guess the number, receiving hints if their guess is too high or too low, until they guess correctly.

### Key Features
- Generates a random number using `random.randint()`.
- Provides feedback to guide the user in guessing.
- Displays a congratulatory message once the user guesses the correct number.

### Instructions
1. Run the program.
2. Guess the number based on feedback, and continue until you guess correctly.

---

## 4. Trivia Game
### Overview
The Trivia Game displays a series of trivia questions stored in a dictionary. The user provides answers, and the program provides feedback on whether each answer is correct or incorrect.

### Key Features
- Uses a dictionary to store questions and answers.
- Loops through questions, providing immediate feedback after each answer.
- Encourages users to test their knowledge on various trivia questions.

### Instructions
1. Run thprogram.
2. Answer each trivia question and receive immediate feedback on your answer.

---

## 5. Text Color Changer
### Overview
The Text Color Changer allows users to display text in different colors on the console. Each color is represented by a specific function that formats text using ANSI escape codes.

### Key Features
- Defines five functions to display text in different colors.
- Allows users to input custom text and choose a color.
- Optional random color feature to apply a random color to the text.

### Instructions
1. Run the script.
2. Choose a color (red, blue, green, yellow, purple) and enter text to display in that color.
3. Experiment with different colors or use the random color option for variety.

---

## 6. Bank Account Manager
### Overview
The Bank Account Manager simulates a simple banking application where users can deposit, withdraw, and check their account balance. Users enter their account number to access account options.

### Key Features
- A `BankAccount` class with methods to deposit, withdraw, and check the balance.
- Verification by asking for the account number before allowing transactions.
- Continuous loop to perform multiple actions until the user chooses to exit.

### Instructions
1. Run the program.
2. Enter the account number and select an action (deposit, withdraw, check balance, or exit).
3. Continue managing your account balance until you exit the program.

---

## Requirements
- Python 3.x
- A terminal or IDE that supports ANSI color codes (for the Text Color Changer project).

## Running the Programs
Clone this repository, navigate to the project directory, and run each script with:
```bash
python project_name.py
