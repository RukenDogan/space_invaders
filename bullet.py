import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Classe pour gérer les tirs"""

    def __init__(self, ai_game):
        """Initialiser le tir et définir sa position de départ"""
        
        super().__init__() # Appelle le constructeur de la classe Sprite
        self.screen = ai_game.screen # Récupère l'écran du jeu
        self.settings = ai_game.settings # Récupère les paramètres du jeu
        self.color = self.settings.bullet_color # Récupère la couleur du tir depuis les paramètres du jeu

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height) # Crée un rectangle pour le tir avec la largeur et la hauteur définies dans les paramètres du jeu
        self.rect.midtop = ai_game.ship.rect.midtop # Positionne le tir au-dessus du vaisseau
        self.y = float(self.rect.y) # Utilise un float pour une précision accrue lors du déplacement du tir
    

    def update(self):
        """Mettre à jour le tir"""
        self.y -= self.settings.bullet_speed # Déplace le tir vers le haut
        self.rect.y = self.y

    def draw_bullet(self):
        """Dessiner le tir à sa position actuelle"""  
        pygame.draw.rect(self.screen, self.color, self.rect) # Dessine le tir