# Heredity

This program assesses the likelihood that a person will have a particular genetic trait.

## Understanding

This program computes, for each person in a family, the **probability distribution** over having 0, 1, or 2 copies of a specific gene, as well as the probability of exhibiting the associated trait. Using unconditional gene probabilities, inheritance rules from parents (including mutation), and known evidence about whether individuals do or do not show the trait, the program enumerates all possible genetic configurations. For each configuration, it calculates a **joint probability**, accumulates these probabilities for each person, and finally **normalizes** the results so that all probability distributions sum to 1.

## Usage

The program can be launched as follows:

```
$ python3 heredity.py <data_file>
```

Once the program launched, it will compute for each person in the family the probability that it has 0, 1 or 2 copies of the gene, and the probability that it has the trait or not. The results will then be printed to the terminal. The `data_file` argument must be the name of a `CSV` file in the `data/` directory. It can be one of the provided files (`family0.csv`, `family1.csv` or `family2.csv`), or any other one, as long as it is structured the same way.
