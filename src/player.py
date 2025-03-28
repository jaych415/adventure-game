class Player:
    def __init__(self):
        self.backpack = []

    def add_to_backpack(self, item):
        if item not in self.backpack:
            self.backpack.append(item)
            print(f"Added '{item}' to backpack.")
        else:
            print(f"'{item}' is already in your backpack.")

    def remove_from_backpack(self, item):
        if item in self.backpack:
            self.backpack.remove(item)
            print(f"Removed '{item}' from backpack.")

    def print_backpack(self):
        if not self.backpack:
            print("Your backpack is empty.")
        else:
            print("Your backpack contains:")
            for item in self.backpack:
                print("-", item)
