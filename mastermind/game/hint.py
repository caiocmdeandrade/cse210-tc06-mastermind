class Hint:
    """An action in the game. The responsibility of Hints is to keep track of the players guesses and the game hints.
    
    Stereotype: 
        Information Holder

    Attributes:
        _guess (string): The pile to remove from.
        _hint (string): The number of stones to remove.
    """
    def __init__(self, guess, hint):
        """The class constructor.
        
        Args:
            self (Board): an instance of Board.
        """
        self._guess = guess
        self._hint = hint

    def get_guess(self):
        """Returns the player guess.

        Args:
            self (Hints): an instance of Hints.
        """
        return self._guess

    def get_hint(self):
        """Returns the games hint.

        Args:
            self (Hints): an instance of Hints.
        """
        return self._hint