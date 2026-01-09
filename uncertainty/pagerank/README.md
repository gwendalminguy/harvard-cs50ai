# PageRank

This program ranks web pages of a corpus by importance, based on the way search engines work.

## Understanding

This program works by implementing a [PageRank](https://en.wikipedia.org/wiki/PageRank) algorithm, that computes scores for each page using two distinct methods.

The first method proceeds by **sampling**, and simulates a user clicking on a link present on a web page, which leads to another, and repeats the operation on the new page. The process is repeated a certain number of times (set to be 10000 in `pagerank.py`), and keeps track of the number of times each page has been visited. This method can be seen as a **Markov Chain**, where each page represents a state, and each page has a transition model that chooses among its links at random. A damping factor `d` (set to be 0.85 in `pagerank.py`) will help ensure all pages can be visited, by beeing chosen randomly with probability `1 - d`.

The second method proceeds by **iterating**, and starts by giving each page the same score, then iteratively adjust the score of each page by computing a new one (based on aplying a formula to the previous score), until all the scores are stable. The formula used to compute a a new score for a given page is the following:

$$PR(p) = \frac{1 - d}{N} + d\sum_{i}\frac{PR(i)}{NumLinks(i)}$$

In this formula, `d` is the damping factor, `N` is the total number of pages in the corpus, `i` ranges over all pages that link to page `p`, and `NumLinks(i)` is the number of links present on page `i`.

## Usage

The program can be launched as follows:

```
$ python3 pagerank.py <corpus_directory>
```

Once the program launched, it will compute a score for each web page and rank them by importance. It will do so twice, the first time by **sampling**, and the second time by **iterating**, and print both results to the terminal. The `corpus_directory` argument must be the name of a directory containing web pages. It can be one of the provided directories (`corpus0`, `corpus1` or `corpus2`), or any other directory, as long as it contains `HTML` web pages, and that each link to another web page found in a file that relates to a page of the corpus has the same name as the matching file.
