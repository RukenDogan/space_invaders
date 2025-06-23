import pygame

class Ship:
    """Classe pour gérer le vaisseau"""

    def __init__(self, ai_game):
        """Initialiser le vaisseau et définir sa position de départ"""
        self.screen = ai_game.screen # Récupère l'écran du jeu
        self.settings = ai_game.settings # Récupère les paramètres du jeu
        self.screen_rect = ai_game.screen.get_rect() # Récupère le rectangle de l'écran du jeu

        self.image = pygame.image.load('images/ship.png') # Charger l'image du vaisseau depuis le fichier
        self.rect = self.image.get_rect() # Obtenir le rectangle de l'image du vaisseau

        self.rect.midbottom = self.screen_rect.midbottom # Commencer chaque nouveau vaisseau au bas centrede l'écran

        self.x = float(self.rect.x) # Stocker la position horizontale du vaisseau en tant que valeur flottante

        self.moving_right = False # Définir le vaisseau comme étant en mouvement vers la droite
        self.moving_left = False # Définir le vaisseau comme étant en mouvement vers la gauche

    def update(self):
        """Mettre à jour le vaisseau"""
        if self.moving_right: # Si le vaisseau est en mouvement vers la droite
            self.x += self.settings.ship_speed # Déplacer le vaisseau vers la droite
        if self.moving_left: # Si le vaisseau est en mouvement vers la gauche
            self.x -= self.settings.ship_speed # Déplacer le vaisseau vers la gauche

        self.rect.x = self.x # Mettre à jour la position du rectangle du vaisseau avec la nouvelle position horizontale

    def blitme(self):
        """Dessiner le vaisseau à sa position actuelle"""
        self.screen.blit(self.image, self.rect) # Utiliser blit pour dessiner l'image du vaisseau à sa position actuelle