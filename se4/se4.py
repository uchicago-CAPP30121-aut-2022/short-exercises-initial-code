"""
Short Exercises #4
Implement a terminal-based tic-tac-toe game
"""

SIZE = 3

class Board:
    """
    Board class
    -----------
      Represents the state of the tic-tac-toe board

    Board attributes
    ----------------
      board (list of lists of strings): the game board

    Board methods
    -------------
      valid_move(location): 
        determines whether or not a move is valid
      play_move(location, player):
        plays one move on the board
      winner(player):
        determines whether player is a winner
    """ 

    def __init__(self):
        """
        Consructor for the Board class
        """
        
        # REPLACE pass with appropriate code.
        pass

    def valid_move(self, location):
        """
        Determine whether or not a move is valid

        Input:
          location (tuple of (int, int)): the row, column location of the move

        Returns:
          True if move is valid, False otherwise
        """
        
        # YOUR CODE HERE
        # Replace None with an appropriate return value
        return None

    def play_move(self, location, player):
        """
        Play one move in the game

        Input:
          location (tuple of (int, int)): the row, column location of the move
          player (Player): the player moving

        Returns:
          True if move is possible, Falser otherwise
        """
        
        # YOUR CODE HERE
        # Replace None with an appropriate return value
        return None

    def winner(self, player):
        """
        Determine whether or not a player is a winner

        Input:
          player (Player): the player

        Returns: 
          True if player has three-in-a-row vertically or horizontally,
          False otherwise
        """

        # YOUR CODE HERE
        # Replace None with an appropriate return value
        return None

    def __str__(self):
        """
        Create a string representation of the board

        Returns (string): string representation of the board
        """

        # YOUR CODE HERE
        # Replace None with an appropriate return value
        return None

"""
DO NOT MODIFY THE CODE BELOW
"""

class Player:
    """
    Player class
    ------------

    Player attributes
    -----------------
      name (string): player's name
      symbol (string): player's symbol (one character)
    """ 

    def __init__(self, name, symbol):
        """
        Consructor for the Player class
        """
        self.name = name
        self.symbol = symbol

class Game:
    """
    Game class
    ----------

    Game attributes
    ---------------
      board (Board): the game board
      player1 (Player): first player
      player2 (Player): second player
      winner (Boolean): True if game has a winner,
        False otherwise 

    Game methods
    ------------
      valid_input(keyboard): 
        checks that a user enters valid input
      get_input(player_num):
        reads user input from the keyboard
      start(): 
        starts the game
      next_up(player):
        determines the next player
      turn(player):
        plays one turn of the game
      play():
        runs the game
    """

    def __init__(self):
        """
        Consructor for the Game class
        """
        self.board = Board()
        self.player1 = None
        self.player2 = None
        self.winner = False

    def valid_input(self, keyboard):
        """
        Validate name and symbol:
          name is one string
          symbol is one character

        Input:
          keyboard (string): keyboard input

        Returns: True if valid, False otherwise
        """
        split = keyboard.split()
        return len(split) == 2 and len(split[1]) == 1

    def get_intput(self, player_num):
        """
        Get name and symbol from player

        Input:
          player_num (string): player 

        Returns: the tuple:
          name (string): name of player
          symbol (string): player's symbol
        """
        s = "Player " + player_num + ": Enter you name and pick your symbol: "

        valid = False
        while not valid:
            keyboard = input(s)
            valid = self.valid_input(keyboard)
            if not valid:
                print("Player", player_num, "enter valid input this time...")
        name, symbol = keyboard.split()
        return name, symbol

    def start(self):
        """
        Method to start game 
          Collect keyboard input
          Initialize player1 and player2
        """
        print("\nReady to play tic-tac-toe?\n")

        name, symbol = self.get_intput("1")
        self.player1 = Player(name, symbol)
        name, symbol = self.get_intput("2")
        self.player2 = Player(name, symbol)

        print()

    def next_up(self, player):
        """
        Method to switch players

        Input:
          player (Player): current player

        Returns: next player
        """
        if player is self.player1:
            return self.player2
        else: 
            return self.player1

    def turn(self, player):
        """
        Method to play one turn of game
          Collect keyboard input
          Play move

        Input:
          player (Player): current player
        """
        valid = False
        while not valid:
            keyboard = input("Enter your move {}: ".format(player.name))
            row, col = keyboard.split()
            if self.board.play_move((int(row), int(col)), player):
                valid = True
        
    def play(self):
        """
        Method to run the game
          Start game
          Play turns 
          Check for winner
          Display result
        """
        self.start()
        player = self.player1

        for play in range(SIZE*SIZE):
            self.turn(player)
            print(self.board)
            if self.board.winner(player):
                print(player.name, "wins!")
                self.winner = True
                break
            player = self.next_up(player)

        if not self.winner:
            print("Tie game!")
        print("Nice game {} and {}!".format(self.player1.name, self.player2.name))

"""
Run game from the command line
"""
if __name__ == "__main__":
    g = Game()
    g.play()

