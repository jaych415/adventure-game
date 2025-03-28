from .utils import *

class TreeHollow:
    def __init__(self):
        self.room_items = []
        self.shovel_found = False
        self.combinator_dict = {
            frozenset(["shovel", "sprout"]): "planted tree"
        }

    def enter(self, game_key):
        slow_print("You arrive at a quiet tree hollow. It's peaceful here.")
        pause(1)

        while True:
            print("*** TREE HOLLOW MENU ***")
            print("1) Search area")
            print("2) Grab item")
            print("3) Check backpack")
            print("4) Combine items")
            print("5) Use item")
            print("6) Escape")
            choice = input("> ")

            if choice == "1":
                if not self.shovel_found:
                    slow_print("You dig around some roots and discover a rusty shovel.")
                    self.room_items.append("shovel")
                    self.shovel_found = True
                else:
                    slow_print("You've already searched the area. Nothing else is here.")

            elif choice == "2":
                if not self.room_items:
                    slow_print("There are no items to grab.")
                else:
                    slow_print("Items you can grab:")
                    for item in self.room_items:
                        slow_print(f"- {item}")
                    slow_print("What would you like to grab?")
                    item = input().lower()
                    if item in self.room_items:
                        self.room_items.remove(item)
                        game_key.player.add_to_backpack(item)
                    else:
                        slow_print("That item isn't here.")

            elif choice == "3":
                game_key.player.print_backpack()

            elif choice == "4":
                game_key.player.print_backpack()
                slow_print("Combine what first?")
                i1 = input().lower()
                slow_print("Combine with?")
                i2 = input().lower()
                key = frozenset([i1, i2])
                if key in self.combinator_dict:
                    result = self.combinator_dict[key]
                    if i1 in game_key.player.backpack and i2 in game_key.player.backpack:
                        game_key.player.remove_from_backpack(i1)
                        game_key.player.remove_from_backpack(i2)
                        game_key.player.add_to_backpack(result)
                        slow_print("You combined them and created: " + result)
                    else:
                        slow_print("You're missing something to complete the combination.")
                else:
                    slow_print("Those don't combine into anything useful.")

            elif choice == "5":
                slow_print("Which item do you want to use?")
                game_key.player.print_backpack()
                item = input().lower()
                if item in game_key.player.backpack:
                    slow_print("You use the " + item + ". Nothing major happens.")
                else:
                    slow_print("You don't have that.")

            elif choice == "6":
                if "planted tree" in game_key.player.backpack:
                    slow_print("The planted tree grows rapidly into a towering beanstalk. You climb to safety. You win!")
                    game_key.game_over = True
                    return None
                else:
                    slow_print("You can't escape yet. Maybe you need to grow something first?")

            else:
                slow_print("Choose a valid option.")
