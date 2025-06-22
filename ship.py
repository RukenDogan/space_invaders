import pygame

class Ship:
    """Classe pour gérer le vaisseau"""

    def __init__(self, ai_game):
        """Initialiser le vaisseau et définir sa position de départ"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Charger l'image du vaisseau et obtenir son rectangle
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()

        # Commencer chaque nouveau vaisseau au bas centrede l'écran
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Dessiner le vaisseau à sa position actuelle"""
        self.screen.blit(self.image, self.rect)