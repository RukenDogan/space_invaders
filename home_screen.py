import pygame

class HomeScreen:
    """Classe pour gérer l'écran de démarrage du jeu"""

    def __init__(self, ai_game):
        self.screen = ai_game.screen # Récupère l'écran du jeu
        self.settings = ai_game.settings # Récupère les paramètres du jeu
        self.screen_rect = ai_game.screen.get_rect() # Récupère le rectangle de l'écran

        self.image = pygame.image.load('images/home_screen.png') # Charge l'image de l'écran d'accueil
        self.rect = self.image.get_rect() # Récupère le rectangle de l'image

        # Centrer l'image de l'écran d'accueil au milieu de l'écran
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Dessiner l'écran de démarrage"""
        self.screen.blit(self.image, self.rect) # Affiche l'image de l'écran d'accueil à la position définie par self.rect

    def center_home_screen(self):
        """Recentrer si besoin"""
        self.rect.center = self.screen_rect.center # Recentre l'image de l'écran d'accueil au milieu de l'écran

    def reset_position(self):
        """Alias pour recentrer"""
        self.center_home_screen() # Permet de recentrer l'écran d'accueil si nécessaire
