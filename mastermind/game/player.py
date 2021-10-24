class Player:
  """A person taking part in a game. The responsibility of Player is to keep track of their identity and last comparison.
    
    Stereotype: 
        Information Holder

    Attributes:
        _name (string): The player's name.
        _comparison (Comparison): The player's last comparison.
  """
  def __init__(self, name):
      """The class constructor.
      
      Args:
          self (Player): an instance of Player.
      """
      self._name = name
      self._guess = None

  def get_name(self):
      """The class constructor.

        Args:
            self (Player): an instance of Player.
      """
      return self._name

  def set_comparison(self, comparison):
      """Sets the player's last comparison to the given instance of Comparison.
          
          Args:
            self (Player): an instance of Player.
            comparison (Comparison): an instance of Comparison
      """
      self._comparison = comparison

  def get_comparison(self):
      """Returns the player's last comparison (an instance of Comparison). If the player 
        hasn't compared yet this method returns None.

        Args:
            self (Player): an instance of Player.
      """
      return self._comparison