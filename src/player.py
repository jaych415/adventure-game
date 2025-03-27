### src/player.py
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

    def show_backpack(self):
        print("Backpack:")
        if not self.backpack:
            print(" - (empty)")
        else:
            for item in self.backpack:
                print(" -", item)

    def combine_items(self, item1, item2):
        combinations = {
            frozenset(["(s)eeds", "(w)ater"]): "watery seeds",
            frozenset(["(d)irt", "(w)ater"]): "mud",
            frozenset(["(d)irt", "(s)eeds"]): "sprout"
        }
        key = frozenset([item1, item2])
        if key in combinations:
            result = combinations[key]
            if item1 in self.backpack and item2 in self.backpack:
                self.remove_from_backpack(item1)
                self.remove_from_backpack(item2)
                self.add_to_backpack(result)
                print(f"You created a '{result}'!")
            else:
                print("You don't have both items.")
        else:
            print("Nothing happens.")

    def print_backpack(self):
        if not self.backpack:
            print("Your backpack is empty.")
        else:
            print("Your backpack contains:")
            for item in self.backpack:
                print("-", item)