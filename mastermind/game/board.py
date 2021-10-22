import random

class Board:
    """A designated playing surface. The responsibility of Board is to keep track of the pieces in play.
    
    Stereotype: 
        Information Holder
    Attributes:
        _items (list): The number of piles of stones.
    """
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Board): an instance of Board.
        """
        self._items = []
        self._prepare()

    def _create_hint(self, code, guess):
      """Generates a hint based on the given code and guess.

      Args:
          self (Board): An instance of Board.
          code (string): The code to compare with.
          guess (string): The guess that was made.

      Returns:
          string: A hint in the form [xxxx]
      """ 
      hint = ""
      for index, letter in enumerate(guess):
          if code[index] == letter:
              hint += "x"
          elif letter in code:
              hint += "o"
          else:
              hint += "*"
      return hint
    
    def is_empty(self):
        """Determines if all the stones have been removed from the board.
        
        Args:
            self (Board): an instance of Board.
        Returns:
            boolean: True if the board has no stones on it; false if otherwise.
        """
        empty = [0] * len(self._piles)
        return self._piles == empty

    def to_string(self):
        """Converts the board data to its string representation.
        Args:
           self (Board): an instance of Board.
        Returns:
            string: A representation of the current board.
        """ 
        text =  "\n--------------------"
        for pile, stones in enumerate(self._piles):
            text += (f"\n{pile}: " + "O " * stones)
        text += "\n--------------------"
        return text

    def prepare(self, player):
            """Sets up the board with an entry for each player.
            
            Args:
                self (Board): an instance of Board.
            """
            name = player.get_name()
            code = str(random.randint(1000, 10000))
            guess = "----"
            hint = "****"
            self._items[name] = [code, guess, hint]