from Mancala import Mancala
from Human_Player import Human_Player
from MiniMaxPlayer import MiniMaxPlayer


mancala = Mancala(MiniMaxPlayer(), Human_Player(), starting_holes=6, verbose=True)
mancala.game_loop()
