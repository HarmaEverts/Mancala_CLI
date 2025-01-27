from Board import Board
from Player import Player


class Game:
    def __init__(self):
        # Keep track of whether someone has won.
        self.victory = False

        # Create (default) players.
        self.player_a = Player("Player A", 6, 13, "A")
        self.player_b = Player("Player B", 13, 6, "B")

        # Set the first turn to player A.
        self.current_player = self.player_a

        # Keep track of whether the player gets a free turn.
        self.free_turn_earned = False

        # Create the game board.
        self.board = Board()

        # Set initial stone count
        self.player_a_zone_count = 0
        self.player_b_zone_count = 0
        self.count_stones_per_side()

    # Setting up the players
    def setup_player_names(self):
        name_a = input("What is player A's name? ")
        name_b = input("What is player B's name? ")

        self.player_a.set_name(name_a)
        self.player_b.set_name(name_b)
        self.board.pockets[6].set_name("Store " + self.player_a.get_name())
        self.board.pockets[13].set_name("Store " + self.player_b.get_name())

    # Helper function to see whose turn it is
    # It returns the player object whose turn it is (and shows a phrase on the screen)
    def whose_turn(self):
        return self.current_player

    # Call this function to set the turn to the next player
    def change_turn(self):
        if self.free_turn_earned:  # Don't change turn!
            return
        elif self.current_player == self.player_a:
            self.current_player = self.player_b
        elif self.current_player == self.player_b:
            self.current_player = self.player_a
        else:
            print("Something went horrible wrong... no current player selected.")

    def count_stones_per_side(self):
        self.player_a_zone_count = 0
        self.player_b_zone_count = 0
        for pocket in range(0, 6):
            self.player_a_zone_count += self.board.pockets[pocket].get_count()
        for pocket in range(7, 13):
            self.player_b_zone_count += self.board.pockets[pocket].get_count()

    # Check if the winning condition has been met (one of the rows of pockets is empty)
    def check_for_victory(self):
        self.count_stones_per_side()
        if self.player_b_zone_count == 0 and self.player_a_zone_count != 0:
            self.board.get_final_score("A")
            self.victory = True
        elif self.player_a_zone_count == 0 and self.player_b_zone_count != 0:
            self.board.get_final_score("B")
            self.victory = True
        else:
            self.victory = False

        return self.victory

    # Play a turn and see if the player gets another turn or not.
    def play_turn(self):
        selection = self.choose_pocket()
        self.free_turn_earned = self.board.execute_move(selection, self.current_player)
        if self.free_turn_earned:
            print("Congratulations, you have earned a free turn, " + self.current_player.get_name() + "!")

    # Choose which pocket to play
    def choose_pocket(self):
        valid_choice = False
        while not valid_choice:
            chosen_pocket = input("Which pocket do you want to pick, " + self.current_player.get_name() + "? ")
            valid_choice = self.board.is_pocket_choice_valid(chosen_pocket)
        return self.board.current_pocket

    # Determine which player has won, whether it was a tie, and what the final scores are.
    def declare_winner(self):
        print("The game has finished!")
        if self.board.pockets[6].get_count() > self.board.pockets[13].get_count():
            print("The winner is " + self.player_a.get_name())
        elif self.board.pockets[6].get_count() == self.board.pockets[13].get_count():
            print("The game ended in a tie!")
        elif self.board.pockets[6].get_count() < self.board.pockets[13].get_count():
            print("The winner is " + self.player_b.get_name())
        else:
            print("Something went wrong.")
        print("Final score: " + self.player_a.get_name() + ": "
              + str(self.board.pockets[6].get_count()) + " - "
              + self.player_b.get_name() + ": "
              + str(self.board.pockets[13].get_count()))

    # Print the current score.
    def print_current_score(self):
        print("Current score: " + self.player_a.get_name() + ": "
              + str(self.board.pockets[6].get_count()) + " - "
              + self.player_b.get_name() + ": "
              + str(self.board.pockets[13].get_count()))


# Manage the game loop
def start_game():
    # Game loop
    game = Game()
    game.setup_player_names()
    winner = False  # The game ends when there is a winner
    while not winner:
        game.print_current_score()
        game.board.print_board()
        game.play_turn()
        if game.check_for_victory():
            winner = True
        game.change_turn()

    game.board.print_board()
    game.declare_winner()
    new_game = input("Would you like to play again? (yes/no)")
    if new_game == "yes":
        start_game()
    else:
        print("Thanks for playing!")


# Display the game rules.
def print_rules():
    print(
        "-------------------------------------------------------------------------------------------------------------"
        "-----------------------")
    print("The Mancala 'board' is made up of two rows of six holes, or pits, each. "
          "Next, four pieces -- marbles or stones -- are placed in each of the 12 holes. "
          "The color of the pieces is irrelevant.")
    print(
        "Each player has a 'store' to the side of the Mancala board. The number of stones in your store is your score.")
    print("The game begins with one player picking up all of the pieces in any one of the holes on his side. "
          "Moving counter-clockwise, the player deposits one of the stones in each hole until the stones run out.")
    print("1. If you run into your own store, deposit one piece in it. If you run into your opponent's store, skip it.")
    print("2. If the last piece you drop is in your own store, you get a free turn.")
    print(
        "3. If the last piece you drop is in an empty hole on your side, "
        "you capture that piece and any pieces in the hole directly opposite.")
    print("4. Always place all captured pieces in your store.")
    print("The game ends when all six spaces on one side of the Mancala board are empty. "
          "The player who still has pieces on his side of the board when the game ends captures all of those pieces. "
          "Count all the pieces in each store. The winner is the player with the most pieces.")
    print(
        "-------------------------------------------------------------------------------------------------------------"
        "-----------------------")


# Kick off the game menu.
print("Welcome to the Mancala game!")
exit_game = False
while not exit_game:
    print("1. Read the rules of Mancala.")
    print("2. Play Mancala.")
    print("3. Exit.")
    choice = input("Please choose an option: ")
    if int(choice) == 1:
        print_rules()
    elif int(choice) == 2:
        start_game()
    elif int(choice) == 3:
        print("Goodbye!")
        exit_game = True
    else:
        print("That is not a valid option. Please choose 1, 2, or 3.")
