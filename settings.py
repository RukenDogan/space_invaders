class Settings:
    """Classe pour gérer les paramètres du jeu"""

    def __init__(self):
        """Initialiser les paramètres du jeu"""
        # Paramètres de l'écran
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # taille de l'alien
        self.alien_width = 60
        self.alien_height = 60