import itertools
import random


class Minesweeper():
    """
    Minesweeper game representation
    """

    def __init__(self, height=8, width=8, mines=8):

        # Set initial width, height, and number of mines
        self.height = height
        self.width = width
        self.mines = set()

        # Initialize an empty field with no mines
        self.board = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(False)
            self.board.append(row)

        # Add mines randomly
        while len(self.mines) != mines:
            i = random.randrange(height)
            j = random.randrange(width)
            if not self.board[i][j]:
                self.mines.add((i, j))
                self.board[i][j] = True

        # At first, player has found no mines
        self.mines_found = set()

    def print(self):
        """
        Prints a text-based representation
        of where mines are located.
        """
        for i in range(self.height):
            print("--" * self.width + "-")
            for j in range(self.width):
                if self.board[i][j]:
                    print("|X", end="")
                else:
                    print("| ", end="")
            print("|")
        print("--" * self.width + "-")

    def is_mine(self, cell):
        i, j = cell
        return self.board[i][j]

    def nearby_mines(self, cell):
        """
        Returns the number of mines that are
        within one row and column of a given cell,
        not including the cell itself.
        """

        # Keep count of nearby mines
        count = 0

        # Loop over all cells within one row and column
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):

                # Ignore the cell itself
                if (i, j) == cell:
                    continue

                # Update count if cell in bounds and is mine
                if 0 <= i < self.height and 0 <= j < self.width:
                    if self.board[i][j]:
                        count += 1

        return count

    def won(self):
        """
        Checks if all mines have been flagged.
        """
        return self.mines_found == self.mines


class Sentence():
    """
    Logical statement about a Minesweeper game
    A sentence consists of a set of board cells,
    and a count of the number of those cells which are mines.
    """

    def __init__(self, cells, count):
        self.cells = set(cells)
        self.count = count

    def __eq__(self, other):
        return self.cells == other.cells and self.count == other.count

    def __str__(self):
        return f"{self.cells} = {self.count}"

    def known_mines(self):
        """
        Returns the set of all cells in self.cells known to be mines.
        """
        n = len(self.cells)
        if n == self.count:
            return self.cells
        return set()

    def known_safes(self):
        """
        Returns the set of all cells in self.cells known to be safe.
        """
        n = len(self.cells)
        if self.count == 0 and n > 0:
            return self.cells
        return set()

    def mark_mine(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be a mine.
        """
        if cell in self.cells:
            self.cells.remove(cell)
            self.count -= 1

    def mark_safe(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be safe.
        """
        if cell in self.cells:
            self.cells.remove(cell)


class MinesweeperAI():
    """
    Minesweeper game player
    """

    def __init__(self, height=8, width=8):

        # Set initial height and width
        self.height = height
        self.width = width

        # Keep track of which cells have been clicked on and which cells remain
        self.moves_made = set()
        self.remaining_moves = set()

        # Keep track of cells known to be safe or mines
        self.mines = set()
        self.safes = set()

        # List of sentences about the game known to be true
        self.knowledge = []

        # Initializing remaining cells
        for i in range(height):
            for j in range(width):
                self.remaining_moves.add((i, j))

    def mark_mine(self, cell):
        """
        Marks a cell as a mine, and updates all knowledge
        to mark that cell as a mine as well.
        """
        self.mines.add(cell)
        if cell in self.remaining_moves:
            self.remaining_moves.remove(cell)
        for sentence in self.knowledge:
            sentence.mark_mine(cell)

    def mark_safe(self, cell):
        """
        Marks a cell as safe, and updates all knowledge
        to mark that cell as safe as well.
        """
        self.safes.add(cell)
        for sentence in self.knowledge:
            sentence.mark_safe(cell)

    def add_knowledge(self, cell, count):
        """
        Called when the Minesweeper board tells us, for a given
        safe cell, how many neighboring cells have mines in them.

        This function should:
            1) mark the cell as a move that has been made
            2) mark the cell as safe
            3) add a new sentence to the AI's knowledge base
               based on the value of `cell` and `count`
            4) mark any additional cells as safe or as mines
               if it can be concluded based on the AI's knowledge base
            5) add any new sentences to the AI's knowledge base
               if they can be inferred from existing knowledge
        """
        self.moves_made.add(cell)
        self.remaining_moves.remove(cell)
        self.mark_safe(cell)

        new = []

        # Finding neighbour cells
        for x in range(3):
            i = cell[0] - 1 + x
            for y in range(3):
                j = cell[1] - 1 + y
                if i < 0 or i >= self.height or j < 0 or j >= self.width:
                    continue
                if (i, j) in self.safes or (i, j) in self.moves_made:
                    continue
                new.append((i, j))

        # Adding knowledge
        if len(new) > 0:
            if count > 0:
                # Removing known mines
                for element in new:
                    if element in self.mines:
                        new.remove(element)
                        count -= 1
                # Adding new sentence
                if len(new) > 0:
                    sentence = Sentence(new, count)
                    if sentence not in self.knowledge:
                        self.knowledge.append(sentence)
            else:
                for element in new:
                    self.mark_safe(element)

        # Marking all cells as mines if sure
        if len(new) == count:
            for element in new:
                self.mark_mine(element)

        # Infering new sentences
        add_sentences = []
        for sentence_a in self.knowledge:
            for sentence_b in self.knowledge:
                if sentence_a == sentence_b:
                    continue
                if sentence_a.cells.issubset(sentence_b.cells):
                    items = sentence_b.cells.difference(sentence_a.cells)
                    quantity = sentence_b.count - sentence_a.count
                    new_sentence = Sentence(items, quantity)
                    if new_sentence not in self.knowledge:
                        add_sentences.append(new_sentence)
        # Adding new sentences to knowledge
        if len(add_sentences):
            for sentence in add_sentences:
                self.knowledge.append(sentence)

        # Looking for mines and safes
        for sentence in self.knowledge:
            # Removing sentence if empty
            if len(sentence.cells) == 0 and sentence.count == 0:
                self.knowledge.remove(sentence)
            # Marking known mines
            self.find_mines(sentence)
            # Looking for known safes
            self.find_safes(sentence)

    def find_mines(self, sentence):
        """
        Infers if a sentence contains only mines.
        """
        if len(sentence.cells) == sentence.count:
            mines = []
            for element in sentence.cells:
                mines.append(element)
            if mines:
                for cell in mines:
                    self.mark_mine(cell)
                for element in self.knowledge:
                    self.find_safes(element)

    def find_safes(self, sentence):
        """
        Infers if a sentence contains only safes.
        """
        if sentence.count == 0 and len(sentence.cells):
            safes = []
            for element in sentence.cells:
                safes.append(element)
            if safes:
                for cell in safes:
                    self.mark_safe(cell)
                for element in self.knowledge:
                    self.find_mines(element)

    def make_safe_move(self):
        """
        Returns a safe cell to choose on the Minesweeper board.
        The move must be known to be safe, and not already a move
        that has been made.

        This function may use the knowledge in self.mines, self.safes
        and self.moves_made, but should not modify any of those values.
        """
        if self.safes:
            done = list(self.moves_made)
            available = list(self.safes)
            for move in available:
                if move not in done:
                    return move
        return None

    def make_random_move(self):
        """
        Returns a move to make on the Minesweeper board.
        Should choose randomly among cells that:
            1) have not already been chosen, and
            2) are not known to be mines
        """
        if self.remaining_moves:
            move = random.choice(list(self.remaining_moves))
            return move
        return None
