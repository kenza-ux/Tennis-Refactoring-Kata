# -*- coding: utf-8 -*-
#correction avec les améliorations apportées kenza Merzouk, Mohammed Daoud, Ahmed Bouzidia, Adam Achabar
from enum import Enum
class TennisGame2:
    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.score_player1 = 0
        self.score_player2 = 0

    def won_point(self, playerName):
        if playerName == "player1":
            self.score_player1 +=1
            
        elif playerName == "player2":
            self.score_player2 +=1
          
        else:
            print(" saisissez un nom de player correct")

    
    def score(self):

        if self.is_deuce():
            return "Deuce"
        if self.is_advantage():
            return f"Advantage {self.advantage_player()}"
        if self.is_win():
            return f"Win for {self.winning_player()}"
        return self.current_score()

    def is_deuce(self):
        return self.score_player1 >= 3 and self.score_player1 == self.score_player2

    def is_advantage(self):
        return self.score_player1 >= 4 or self.score_player2 >= 4 and abs(self.score_player1 - self.score_player2) == 1

    def is_win(self):
        return self.score_player1 >= 4 or self.score_player2 >= 4 and abs(self.score_player1 - self.score_player2) >= 2

    def advantage_player(self):
        return self.player1Name if self.score_player1 > self.score_player2 else self.player2Name

    def winning_player(self):
        return self.player1Name if self.score_player1 > self.score_player2 else self.player2Name

    def current_score(self):
        score_names = ["Love", "Fifteen", "Thirty", "Forty"]
        score_p1 = score_names[self.score_player1] if self.score_player1 < 4 else "Deuce"
        score_p2 = score_names[self.score_player2] if self.score_player2 < 4 else "Deuce"
        if self.score_player1 == self.score_player2:
            return f"{score_p1}-All" if self.score_player1 < 3 else "Deuce"
        return f"{score_p1}-{score_p2}"

    
    
