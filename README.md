# cse210-tc06-mastermind
=======
# Mastermind
Mastermind is a game in which each player seeks to guess the secret code 
they've been assigned before the other players do.

#Rules
Mastermind is played according to the following rules.

The code is a randomly generated, four digit number between 1000 and 9999.
The players take turns registering themselves by entering their name.
The players take turns guessing the secret code based on the hint that is offered. An x means a correct number in a correct position. An o means a correct number in an incorrect position. An * means an incorrect number (see interface section).
If the guess is correct, the current player wins and the game is over.
If the guess is incorrect, a new hint is generated and play continues.

## Getting Started
---
Make sure you have Python 3.8.0 or newer installed and running on your machine. 
Open a terminal and browse to the project's root folder. Start the program by 
running the following command.
```
python3 mastermind 
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE 
and open the project folder. Select the main module inside the hunter folder and 
click the "run" icon.

## Project Structure
---
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- mastermind          (source code for game)
  +-- game              (specific game classes)
    +-- __init__.py     (python package file)
    +-- board.py        (Class to setup the board)
    +-- comparison.py   (Class to control items for game loop)
    +-- console.py      (Class to control input and output)
    +-- director.py     (Class to control the game)
    +-- player.py       (Class to control player items)
    +-- roster.py       (Class to control players turns)
  +-- __init__.py       (python package file)
  +-- __main__.py       (entry point for program)
+-- README.md           (general info)
```

## Required Technologies
---
* Python 3.8.0

## Authors
---
* Ezequiel Iannone
* Caio Andrade
* Kevin Augusto
* Celeste Popoca