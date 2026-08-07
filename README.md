# voting_eligibility_checker
A beginner-friendly Python program that checks voting eligibility based on age and voter ID availability. It demonstrates nested if statements, conditional logic, user input, and decision-making in Python.
# Python Voting Eligibility Checker

## 📌 Overview

The **Python Voting Eligibility Checker** is a beginner-friendly Python program that determines whether a person is eligible to vote based on their age and whether they possess a valid voter ID.

This project helps beginners understand conditional statements and nested decision-making in Python.

## ✨ Features

- Accepts user age
- Checks voting eligibility
- Verifies voter ID availability
- Uses nested `if` statements
- Displays appropriate messages

## 🛠️ Concepts Practiced

- User Input (`input()`)
- Variables
- Type Conversion (`int()`)
- Conditional Statements (`if`, `else`)
- Nested `if` Statements
- String Methods (`lower()`)
- Decision Making

## 💻 Source Code

```python
age = int(input("Enter your age: "))

if age >= 18:
    voter_id = input("Do you have a Voter ID? (Y/N): ").lower()

    if voter_id == "y":
        print("You are eligible to vote.")
    else:
        print("Please apply for a Voter ID.")
else:
    print("You are not eligible to vote.")
```

## ▶️ Example

### Input

```
Enter your age: 20
Do you have a Voter ID? (Y/N): y
```

### Output

```
You are eligible to vote.
```

### Input

```
Enter your age: 20
Do you have a Voter ID? (Y/N): n
```

### Output

```
Please apply for a Voter ID.
```

### Input

```
Enter your age: 16
```

### Output

```
You are not eligible to vote.
```

## 📂 Project Structure

```
Python-Voting-Eligibility-Checker/
├── voting_eligibility_checker.py
└── README.md
```

## 🎯 Learning Objectives

- Learn conditional statements
- Understand nested `if` statements
- Practice user input handling
- Build logical decision-making skills
- Improve problem-solving using Python

## 🚀 Future Improvements

- Validate age input
- Accept multiple users
- Add age verification messages
- Store voter details in a file
- Create a graphical user interface (GUI)

---

⭐ **Part of my Python learning journey and beginner programming practice.**
