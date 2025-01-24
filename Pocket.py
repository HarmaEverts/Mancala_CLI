class Pocket:
    def __init__(self, name, pit_type, owner, count, place, opposite_pocket):
        self.name= name
        self.pit_type = pit_type
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

    def add_one_stone(self):
        self.count = self.count + 1

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
