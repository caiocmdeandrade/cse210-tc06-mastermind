
from game.board import Board
from game.player import Player
from game.roster import Roster
from game.console import Console
from game.comparison import Comparison

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        board (Hunter): An instance of the class of objects known as Board.
        console (Console): An instance of the class of objects known as Console.
        keep_playing (boolean): Whether or not the game can continue.
        comparison (Rabbit): An instance of the class of objects known as Comparison.
        roster (Roster): An instance of the class of objects known as Roster.
    """

    def __init__(self):
        """The class constructor.

        Args:
            self (Director): an instance of Director.
        """
        self._board = Board()
        self._roster = Roster()
        self._console = Console()
        self._keep_playing = True
        self._comparison = None
        
    def start_game(self):
        """Starts the game loop to control the sequence of play.

        Args:
            self (Director): an instance of Director.
        """
        self._prepare_game()
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _prepare_game(self):
        """Prepares the game before it begins. In this case, that means getting the player names and adding them to the roster.

        Args:
            self (Director): An instance of Director.
        """
        for n in range(2):
            name = self._console.read(f"Enter a name for player {n + 1}: ")
            player = Player(name)
            self._roster.add_player(player)

    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the move from the current player.

        Args:
            self (Director): An instance of Director.
        """
        board = self._board.to_string(self._roster)
        self._console.write(board)

        player = self._roster.get_current()
        self._console.write(f"{player.get_name()}'s turn:")
        guess = self._console.read("What is your guess? ")
        code = self._board.get_protected_code()
        comparison = Comparison(code, guess)
        player.set_comparison(comparison)

    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means updating the board with the current comparison
        
        Args:
            self (Director): An instance of Director.
        """
        player = self._roster.get_current()
        comparison = player.get_comparison()
        self._board.create_hint(comparison)
        
    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if there is a code that has been found and declaring the winner.
        
        Args:
            self (Director): An instance of Director.
        """
        if self._board.discovered_code():
            winner = self._roster.get_current()
            name = winner.get_name()
            print(f"\n{name} won!")
            self._keep_playing = False

        self._roster.next_player()