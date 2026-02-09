# 🔢 Number Guessing Game — Python CLI Project

A simple and fun **Number Guessing Game** built using Python.
The computer randomly selects a number between **1 and 100**, and the player keeps guessing until the correct number is found.

This is a great beginner project to practice loops, condition handling, exceptions, and user input validation.

---

## 🎮 Game Description

* The program generates a random number between **1 and 100**
* The player guesses the number
* The program gives hints:

  * **Too high**
  * **Too low**
* The game continues until the correct guess
* Shows total number of attempts taken
* Handles invalid (non-numeric) input safely

---

## 🚀 Features

* Random number generation
* Infinite loop until correct guess
* Attempt counter
* Error handling using `try/except`
* User-friendly hint messages
* Clean command-line interaction

---

## 🧠 Concepts Used

* `random.randint()`
* While loops
* If–elif–else logic
* Exception handling (`ValueError`)
* Type conversion (`int`)
* Counters and variables

---

## ▶️ How to Run

1. Make sure Python is installed
2. Save the file as:

```
number_guessing_game.py
```

3. Run from terminal:

```
python number_guessing_game.py
```

---

## 🎯 How to Play

* Enter a number between **1 and 100**
* Follow the hints printed by the program
* Keep guessing until you win
* The game displays how many tries you used

---

## 💻 Example Output

```
Guess The number between 1 to 100: 50
Too low!
Guess The number between 1 to 100: 75
Too high!
Guess The number between 1 to 100: 63
Congratulation! You guessed the number in 3 tries.
```

---

## 👨‍💻 Author

Built as a beginner-friendly Python practice project.

---

## 📄 License

Free for learning and educational use.
