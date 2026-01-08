import nltk
import sys

TERMINALS = """
Adj -> "country" | "dreadful" | "enigmatical" | "little" | "moist" | "red"
Adv -> "down" | "here" | "never"
P -> "at" | "before" | "after" | "in" | "of"
P -> "with" | "by" | "from" | "about" | "on" | "to"

Coo -> "for" | "and" | "nor" | "but" | "or" | "yet" | "so"
Sub -> "when" | "while" | "before" | "after" | "since" | "until" | "whenever"
Sub -> "that" | "if" | "whether" | "because" | "as" | "unless"
Sub -> "although" | "though" | "whereas"

Det -> "a" | "an" | "his" | "my" | "the" | "their" | "our" | "some"
N -> "armchair" | "companion" | "day" | "door" | "hand" | "he" | "himself"
N -> "holmes" | "home" | "i" | "mess" | "paint" | "palm" | "pipe" | "she"
N -> "smile" | "thursday" | "walk" | "we" | "word" | "wallet"
V -> "arrived" | "came" | "chuckled" | "had" | "lit" | "said" | "sat"
V -> "smiled" | "tell" | "were" | "left" | "did" | "went" | "worked"
"""

NONTERMINALS = """
S -> NP VP
S -> S Coo S
S -> NP VP Sub S

VP -> V
VP -> Adv VP
VP -> VP Adv
VP -> VP NP
VP -> VP PP
VP -> VP Coo VP

NP -> N
NP -> Det N
NP -> Det AdjP N
NP -> NP PP
NP -> NP Coo NP

AdjP -> Adj
AdjP -> Adj AdjP

PP -> P NP
"""

grammar = nltk.CFG.fromstring(NONTERMINALS + TERMINALS)
parser = nltk.ChartParser(grammar)


def main():

    # If filename specified, read sentence from file
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            s = f.read()

    # Otherwise, get sentence as input
    else:
        s = input("Sentence: ")

    # Convert input into list of words
    s = preprocess(s)

    # Attempt to parse sentence
    try:
        trees = list(parser.parse(s))
    except ValueError as e:
        print(e)
        return
    if not trees:
        print("Could not parse sentence.")
        return

    # Print each tree with noun phrase chunks
    for tree in trees:
        tree.pretty_print()

        print("Noun Phrase Chunks")
        for np in np_chunk(tree):
            print(" ".join(np.flatten()))


def preprocess(sentence):
    """
    Convert `sentence` to a list of its words.
    Pre-process sentence by converting all characters to lowercase
    and removing any word that does not contain at least one alphabetic
    character.
    """
    words = nltk.word_tokenize(sentence)
    result = []

    for word in words:
        if word.isalpha():
            result.append(word.lower())

    return result


def np_chunk(tree):
    """
    Return a list of all noun phrase chunks in the sentence tree.
    A noun phrase chunk is defined as any subtree of the sentence
    whose label is "NP" that does not itself contain any other
    noun phrases as subtrees.
    """
    noun_phrase_chunks = []

    for element in tree.subtrees(filter=lambda t: t.label() == "NP"):
        if "NP" not in [e.label() for e in element.subtrees()][1:]:
            noun_phrase_chunks.append(element)

    return noun_phrase_chunks


if __name__ == "__main__":
    main()
