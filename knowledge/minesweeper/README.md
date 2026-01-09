# Minesweeper

This program implements a small AI able to play the [Minesweeper](https://en.wikipedia.org/wiki/Minesweeper_(video_game)) game.

## Understanding

The program works by accumulating knowledge about the board of the game at each move, and drawing new knowledge by **inference** when it can, based on the information given by the number found when making a move (which represents the number of neighboring cells that are mine cells). This knowledge is then used to categorize, among the remaining cells, which are safe cells and which are mine cells. Since there can sometimes be no safe cell known, the AI can still lose the game by making a random move on a mine cell.

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

Once launched, the player can either make a move by clicking on a cell, or let the AI figure out a move by clicking on the `AI Move` button. In this case, the AI will make a safe move if possible, or a random one otherwise. Once done playing, the virtual environment must be deactivated with the following command:

```
$ deactivate
```
