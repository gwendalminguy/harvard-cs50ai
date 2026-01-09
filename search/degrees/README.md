# Degrees

This program determines how many "degrees of separation" apart two actors are, by finding the shortest path between any two actors by choosing a sequence of movies that connects them. It is based on the [Six Degrees of Kevin Bacon](https://en.wikipedia.org/wiki/Six_Degrees_of_Kevin_Bacon) game.

## Understanding

This program works as solving a search problem, where the **initial state** is the first actor, and the **goal state** is the second actor. The program finds the shortest path connecting the two actors using an implementation of **breadth-first search**, by building and maintaining a **queue frontier** of state nodes (which are actors), and exploring neighbor actors first.

## Usage

The program can be launched as follows:

```
$ python3 degrees.py [<data_directory>]
```

Once the data is loaded, the program will prompt the user for an actor's name, then for another. If both actors are connected somehow, it will print thier degree of separation, and the details of the shortest path connecting them. The `data_directory` is an optional argument, which can be either `small` (reduced dataset to test the program) or `large` (much more complete but slower). If not given, the `large` dataset will be used by default.
