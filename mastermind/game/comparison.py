class Comparison:
  """An action in the game. The responsibility of Comparison is to keep track of the players secret code and their guesses.
    
  Stereotype: 
    Information Holder

  Attributes:
    _guess (string): The pile to remove from.
    _code (string): The number of stones to remove.
  """
  def __init__(self, code, guess):
    """The class constructor.
        
    Args:
      self (Board): an instance of Board.
    """
    self._code = code
    self._guess = guess

  def get_code(self):
    """Returns the games hint.

    Args:
      self (Secret): an instance of Secret.
    """
    return self._code

  def get_guess(self):
    """Returns the player guess.

    Args:
      self (Secret): an instance of Secret.
    """
    return self._guess