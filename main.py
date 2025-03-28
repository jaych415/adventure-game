from src.game_key_maker import GameKeyMaker
from src.player import Player
from src.dungeons.intro_dungeon import IntroDungeon

def main():
    game = GameKeyMaker(IntroDungeon, Player)
    game.turn()

if __name__ == "__main__":
    main()
