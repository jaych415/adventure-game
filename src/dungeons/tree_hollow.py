### src/dungeons/tree_hollow.py
from .utils import *

class TreeHollow:
    def enter(self, game_key):
        slow_print("You arrive at a quiet tree hollow. It's peaceful here.")
        if "sprout" in game_key.player.backpack:
            slow_print("A soft patch of soil seems perfect for planting something...")
            slow_print("Plant the sprout? (yes/no)")
            if input().lower() == "yes":
                slow_print("The sprout grows rapidly into a magical vine! You climb it and escape!")
                game_key.game_over = True
                return None
        else:
            slow_print("It feels like you're missing something important.")
        return "intro"