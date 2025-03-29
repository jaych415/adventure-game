from .utils import *

class IntroDungeon:
    def __init__(self):
        self.room_items = ["(s)eeds", "(d)irt", "(w)ater"]
        self.combinator_dict = {
            frozenset(["(d)irt", "(w)ater"]): "mud",
            frozenset(["(d)irt", "(s)eeds"]): "sprout",
            frozenset(["(s)eeds", "(w)ater"]): "watery seeds"
        }

    def enter(self, game_key):
        slow_print("You awaken on a riverbank...")
        pause(2)
        slow_print("You have no idea how you got here.")
        pause(2)

        while True:
            print("*** MENU ***")
            print("1) Search area")
            print("2) Grab item")
            print("3) Combine items")
            print("4) Use item")
            action = input("> ")

            if action == '1':
                slow_print("You see some (s)eeds, a pile of (d)irt, and a pail of (w)ater.")

            elif action == '2':
                slow_print("What would you like to grab? (s/w/d)")
                item = input().lower()
                name_map = {"s": "(s)eeds", "w": "(w)ater", "d": "(d)irt"}
                name = name_map.get(item)
                if name and name in self.room_items:
                    self.room_items.remove(name)
                    game_key.player.add_to_backpack(name)
                else:
                    slow_print("That item isn't here.")

            elif action == '3':
                game_key.player.print_backpack()
                slow_print("Combine what first? (s/w/d or full name)")
                name_map = {"s": "(s)eeds", "w": "(w)ater", "d": "(d)irt"}
                i1_key = input().lower()
                slow_print("Combine with? (s/w/d or full name)")
                i2_key = input().lower()

                i1 = name_map.get(i1_key, i1_key)
                i2 = name_map.get(i2_key, i2_key)

                key = frozenset([i1, i2])
                if key in self.combinator_dict:
                    result = self.combinator_dict[key]
                    if i1 in game_key.player.backpack and i2 in game_key.player.backpack:
                        game_key.player.remove_from_backpack(i1)
                        game_key.player.remove_from_backpack(i2)
                        game_key.player.add_to_backpack(result)
                        slow_print("You created: " + result)

                        if result == "sprout":
                            slow_print("A magical wind blows... you feel drawn toward a nearby tree hollow.")
                            return "tree hollow"
                    else:
                        slow_print("You're missing something.")
                else:
                    slow_print("That didn't work.")

            elif action == '4':
                slow_print("What would you like to use?")
                game_key.player.print_backpack()
                item = input().lower()
                if item in game_key.player.backpack:
                    slow_print("You use the " + item + ". Nothing major happens.")
                else:
                    slow_print("You don't have that.")
