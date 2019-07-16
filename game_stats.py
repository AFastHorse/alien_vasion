import sys


class GameStats():

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
        self.high_score = 0
        try:
            with open('highestScore.txt', 'r') as f:
                score = f.readline()
                self.high_score = int(score)
        except:
            pass

    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
