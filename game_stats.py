class GameStats:
    def __init__(self, ai_game):
        """ Initialise les stats de la partie """
        self.settings = ai_game.settings
        self.reset_stats()
    
    def reset_stats(self):
        """ Initialise les stats qui peuvent changer durant la partie """
        self.ships_left = self.settings.ship_limit
