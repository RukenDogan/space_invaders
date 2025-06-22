import sys # Sert à accéder à des fonctions et objets système fournis par le module sys

import pygame

from settings import Settings # Importe la classe Settings depuis le fichier settings.py
from ship import Ship # Importe la classe Ship depuis le fichier ship.py
from alien import Alien # Importe la classe Alien depuis le fichier alien.py

class AlienInvasion:
    """Classe principale pour gérer les ressources et le comportement du jeu"""

    def __init__(self):
        """Initialiser le jeu et créer des ressources de jeu"""
        pygame.init()

        self.clock = pygame.time.Clock() # Crée un objet pour contrôler la fréquence d'images du jeu
        self.settings = Settings() # Crée un objet pour gérer les paramètres du jeu

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height)) # Définit la taille de l'écran
        pygame.display.set_caption("Alien Invasion")

        self.bg_image = pygame.image.load('images/bg.png')  # Charge l'image du background
        self.bg_image = pygame.transform.scale(self.bg_image, (self.settings.screen_width, self.settings.screen_height))  # Ajuste la taille pour remplir l'écran

        self.ship = Ship(self) # Crée une instance de la classe Ship pour gérer le vaisseau spatial

        self.alien = Alien(self) # Crée une instance de la classe Alien pour gérer les aliens

        # self.aliens = [] # Liste pour stocker les aliens (actuellement vide)

    def run_game(self):
        """Démarrer la boucle principale du jeu"""
        while True:
            self.check_events() # Vérifier les événements de l'utilisateur
            self._update_screen() # Mettre à jour l'écran
            self.clock.tick(60) # Limite la boucle à 60 images par seconde

    def check_events(self):      
            # Surveille les événements du clavier et de la souris
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

    def _update_screen(self):
            """Met à jour l'écran et dessiner le vaisseau"""        
            self.screen.blit(self.bg_image, (0, 0))  # Affiche l'image de fond en (0,0)
            self.ship.blitme()                        # Dessine le vaisseau
            self.alien.blitme()                       # Dessine l'alien
            pygame.display.flip()                     # Met à jour l'écran
            
            # self.screen.fill(self.settings.bg_color) # Remplir l’écran avec la couleur de fond
            # self.ship.blitme() # Dessine le vaisseau à sa position actuelle

            # pygame.display.flip() # Afficher à l’écran ce qui vient d’être dessiné



if __name__ == '__main__':
    # Crée une instance de jeu et exécute le jeu (la boucle principale)
    ai = AlienInvasion()
    ai.run_game()

