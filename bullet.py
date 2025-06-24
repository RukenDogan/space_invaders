import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Classe pour gérer les tirs"""

    def __init__(self, ai_game):
        """Initialiser le tir et définir sa position de départ"""
        self.screen = ai_game.screen # Récupère l'écran du jeu
        self.settings = ai_game.settings # Récupère les paramètres du jeu
        self.color = self.settings.bullet.color() # Récupère la couleur du tir depuis les paramètres du jeu

        self.rect = pygame.Rect(0, 0, self.settings.bullet.width, 
            self.settings.bullet.height) # Crée un rectangle pour le tir
        self.rect.midtop = ai_game.ship.rect.midtop # Positionne le tir au-dessus du vaisseau
        self.y = float(self.rect.y) # Utilise un float pour une précision accrue lors du déplacement du tir
    def update(self):
        """Mettre à jour le tir"""

    def blitme(self):
        """Dessiner le tir à sa position actuelle"""        