class Pocket:
    def __init__(self, name, pocket_type, owner, count, place, opposite_pocket):
        self.name= name
        self.pocket_type = pocket_type
        self.owner = owner
        self.count = count
        self.place = place
        self.opposite_pocket = opposite_pocket

    # Helper functions to manage the cup counts and cup owners
    def get_owner(self):
        return self.owner

    def set_owner(self, player):
        self.owner = player

    def get_count(self):
        return self.count

    def set_count(self, new_count):
        self.count = new_count

    def add_stones(self, no_of_stones):
        self.count = self.count + no_of_stones

    def get_type(self):
        return self.pocket_type

    def set_type(self, pocket_type):
        self.pocket_type = pocket_type

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_opposite_pocket(self):
        return self.opposite_pocket

    def set_opposite_pocket(self, pocket):
        self.opposite_pocket = pocket

    def is_store(self):
        if self.place == 6 or self.place == 13:
            return True
        else:
            return False

    def is_valid_pocket(self, current_player):
        if current_player.get_side == self.owner:
            return True
        else:
            print("You cannot select an opponent\'s pocket. Please choose again.")
            return False
