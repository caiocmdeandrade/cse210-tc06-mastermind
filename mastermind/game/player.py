class Player:
  """A person taking part in a game. 
  The responsibility of Player is to keep track of their identity and last guess.
  
  Stereotype: 
      Information Holder

  Attributes:
      _name (string): The player's name.
      _guess (Guess): The player's last guess.
  """
  def __init__(self, name):
      """The class constructor.
      
      Args:
          self (Player): an instance of Player.
      """
      self._name = name
      self._guess = None
  def get_name(self):
      """Returns the player's name.

      Args:
          self (Player): an instance of Player.
      """
      return self._name

  def set_comparison(self, comparison):
      """Returns the player's last guess (an instance of guess).
      If the player hasn't guessed yet this method returns None.

      Args:
          self (Player): an instance of Player.
      """
      self._comparison = comparison

  def get_comparison(self):
      """Returns the player's last move (an instance of Move). If the player 
      hasn't moved yet this method returns None.

      Args:
          self (Player): an instance of Player.
      """
      return self._comparison