import pygame

class Alien:
    """Classe pour gérer les aliens dans le jeu"""
    def __init__(self, ai_game):
        """Initialiser l'alien et définir sa position de départ"""
        self.screen = ai_game.screen # Récupère l'écran du jeu
        self.settings = ai_game.settings # Récupère les paramètres du jeu

        self.image = pygame.image.load('images/alien.png') # Charge l'image de l'alien depuis le fichier
        size = (self.settings.alien_width, self.settings.alien_height) # Obtenir la taille de l'image de l'alien (définie dans le fichier settings.py)
        self.image = pygame.transform.scale(self.image, size) # Redimensionne l'image de l'alien
        self.rect = self.image.get_rect() # Obtenir le rectangle de l'image de l'alien

        self.screen_rect = self.screen.get_rect() # Récupère le rectangle de l'écran du jeu
        self.rect.center = self.screen_rect.center # Définir la position de départ de l'alien au centre de l'écran

    def blitme(self):
        """Dessiner l'alien à sa position actuelle"""
        self.screen.blit(self.image, self.rect) # Utiliser blit pour dessiner l'image de l'alien à sa position actuelle