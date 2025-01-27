from Pocket import Pocket


class Board:
    def __init__(self):

        # Creating the pockets for the board
        pocket_a1 = Pocket("A1", "cup", "A", 4, 0, None)
        pocket_a2 = Pocket("A2", "cup", "A", 4, 1, None)
        pocket_a3 = Pocket("A3", "cup", "A", 4, 2, None)
        pocket_a4 = Pocket("A4", "cup", "A", 4, 3, None)
        pocket_a5 = Pocket("A5", "cup", "A", 4, 4, None)
        pocket_a6 = Pocket("A6", "cup", "A", 4, 5, None)

        store_a = Pocket("Store A", "store", "A", 0, 6, None)

        pocket_b1 = Pocket("B1", "cup", "B", 4, 7, None)
        pocket_b2 = Pocket("B2", "cup", "B", 4, 8, None)
        pocket_b3 = Pocket("B3", "cup", "B", 4, 9, None)
        pocket_b4 = Pocket("B4", "cup", "B", 4, 10, None)
        pocket_b5 = Pocket("B5", "cup", "B", 4, 11, None)
        pocket_b6 = Pocket("B6", "cup", "B", 4, 12, None)

        store_b = Pocket("Store B", "store", "B", 0, 13, None)

        # Setting up the opposite pockets
        pocket_a1.set_opposite_pocket(pocket_b6)
        pocket_a2.set_opposite_pocket(pocket_b5)
        pocket_a3.set_opposite_pocket(pocket_b4)
        pocket_a4.set_opposite_pocket(pocket_b3)
        pocket_a5.set_opposite_pocket(pocket_b2)
        pocket_a6.set_opposite_pocket(pocket_b1)
        store_a.set_opposite_pocket(store_b)
        pocket_b1.set_opposite_pocket(pocket_a6)
        pocket_b2.set_opposite_pocket(pocket_a5)
        pocket_b3.set_opposite_pocket(pocket_a4)
        pocket_b4.set_opposite_pocket(pocket_a3)
        pocket_b5.set_opposite_pocket(pocket_a2)
        pocket_b6.set_opposite_pocket(pocket_a1)
        store_b.set_opposite_pocket(store_a)

        # Now add the pockets to the board (counter-clockwise, following the direction of the stones)
        self.pockets = [pocket_a1, pocket_a2, pocket_a3, pocket_a4, pocket_a5, pocket_a6, store_a, pocket_b1, pocket_b2,
                      pocket_b3, pocket_b4, pocket_b5, pocket_b6, store_b]
        self.current_pocket = None
        self.size = len(self.pockets)

    def print_board(self):
        board = "                                          <-------------                                       \n"
        board += "                             "
        board += "| "
        for i in range(12, 6, -1):
            board += self.pockets[i].get_name()
            board += ": "
            board += str(self.pockets[i].get_count())
            board += " | "
        board += "\n| " + self.pockets[13].get_name() + ": " + str(self.pockets[13].get_count()) + " |"
        board += "                                                                               "
        board += "| " + self.pockets[6].get_name() + ": " + str(self.pockets[6].get_count()) + " |"
        board += "\n                             | "
        for i in range(0, 6):
            board += self.pockets[i].get_name()
            board += ": "
            board += str(self.pockets[i].get_count())
            board += " | "
        board += "\n"
        board += "                                         ------------->                                       \n"
        print(board)

    def get_pocket_from_name(self, pocket_name):
        for pocket in self.pockets:
            if pocket_name == pocket.get_name():
                return pocket
        return None

    def is_pocket_choice_valid(self, pocket_name, current_player_side):
        chosen_pocket = self.get_pocket_from_name(pocket_name)
        if chosen_pocket is not None:
            if chosen_pocket.get_type() == "store":
                print("Selecting a store is not allowed.")
                self.current_pocket = None
                return False
            elif chosen_pocket.get_owner() != current_player_side:
                print("You can only select pockets that you own.")
                self.current_pocket = None
                return False
            else:
                self.current_pocket = chosen_pocket
                return True
        else:
            print("That is not a valid pocket name.")
            return False


    def check_opposites(self, current_player, last_pocket):
        # Walk through the board
        if (self.pockets[last_pocket].get_count() == 1
                and current_player.pocket_belongs_to_player(self.pockets[last_pocket])
                and not self.pockets[last_pocket].is_store()):
            return True
        else:
            return False

    def free_turn_earned(self, last_pocket, opposite_store):
        if last_pocket == (opposite_store + 7) % self.size:
            return True
        else:
            return False

    def claim_opposite_stones(self, last_pocket, current_player):
        # If the current player ends their turn in an empty pocket they own
        if self.check_opposites(current_player, last_pocket):
            score = (self.pockets[last_pocket].get_count()
                     + self.pockets[last_pocket].get_opposite_pocket().get_count())
            self.pockets[current_player.store].set_count(self.pockets[current_player.store].get_count() + score)
            self.pockets[last_pocket].set_count(0)
            self.pockets[last_pocket].get_opposite_pocket().set_count(0)
            print("Congratulations! You\'ve added " + str(score) + " extra stone(s) to your store!")

    def execute_move(self, current_pocket, current_player):
        free_turn_earned = False
        if current_pocket is not None:
            number_of_stones = current_pocket.get_count()
            remaining__number_of_stones = number_of_stones
            current_pocket.set_count(0)
            start_pocket_index = current_pocket.place+1 # Start dropping stones in the next pocket
            this_pocket_index = start_pocket_index
            opposite_store_index = current_player.get_opposite_store() # To see which pocket we need to skip
            last_pocket = start_pocket_index # For the claim_opposite_stones and free_turn_earned functions

            # Put a stone in each next pocket until your hand is empty
            while remaining__number_of_stones > 0:
                # Don't drop a stone in the opponent's store, just skip it.
                if this_pocket_index == opposite_store_index:
                    this_pocket_index = (this_pocket_index + 1) % self.size
                    continue
                # Drop the stone and update position and hand
                else:
                    self.pockets[this_pocket_index % self.size].add_stones(1)
                    remaining__number_of_stones = remaining__number_of_stones - 1
                    last_pocket = this_pocket_index % self.size
                    this_pocket_index = (this_pocket_index + 1) % self.size

            # Tell the player what happened
            print(str(number_of_stones) + " stones moved from pocket " + current_pocket.get_name())

            # Check if you put the last stone into an empty pocket to earn a free turn
            free_turn_earned = self.free_turn_earned(last_pocket, opposite_store_index)

            # Take care of adding opposite stones to your store if you hava managed to claim any
            self.claim_opposite_stones(last_pocket, current_player)
        else:
            print("Error: No pocket is selected.")

        return free_turn_earned

    # Add the remaining stones on the side that still has them to the corresponding player's store
    def get_final_score(self, owner):
        count = 0
        if owner == "A":
            for pocket_index in range(0, 6):
                count += self.pockets[pocket_index].get_count()
                self.pockets[pocket_index].set_count(0)
            self.pockets[6].add_stones(count)
        elif owner == "B":
            for pocket_index in range(7, 13):
                count += self.pockets[pocket_index].get_count()
                self.pockets[pocket_index].set_count(0)
            self.pockets[13].add_stones(count)
        else:
            print("Error: That is not a valid pocket owner.")
