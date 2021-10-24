import random

class Board:
    """A designated playing surface. The responsibility of Board is to keep track of the pieces in play.
    
    Stereotype: 
        Information Holder

    Attributes:
        _piles (list): The number of piles of stones.
    """
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Board): an instance of Board.
        """
        self._items = [0, 0]
        self._current = 0
        self._prepare()

    def _prepare(self):
        """Sets up the board with an entry for each player.
        
        Args:
            self (Board): an instance of Board.
        """
        for i in range(2):    
            code = str(random.randint(1000, 9999))
            guess = "----"
            hint = "****"
            self._items[i] = [code, guess, hint]

    def to_string(self, roster):
        """Converts the board data to its string representation.

        Args:
           self (Board): an instance of Board.

        Returns:
            string: A representation of the current board.
        """
        text =  "\n----------------------------"
        for row, values in enumerate(self._items):
            text += (f"\nPlayer {roster.players[row].get_name()}:   {values[1]}, {values[2]}")
        text += "\n----------------------------"
        return text

    def get_protected_code(self):
        """Returns the players's code from the board.
        Args:
            self (Board): an instance of Board.
        """
        return self._items[self._current][0]
        
    def create_hint(self, comparison):
        """Generates a hint based on the given code and guess.

        Args:
            self (Board): An instance of Board.
            code (string): The code to compare with.
            guess (string): The guess that was made.

        Returns:
            string: A hint in the form [xxxx]
        """ 
        hint = ""
        code = comparison.get_code()
        guess = comparison.get_guess()

        for index, number in enumerate(guess):
            if code[index] == number:
                hint += "x"
            elif number in code:
                hint += "o"
            else:
                hint += "*"
        
        self._items[self._current][1] = guess
        self._items[self._current][2] = hint

    def discovered_code(self):
        """Determines if all the stones have been removed from the board.
        
        Args:
            self (Board): an instance of Board.

        Returns:
            boolean: True if the board has no stones on it; false if otherwise.
        """
        code = self._items[self._current][0]
        guess = self._items[self._current][1]

        if code == guess:
            return True
        else:
            self._current = (self._current + 1) % len(self._items)