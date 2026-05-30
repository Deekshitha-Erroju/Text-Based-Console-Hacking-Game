# 🎮 CYBERSTRIKE - Hacking Simulation Game

CYBERSTRIKE is a Python console-based game that simulates hacking missions through password-cracking challenges. Players must register, log in, and complete various missions by correctly guessing passwords using progressively revealed hints. The game rewards successful hacks with points and tracks the player's score throughout the session.

## Features

- User Registration and Login System
- Password-based Hacking Missions
- Progressive Hint System
- Limited Lives for Each Mission
- Score Tracking
- File Handling for User Data Storage
- Exception Handling for Better User Experience
- Interactive Console Interface

## Technologies Used

- Python 3
- File Handling
- Functions
- Loops
- Conditional Statements
- Exception Handling
- Time Module

## Missions

| Mission | Description | Points |
|----------|------------|---------|
| Hack PC System | Crack a simple system password | 100 |
| Hack Bank Server | Crack a secure banking server password | 150 |
| Hack Private Organization | Crack a high-security organization password | 200 |

## Project Structure

```
CYBERSTRIKE/
│
├── cyberstrike.py
├── users.txt
└── README.md
```

## How to Run

1. Install Python 3.
2. Download or clone this repository.
3. Open a terminal in the project directory.
4. Run the program using:

```bash
python cyberstrike.py
```

## How to Play

### Step 1: Register
Create a new account with a username and password.

### Step 2: Login
Login using your registered credentials.

### Step 3: Select a Mission
Choose from:
- Hack PC
- Hack Bank
- Hack Organization

### Step 4: Guess the Password
- You start with 5 lives.
- A password hint is displayed.
- Each incorrect attempt reveals one additional character.
- Guess the password before running out of lives.

### Step 5: Earn Points
Successful mission completion awards points based on difficulty.

### Step 6: Check Your Score
Use the "Check Score" option from the menu to view your total score.

## Concepts Demonstrated

- Functions and Modular Programming
- File Handling (Read/Write Operations)
- User Authentication
- String Manipulation
- Loops and Conditional Statements
- Exception Handling
- Menu-Driven Applications

## Sample Output

```text
====== WELCOME TO CYBERSTRIKE ======

1. Register
2. Login
3. Exit

Enter Choice: 2

LOGIN SUCCESSFUL!

========== CYBERSTRIKE ==========
1. Hack PC
2. Hack Bank
3. Hack Organization
4. Check Score
5. Exit
=================================
```

## Future Enhancements

- Encrypted Password Storage
- Persistent Score Saving
- Global Leaderboard
- Additional Missions
- Difficulty Levels
- Graphical User Interface (GUI)
- Multiplayer Support

## Educational Purpose

This project was developed as a Python mini-project to practice:
- File Handling
- Functions
- Exception Handling
- Loops
- User Authentication
- Menu-Driven Programming

## License

This project is intended for educational and learning purposes only.