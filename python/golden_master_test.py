import unittest

from tennis2 import TennisGame2
#from Tennis2_ameliore_E_G import TennisGame2
from game2 import Game2
class GoldenMasterTest(unittest.TestCase):

    DIR = "/Users/kenzamerzouk/PycharmProjects/Tennis-Refactoring-Kata/golden-master";

    @staticmethod
    def play_game(p1Points, p2Points, p1Name, p2Name):
        game = Game2(p1Name, p2Name)
        for i in range(max(p1Points, p2Points)):
            if i < p1Points:
                game.won_point(p1Name)
            if i < p2Points:
                game.won_point(p2Name)
        return game.score()

    def make_file_name(self, score_player_1, score_player_2):
        return f"{self.DIR}//{score_player_1}_{score_player_2}.txt"

    def _test_record(self):
        for score_player_1 in list(range(0, 16)):
            for score_player_2 in list(range(0, 16)):
                with self.subTest(f"{score_player_1}, {score_player_2}"):
                    sortie = self.play_game(score_player_1, score_player_2, "player1", "player2")
                    file = open(self.make_file_name(score_player_1, score_player_2), "w")
                    file.writelines(sortie)
                    file.close()

    def test_replay(self):
        for score_player_1 in list(range(0, 16)):
            for score_player_2 in list(range(0, 16)):
                with self.subTest(f"{score_player_1}, {score_player_2}"):
                    sortie = self.play_game(score_player_1, score_player_2, "player1", "player2")
                    file = open(self.make_file_name(score_player_1, score_player_2), "r")
                    attendu = file.read()
                    file.close()
                    self.assertEqual(attendu, sortie)


    unittest.main(argv=[''], exit=False)

