class GameStats:
    def __init__(self, ai_game):
        """ Initialise les stats de la partie """
        self.settings = ai_game.settings # Récupère les paramètres du jeu
        self.reset_stats() # Initialise les statistiques qui peuvent changer durant la partie
    
    def reset_stats(self):
        """ Initialise les stats qui peuvent changer durant la partie """
        self.ships_left = self.settings.ship_limit # Nombre de vaisseaux (vies) que le joueur a au début de la partie
