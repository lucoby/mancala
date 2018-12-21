from Mancala import Mancala
from Human_Player import Human_Player
from MiniMaxPlayer import MiniMaxPlayer
from AlphaBetaPlayer import AlphaBetaPlayer


mancala = Mancala(Human_Player(), AlphaBetaPlayer(search_depth=12), starting_holes=6, verbose=True)
mancala.game_loop()
