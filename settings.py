# Fichier pour définir les paramètres du jeu Alien Invasion (des constantes simples : tailles, vitesses, couleurs)

class Settings:
    """Classe pour gérer les paramètres du jeu"""

    def __init__(self):
        """Initialiser les paramètres du jeu"""
        # Paramètres de l'écran
        self.screen_width = 900 # Largeur de l'écran 900 pour 16:9
        self.screen_height = 600 # Hauteur de l'écran 600 pour 16:9
        # self.bg_color = (230, 230, 230)

        # taille de l'alien
        self.alien_width = 60
        self.alien_height = 60

        # Vitesse des aliens
        self.alien_speed = 1.0

        # Vitesse de la flotte d'aliens
        self.fleet_drop_speed = 10

        # Direction de la flotte d'aliens (1 = droite, -1 = gauche)
        self.fleet_direction = 1

        # Vitesse du vaisseau
        self.ship_speed = 2.5

        # Paramètres du tir
        self.bullet_speed = 2.0 # Vitesse du tir
        self.bullet_width = 5 # Largeur du tir (80 si image, pour height aussi)
        self.bullet_height = 15 # Hauteur du tir
        self.bullet_color = (255, 255, 255) # Couleur du tir
        self.bullets_allowed = 10 # Nombre maximum de tirs autorisés à l'écran