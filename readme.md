# Hangman Game

```
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    
```

A classic Hangman word-guessing game built with Python. Guess letters one at a time to reveal the hidden word before the man is hanged!

---

## Hangman Stages

The hangman is drawn progressively with each wrong guess — 6 lives, 6 stages:

```
  +---+       +---+       +---+       +---+       +---+       +---+       +---+
  |   |       |   |       |   |       |   |       |   |       |   |       |   |
  O   |       O   |       O   |       O   |       O   |       O   |           |
 /|\  |      /|\  |      /|\  |      /|   |       |   |           |           |
 / \  |      /    |           |           |           |           |           |
      |           |           |           |           |           |           |
=========   =========   =========   =========   =========   =========   =========
 0 lives     1 life      2 lives     3 lives     4 lives     5 lives     6 lives
  LOSE                                                                     START
```

---

## How It Works

- A random word is selected from the word list
- The word is displayed as blanks ( `_` ) for each letter
- Guess one letter at a time
- Wrong guess → lose a life + hangman draws further
- Already guessed letters are tracked so you don't repeat
- Guess the full word before 0 lives → **YOU WIN**
- Run out of lives → **YOU LOSE** and the word is revealed

---

## Project Structure

```
hangman/
├── main.py            # Main game logic
├── hangman_words.py   # Word list
├── hangman_art.py     # ASCII art stages and logo
└── README.md
```

---

## How to Run

1. Clone the repository:
```bash
git clone https://github.com/your-username/hangman.git
cd hangman
```

2. Run the game:
```bash
python main.py
```

No external libraries needed — uses Python's built-in `random` module only.

---

## Gameplay Preview

```
****************************6/6 LIVES LEFT****************************
Word to guess: _ _ _ _ _ _
Guess a letter: a
Word to guess: _ _ _ _ a _
****************************5/6 LIVES LEFT****************************
Guess a letter: e
e is not in the word. You lose a life.

  +---+
  |   |
  O   |
      |
      |
      |
=========

****************************4/6 LIVES LEFT****************************
Word to guess: _ _ _ _ a _
Guess a letter: 
```

---

## Concepts Used

- Python loops and conditionals
- String manipulation
- Lists and membership checks
- `random` module for word selection
- Multi-file Python project structure
- ASCII art for visual feedback

---

## Author

**Muhammed Adhil M J** — B.Tech AI & ML, Vidya Academy of Science and Technology