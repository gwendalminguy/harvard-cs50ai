# Crossword

This program generates crossword puzzles.

## Understanding

This program automatically solves a crossword puzzle by modeling it as a **constraint satisfaction problem**. Each slot in the crossword is represented as a variable whose possible values are words from a given list of words, and each word length constitutes a **unary constraint**, while each overlapping position for two words constitutes a **binary constraint**. The program first reduces the possible words for each variable by enforcing **node consistency** and **arc consistency**, then uses a **backtracking search** to assign words to all variables while satisfying all constraints.

## Files

This project contains the following files and directories:

| Element | Description |
| :---- | :---------- |
| `assets/` | The directory containing a font file. |
| `data/` | The directory containing structures and words text files. |
| `crossword.py` | The python file containing useful class implementations. |
| `generate.py` | The python script to generate a crossword puzzle. |
| `requirements.txt` | The text file listing requirements for installation. |

## Installation

In order to save the output as an image file, a small installation needs to be made, by creating a virtual environment, activating it and installing the requirements. This can be achieved using the following commands:

```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
```

## Usage

The program can be launched as follows:

```
$ python3 generate.py <structure_file.txt> <words_file.txt> [<output_name.png>]
```

Once the program launched, it will find a solution, if one exists, to fill the given crossword puzzle structure with a matching combination of words from the given list. The `structure_file.txt` argument must be a text file representing a crossword puzzle structure, by containing solid blocks, represented with the `#` character, and empty blocks, represented with the `_` character. The `words_file.txt` argument must be a text file containing a list of words, one per line, that can be used to solve the puzzle. The solution will be printed to the terminal, and saved to an image file if the `output_name.png` argument is specified.
