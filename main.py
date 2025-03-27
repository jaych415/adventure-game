### main.py
import os
import sys

project_root = os.path.dirname(os.path.abspath(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from src.game_key_maker import GameKeyMaker

def main():
    game = GameKeyMaker()
    game.start()

if __name__ == "__main__":
    main()
