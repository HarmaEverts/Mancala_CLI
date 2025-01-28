from Game import Game


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
    new_game = input("Would you like to play again? (y/n) ")
    if new_game == "y":
        start_game()
    else:
        print("Thanks for playing!")


# Display the game rules.
def print_rules():
    print(
        "-------------------------------------------------------------------------------------------------------------"
        "-----------------------")
    print("The Mancala board is made up of two rows of six holes, or pockets, each. "
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
        print("Thanks for playing. Goodbye!\nThis game was written by Harma Everts, inspired by Mattchu Picchu.")
        exit_game = True
    else:
        print("That is not a valid option. Please choose 1, 2, or 3.")
