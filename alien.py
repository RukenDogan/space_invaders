import pygame

class Alien:
    """Classe pour gérer les aliens dans le jeu"""
    def __init__(self, ai_game):
        """Initialiser l'alien et définir sa position de départ"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Charger l'image de l'alien et obtenir son rectangle
        self.image = pygame.image.load('images/alien.png')
        size = (self.settings.alien_width, self.settings.alien_height)
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()

        # Commencer chaque nouveau alien au centre de l'écran
        self.screen_rect = self.screen.get_rect()
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Dessiner l'alien à sa position actuelle"""
        self.screen.blit(self.image, self.rect)