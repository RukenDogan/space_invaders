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


    def check_edges(self):
        """Retourne True si l'alien est en dehors des bords de l'écran"""
        screen_rect = self.screen.get_rect() # Obtenir le rectangle de l'écran
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0) # Vérifier si l'alien est en dehors des bords de l'écran à droite ou à gauche


    def update(self):
        """Déplacer l'alien vers la droite"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction # Déplacer l'alien vers la droite ou la gauche en fonction de la direction de la flotte d'aliens
        self.rect.x = self.x # Mettre à jour la position horizontale de l'alien

