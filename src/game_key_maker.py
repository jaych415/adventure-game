### src/game_key_maker.py
from .player import Player
from .dungeons.intro_dungeon import IntroDungeon
from .dungeons.tree_hollow import TreeHollow

class GameKeyMaker:
    def __init__(self):
        self.player = Player()
        self.game_over = False
        self.scenes = {
            "intro": IntroDungeon(),
            "tree hollow": TreeHollow()
        }
        self.current_scene = "intro"

    def start(self):
        print("🌳 Welcome to the Nature Escape Game 🌱")
        while not self.game_over:
            scene = self.scenes[self.current_scene]
            self.current_scene = scene.enter(self) or self.current_scene

    def change_scene(self, name):
        if name in self.scenes:
            self.current_scene = name
        else:
            print("That place doesn't exist.")