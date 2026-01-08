import sys

from crossword import *


class CrosswordCreator():

    def __init__(self, crossword):
        """
        Create new CSP crossword generate.
        """
        self.crossword = crossword
        self.domains = {
            var: self.crossword.words.copy()
            for var in self.crossword.variables
        }

    def letter_grid(self, assignment):
        """
        Return 2D array representing a given assignment.
        """
        letters = [
            [None for _ in range(self.crossword.width)]
            for _ in range(self.crossword.height)
        ]
        for variable, word in assignment.items():
            direction = variable.direction
            for k in range(len(word)):
                i = variable.i + (k if direction == Variable.DOWN else 0)
                j = variable.j + (k if direction == Variable.ACROSS else 0)
                letters[i][j] = word[k]
        return letters

    def print(self, assignment):
        """
        Print crossword assignment to the terminal.
        """
        letters = self.letter_grid(assignment)
        for i in range(self.crossword.height):
            for j in range(self.crossword.width):
                if self.crossword.structure[i][j]:
                    print(letters[i][j] or " ", end="")
                else:
                    print("█", end="")
            print()

    def save(self, assignment, filename):
        """
        Save crossword assignment to an image file.
        """
        from PIL import Image, ImageDraw, ImageFont
        cell_size = 100
        cell_border = 2
        interior_size = cell_size - 2 * cell_border
        letters = self.letter_grid(assignment)

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.crossword.width * cell_size,
             self.crossword.height * cell_size),
            "black"
        )
        font = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", 80)
        draw = ImageDraw.Draw(img)

        for i in range(self.crossword.height):
            for j in range(self.crossword.width):

                rect = [
                    (j * cell_size + cell_border,
                     i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border,
                     (i + 1) * cell_size - cell_border)
                ]
                if self.crossword.structure[i][j]:
                    draw.rectangle(rect, fill="white")
                    if letters[i][j]:
                        _, _, w, h = draw.textbbox((0, 0), letters[i][j], font=font)
                        draw.text(
                            (rect[0][0] + ((interior_size - w) / 2),
                             rect[0][1] + ((interior_size - h) / 2) - 10),
                            letters[i][j], fill="black", font=font
                        )

        img.save(filename)

    def solve(self):
        """
        Enforce node and arc consistency, and then solve the CSP.
        """
        self.enforce_node_consistency()
        self.ac3()
        return self.backtrack(dict())

    def enforce_node_consistency(self):
        """
        Update `self.domains` such that each variable is node-consistent.
        (Remove any values that are inconsistent with a variable's unary
         constraints; in this case, the length of the word.)
        """
        for var in self.domains:
            inconsistent = set()

            # Looking for inconsistent words
            for word in self.domains[var]:
                if len(word) != var.length:
                    inconsistent.add(word)

            # Updating domain by removing inconsistent words
            self.domains[var] = self.domains[var].difference(inconsistent)

    def revise(self, x, y):
        """
        Make variable `x` arc consistent with variable `y`.
        To do so, remove values from `self.domains[x]` for which there is no
        possible corresponding value for `y` in `self.domains[y]`.

        Return True if a revision was made to the domain of `x`; return
        False if no revision was made.
        """
        overlap = self.crossword.overlaps[x, y]

        if not overlap:
            return False

        inconsistent = set()

        # Iterating through x to find inconsistent values
        for word_a in self.domains[x]:
            match = False
            for word_b in self.domains[y]:
                if word_a[overlap[0]] == word_b[overlap[1]]:
                    match = True
                    break
            if not match:
                inconsistent.add(word_a)

        # Removing inconsistent values from x
        if len(inconsistent):
            self.domains[x] = self.domains[x].difference(inconsistent)
            return True

        return False

    def ac3(self, arcs=None):
        """
        Update `self.domains` such that each variable is arc consistent.
        If `arcs` is None, begin with initial list of all arcs in the problem.
        Otherwise, use `arcs` as the initial list of arcs to make consistent.

        Return True if arc consistency is enforced and no domains are empty;
        return False if one or more domains end up empty.
        """
        # Initializing arcs list if None
        if arcs is None:
            arcs = []
            for x in self.domains:
                for y in self.crossword.neighbors(x):
                    arcs.append((x, y))

        # Revising each arc while list not empty
        while arcs:
            x, y = arcs.pop(0)
            change = False
            change = self.revise(x, y)
            if change:
                # Stopping if empty domain
                if not self.domains[x]:
                    return False
                # Adding new arcs if necessary
                for z in self.crossword.neighbors(x):
                    if z != y:
                        arcs.append((x, z))
                        arcs.append((z, x))

        return True


    def assignment_complete(self, assignment):
        """
        Return True if `assignment` is complete (i.e., assigns a value to each
        crossword variable); return False otherwise.
        """
        if len(assignment) != len(self.domains):
            return False

        return True

    def consistent(self, assignment):
        """
        Return True if `assignment` is consistent (i.e., words fit in crossword
        puzzle without conflicting characters); return False otherwise.
        """
        keys = assignment.keys()
        values = assignment.values()

        # Checking if all values are different
        if len(values) != len(set(values)):
            return False

        # Checking if each value has correct length
        for var in keys:
            if len(assignment[var]) != var.length:
                return False

        # Checking if overlapping values match
        for var_a in keys:
            for var_b in keys:
                overlap = None
                if var_a != var_b:
                    overlap = self.crossword.overlaps[var_a, var_b]
                    if overlap:
                        word_a = assignment[var_a]
                        word_b = assignment[var_b]
                        if word_a[overlap[0]] != word_b[overlap[1]]:
                            return False

        return True

    def order_domain_values(self, var, assignment):
        """
        Return a list of values in the domain of `var`, in order by
        the number of values they rule out for neighboring variables.
        The first value in the list, for example, should be the one
        that rules out the fewest values among the neighbors of `var`.
        """
        values = [{"value": value, "n": 0} for value in self.domains[var]]
        neighbors = self.crossword.neighbors(var)

        # Computing n as number of values ruled out in neighbors for each possible value for var
        for element in values:
            n = 0
            for neighbor in neighbors:
                overlap = self.crossword.overlaps[var, neighbor]
                for choice in self.domains[neighbor]:
                    if element["value"][overlap[0]] != choice[overlap[1]]:
                        n += 1
            element["n"] += n

        # Ordering list of values according to n
        ordered = [element["value"] for element in sorted(values, key=lambda x: x["n"])]

        return ordered

    def select_unassigned_variable(self, assignment):
        """
        Return an unassigned variable not already part of `assignment`.
        Choose the variable with the minimum number of remaining values
        in its domain. If there is a tie, choose the variable with the highest
        degree. If there is a tie, any of the tied variables are acceptable
        return values.
        """
        variables = []
        assigned = list(assignment.keys())

        # Adding all unassigned variables to a list
        for var in self.crossword.variables:
            if var not in assigned:
                variables.append({"var": var, "n": len(self.domains[var])})

        # Ordering list of variables according to n number of values in var domain
        ordered = [element["var"] for element in sorted(variables, key=lambda x: x["n"])]

        return ordered.pop(0)

    def backtrack(self, assignment):
        """
        Using Backtracking Search, take as input a partial assignment for the
        crossword and return a complete assignment if possible to do so.

        `assignment` is a mapping from variables (keys) to words (values).

        If no assignment is possible, return None.
        """
        if self.assignment_complete(assignment):
            return assignment

        var = self.select_unassigned_variable(assignment)

        # Trying an assignment for each value
        for value in self.order_domain_values(var, assignment):
            assignment[var] = value

            # Calling backtrack recursively of assignment consistent
            if self.consistent(assignment):
                result = self.backtrack(assignment)
                if result:
                    return result

            # Removing assignment on failure
            assignment.pop(var)

        return None


def main():

    # Check usage
    if len(sys.argv) not in [3, 4]:
        sys.exit("Usage: python generate.py structure words [output]")

    # Parse command-line arguments
    structure = sys.argv[1]
    words = sys.argv[2]
    output = sys.argv[3] if len(sys.argv) == 4 else None

    # Generate crossword
    crossword = Crossword(structure, words)
    creator = CrosswordCreator(crossword)
    assignment = creator.solve()

    # Print result
    if assignment is None:
        print("No solution.")
    else:
        creator.print(assignment)
        if output:
            creator.save(assignment, output)


if __name__ == "__main__":
    main()
