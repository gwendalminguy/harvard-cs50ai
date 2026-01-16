# Knights

This program solves [Knights and Knaves](https://en.wikipedia.org/wiki/Knights_and_Knaves) logic puzzles, in which each character is either a knight or a knave. A knight will always tell the truth, and a knave will always lie.

## Understanding

This program solves four of these puzzles, described in `puzzle.py`, by representing them using **propositional logic**. Each puzzle's knowledge is built using **logical connectives**, which is then used by the program to draw conclusions about the identity of each character.

## Files

This project contains the following files:

| Element | Description |
| :---- | :---------- |
| `logic.py` | The python file containing useful class implementations. |
| `puzzle.py` | The python script to define and solve puzzles. |

## Usage

The program can be launched as follows:

```
$ python3 puzzle.py
```

Conclusions for each puzzle are then printed to the terminal.

## See More

This project is part of the [CS50 - Artificial Intelligence](https://harvardonline.harvard.edu/course/cs50s-introduction-artificial-intelligence-python) class by Harvard. More information about this specific project can be found [here](https://cs50.harvard.edu/ai/projects/1/knights/).
