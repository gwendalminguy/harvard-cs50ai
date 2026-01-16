# Tic-Tac-Toe

This program implements a small AI able to play the well known [Tic-Tac-Toe](https://en.wikipedia.org/wiki/Tic-tac-toe) game.

## Understanding

The program works by using an implementation of the [MiniMax](https://en.wikipedia.org/wiki/Minimax) algorithm. This basically means that, for each move made by the player, the program computes the best move available according to the given state (which is the current board of the game), by minimizing the possible loss for the worst case scenario.

## Files

This project contains the following files:

| Element | Description |
| :---- | :---------- |
| `OpenSans-Regular.ttf` | The font file to be used by the game. |
| `requirements.txt` | The text file listing requirements for installation. |
| `runner.py` | The python script to run the game. |
| `tictactoe.py` | The python file containing the function implementations for the AI. |

## Installation

In order to play the game, a small installation needs to be made, by creating a virtual environment, activating it and installing the requirements. This can be achieved using the following commands:

```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
```

## Usage

The program can be launched as follows:

```
$ python3 runner.py
```

Once launched, the player will be asked to choose between playing as `X` or as `O`. The game will then start. Once done playing, the virtual environment must be deactivated with the following command:

```
$ deactivate
```

## See More

This project is part of the [CS50 - Artificial Intelligence](https://harvardonline.harvard.edu/course/cs50s-introduction-artificial-intelligence-python) class by Harvard. More information about this specific project can be found [here](https://cs50.harvard.edu/ai/projects/0/tictactoe/).
