class Player:
    def __init__(self, name, store, opposite_store, side):
        self.name = name
        self.store = store
        self.opposite_store = opposite_store
        self.side = side

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_store(self):
        return self.store

    def set_store(self, store):
        self.store = store

    def get_opposite_store(self):
        return self.opposite_store

    def get_side(self):
        return self.side

    def pocket_belongs_to_player(self, pocket):
        if self.get_side() == pocket.get_owner():
            return True
        else:
            return False
