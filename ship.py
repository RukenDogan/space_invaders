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
        self.y = float(self.rect.y) # Stocker la position verticale du vaisseau en tant que valeur flottante

        self.moving_right = False # Définir le vaisseau comme étant en mouvement vers la droite
        self.moving_left = False # Définir le vaisseau comme étant en mouvement vers la gauche
        self.moving_up = False # Définir le vaisseau comme étant en mouvement vers le haut
        self.moving_down = False # Définir le vaisseau comme étant en mouvement vers le bas

        self.alive = True # Le vaisseau est vivant (pour pouvoir le faire disparaitre)
    


    def update(self):
        """Mettre à jour le vaisseau"""
        if self.moving_right and self.rect.right < self.screen_rect.right: # Si le vaisseau est en mouvement vers la droite et qu'il est en dehors de l'écran
            self.x += self.settings.ship_speed # Déplacer le vaisseau vers la droite
        if self.moving_left and self.rect.left > 0: # Si le vaisseau est en mouvement vers la gauche et qu'il est à l'intérieur de l'écran
            self.x -= self.settings.ship_speed # Déplacer le vaisseau vers la gauche
        if self.moving_up and self.rect.top > 0: # Si le vaisseau est en mouvement vers le haut et qu'il est à l'intérieur de l'écran
            self.y -= self.settings.ship_speed # Déplacer le vaisseau vers le haut
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom: # Si le vaisseau est en mouvement vers le bas et qu'il est en dehors de l'écran
            self.y += self.settings.ship_speed # Déplacer le vaisseau vers le bas

        self.rect.x = self.x # Mettre à jour la position du rectangle du vaisseau avec la nouvelle position horizontale
        self.rect.y = self.y # Mettre à jour la position du rectangle du vaisseau avec la nouvelle position verticale
        

    def blitme(self):
        """Dessiner le vaisseau à sa position actuelle"""
        self.screen.blit(self.image, self.rect) # Utiliser blit pour dessiner l'image du vaisseau à sa position actuelle