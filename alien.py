import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Classe pour gérer les aliens dans le jeu"""

    def __init__(self, ai_game):
        """Initialiser l'alien et définir sa position de départ"""
        super().__init__() # Appelle le constructeur de la classe Sprite
        self.screen = ai_game.screen # Récupère l'écran du jeu
        self.settings = ai_game.settings # Récupère les paramètres du jeu
        self.screen_rect = ai_game.screen.get_rect() # Récupère le rectangle de l'écran du jeu

        self.image = pygame.image.load('images/alien.png') # Charge l'image de l'alien depuis le fichier
        self.image = pygame.transform.scale(self.image, (self.settings.alien_width, self.settings.alien_height)) # Redimensionne l'image de l'alien à la taille définie dans le fichier settings.py
        self.rect = self.image.get_rect() # Obtenir le rectangle de l'image de l'alien

        self.rect.x = self.rect.width # Positionne l'alien à la largeur de son rectangle
        self.rect.y = self.rect.height # Positionne l'alien à la hauteur de son rectangle

        self.x = float(self.rect.x) # Stocker la position horizontale de l'alien en tant que valeur flottante
        self.y = float(self.rect.y) # Stocker la position verticale de l'alien en tant que valeur flottante

    # def blitme(self):
    #     """Dessiner l'alien à sa position actuelle"""
    #     self.screen.blit(self.image, self.rect) # Utiliser blit pour dessiner l'image de l'alien à sa position actuelle