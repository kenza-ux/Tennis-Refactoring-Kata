# -*- coding: utf-8 -*-
class Game2:
    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.score_player1 = 0
        self.score_player2 = 0


    def won_point(self, playerName):
        if playerName not in [self.player1Name, self.player2Name]:
            raise ValueError("Player name is not recognized")

        if playerName == self.player1Name:
            self.score_player1 += 1
        else:
            self.score_player2 += 1

    def score(self):
        if self.is_deuce():
            return "Deuce"
        if self.is_advantage():
            return f"Advantage {self.advantage_player()}"
        if self.is_win():
            return f"Win for {self.winning_player()}"
        return self.current_score()

    def is_deuce(self):
        return self.score_player1 > 2 and self.score_player1 == self.score_player2

    def is_advantage(self):
        return abs(self.score_player1 - self.score_player2) == 1 and max(self.score_player1, self.score_player2) > 3

    def is_win(self):
        return abs(self.score_player1 - self.score_player2) >= 2 and max(self.score_player1, self.score_player2) > 3

    def advantage_player(self):
        return self.player1Name if self.score_player1 > self.score_player2 else self.player2Name

    def winning_player(self):
        return self.player1Name if self.score_player1 > self.score_player2 else self.player2Name

    def current_score(self):
        score_names = ["Love", "Fifteen", "Thirty", "Forty"]
        score_p1 = score_names[min(self.score_player1, 3)]
        score_p2 = score_names[min(self.score_player2, 3)]
        if self.score_player1 == self.score_player2:
            return f"{score_p1}-All"
        return f"{score_p1}-{score_p2}"