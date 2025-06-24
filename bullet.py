import pygame

class Bullet:
    """Classe pour gérer les tirs"""

    def __init__(self, ai_game):
        """Initialiser le tir et définir sa position de départ"""
        self.screen = ai_game.screen # Récupère l'écran du jeu
        self.settings = ai_game.settings # Récupère les paramètres du jeu
        self.screen_rect = ai_game.screen.get_rect() # Récupère le rectangle de l'écran du jeu

        self.image = pygame.image.load('images/bullet.png') # Charger l'image du tir depuis le fichier
        self.rect = self.image.get_rect() # Obtenir le rectangle de l'image du tir

        self.rect.midbottom = self.screen_rect.midbottom # Commencer chaque nouveau tir au bas centrede l'écran

        self.x = float(self.rect.x) # Stocker la position horizontale du tir en tant que valeur flottante

        self.moving_right = False # Définir le tir comme étant en mouvement vers la droite
        self.moving_left = False # Définir le tir comme étant en mouvement vers la gauche

    def update(self):
        """Mettre à jour le tir"""
        if self.moving_right and self.rect.right < self.screen_rect.right: # Si le tir est en mouvement vers la droite et qu'il est en dehors de l'écran
            self.x += self.settings.ship_speed # Déplacer le tir vers la droite
        if self.moving_left and self.rect.left > 0: # Si le tir est en mouvement vers la gauche et qu'il est à l'intérieur de l'écran
            self.x -= self.settings.ship_speed # Déplacer le tir vers la gauche

        self.rect.x = self.x # Mettre à jour la position du rectangle du tir avec la nouvelle position horizontale

    def blitme(self):
        """Dessiner le tir à sa position actuelle"""        
        self.screen.blit(self.image, self.rect) # Utiliser blit pour dessiner l'image du tir à sa position actuelle