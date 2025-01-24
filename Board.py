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


    def is_pocket_choice_valid(self, chosen_pocket):
        for pocket in self.pockets:
            if chosen_pocket == self.pockets[6].get_name() or chosen_pocket == self.pockets[13].name:
                print("Selecting a store is not allowed.")
                self.current_pocket = None
                return False
            else:
                if chosen_pocket == pocket.get_name():
                    self.current_pocket = pocket
                    return True
        self.current_pocket = None
        return False


    def check_opposites(self, current_player, last_pocket):
        # Walk through the board
        if (self.pockets[last_pocket].get_count() == 1
                and current_player.pocket_belongs_to_player(self.pockets[last_pocket])
                and not self.pockets[last_pocket].is_store()):
            return True
        else:
            return False


    def execute_move(self, current_pocket, current_player):
        # Do this differently.
        # Pick up the stones and drop them depending on the circumstances (own store or not).
        # This is too complex and also wrong.

        free_turn_earned = False
        if current_pocket is not None:
            number_of_stones = current_pocket.get_count()
            remaining_stones = number_of_stones
            current_pocket.set_count(0)
            start_pocket = current_pocket.place+1
            this_pocket = start_pocket
            opposite_store = current_player.get_opposite_store()

            last_pocket = start_pocket
            while remaining_stones > 0:
                if this_pocket == opposite_store: # Don't drop a stone in the opponent's store, just skip it.
                    this_pocket = (this_pocket + 1) % self.size
                    continue
                else:
                    self.pockets[this_pocket % self.size].add_stones(1)
                    remaining_stones = remaining_stones - 1
                    last_pocket = this_pocket % self.size
                    this_pocket = (this_pocket + 1) % self.size

            print(str(number_of_stones) + " stones moved from pocket " + current_pocket.get_name())

            # Check if you put the last stone into an empty pocket to earn a free turn
            if last_pocket == (opposite_store + 7) % self.size:
                free_turn_earned = True

            # If the current player ends their turn in an empty pocket they own
            if self.check_opposites(current_player, last_pocket):
                score = (self.pockets[last_pocket].get_count()
                         + self.pockets[last_pocket].get_opposite_pocket().get_count())
                self.pockets[current_player.store].set_count(self.pockets[current_player.store].get_count() + score)
                self.pockets[last_pocket].set_count(0)
                self.pockets[last_pocket].get_opposite_pocket().set_count(0)
                print("Congratulations! You\'ve added " + str(score) + " to your store!")

        return free_turn_earned

    # Add the remaining stones on the side that still has them to the corresponding player's store
    def count_side(self, owner):
        count = 0
        if owner == "A":
            for pocket in range(0, 6):
                count += self.pockets[pocket].get_count()
                self.pockets[pocket].set_count(0)
            self.pockets[6].add_stones(count)
        elif owner == "B":
            for pocket in range(7, 13):
                count += self.pockets[pocket].get_count()
                self.pockets[pocket].set_count(0)
            self.pockets[13].add_stones(count)
        else:
            print("That is not a valid pocket owner.")
