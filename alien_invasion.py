# Fichier avec le code qui utilise pygame pour charger, afficher, transformer des éléments graphiques et gérer les événements

import sys # Sert à accéder à des fonctions et objets système fournis par le module sys
import pygame # Importe la bibliothèque Pygame pour créer des jeux vidéo
import time # Importe le module time pour gérer le temps dans le jeu

from settings import Settings # Importe la classe Settings depuis le fichier settings.py
from ship import Ship # Importe la classe Ship depuis le fichier ship.py
from alien import Alien # Importe la classe Alien depuis le fichier alien.py
from home_screen import HomeScreen # Importe la classe HomeScreen depuis le fichier home_screen.py


class AlienInvasion:
    """Classe principale pour gérer les ressources et le comportement du jeu"""

    def __init__(self):
        """Initialiser le jeu et créer des ressources de jeu"""
        pygame.init() # Initialise tous les modules Pygame nécessaires

        self.clock = pygame.time.Clock() # Crée un objet pour contrôler la fréquence d'images du jeu
        self.settings = Settings() # Crée un objet pour gérer les paramètres du jeu

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) # Définit la taille de l'écran
        self.settings.screen_width = self.screen.get_width() # Récupère la largeur de l'écran
        self.settings.screen_height = self.screen.get_height() # Récupère la hauteur de l'écran

        pygame.display.set_caption("Alien Invasion") # Définit le titre de la fenêtre du jeu

        self.bg_image = pygame.image.load('images/bg.png')  # Charge l'image du background
        self.bg_image = pygame.transform.scale(self.bg_image, (self.settings.screen_width, self.settings.screen_height))  # Ajuste la taille pour remplir l'écran

        self.ship = Ship(self) # Crée une instance de la classe Ship pour gérer le vaisseau spatial
        self.alien = Alien(self) # Crée une instance de la classe Alien pour gérer les aliens
        self.home_screen = HomeScreen(self) # Crée une instance de la classe HomeScreen pour gérer l'écran d'accueil
        
        self.show_home_screen = True # Indique si l'écran d'accueil doit être affiché
        self.start_time = time.time() # Enregistre le temps de début pour gérer l'affichage de l'écran d'accueil
        # self.aliens = [] # Liste pour stocker les aliens (actuellement vide)

        self.home_bg = pygame.image.load('images/home_bg.jpg')
        self.home_bg = pygame.transform.scale(self.home_bg, (self.settings.screen_width, self.settings.screen_height))


    def run_game(self):
        """Démarrer la boucle principale du jeu"""
        while True:
            self.check_events() # Vérifier les événements de l'utilisateur

            if self.show_home_screen:
                # Affiche l’écran d’accueil pendant 3 sec max
                if time.time() - self.start_time > 3:
                    self.show_home_screen = False
                self._update_home_screen()
            else:
                self.ship.update() # Met à jour la position du vaisseau
                self._update_screen() # Met à jour l'écran pour afficher les éléments du jeu

            self.clock.tick(60) # Limite la boucle à 60 images par seconde

    def check_events(self):      
            # Surveille les événements du clavier et de la souris
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.KEYDOWN: # vérifie si une touche est enfoncée
                    if self.show_home_screen: # Si l'écran d'accueil est affiché
                        self.show_home_screen = False # Ne pas afficher l'écran d'accueil
                    else:
                        self._check_keydown_events(event) # Vérifie les événements clavier
                elif event.type == pygame.KEYUP: # vérifie si une touche est relâchée
                    self._check_keyup_events(event) # Vérifie les événements clavier

    def _check_keydown_events(self, event):
                    """Réagit aux touches enfoncées""" 
                    if event.key == pygame.K_RIGHT: # Si la touche flèche droite est enfoncée
                        self.ship.moving_right = True # Déplace le vaisseau vers la droite
                    elif event.key == pygame.K_LEFT: # Si la touche flèche gauche est enfoncée
                        self.ship.moving_left = True # Déplace le vaisseau vers la gauche
                    elif event.key == pygame.K_q: # Si la touche Q est enfoncée
                        sys.exit() # Quitte le jeu

    def _check_keyup_events(self, event):
                    """Réagit aux touches relâchées"""          
                    if event.key == pygame.K_RIGHT: # Si la touche flèche droite est relâchée
                         self.ship.moving_right = False # Déplace le vaisseau vers la droite
                    elif event.key == pygame.K_LEFT: # Si la touche flèche gauche est relâchée
                        self.ship.moving_left = False # Déplace le vaisseau vers la gauche
                    elif event.key == pygame.K_ESCAPE: # Si la touche Échap est enfoncée
                        sys.exit() # Quitte le jeu

    def _update_screen(self):
            """Met à jour l'écran et affiche les éléments du jeu"""        
            self.screen.blit(self.bg_image, (0, 0))  # Affiche l'image de fond en (0,0)
            self.ship.blitme()                        # Dessine le vaisseau
            self.alien.blitme()                       # Dessine l'alien
            pygame.display.flip()                     # Met à jour l'écran

    def _update_home_screen(self):
            """Met à jour l'écran d'accueil et affiche les éléments de l'écran d'accueil"""
            self.screen.blit(self.home_bg, (0, 0))  # Affiche l'image de fond en (0,0)
            self.home_screen.blitme()                        # Dessine l'image de l'écran d'accueil
            pygame.display.flip()                     # Met à jour l'écran

if __name__ == '__main__':
    # Crée une instance de jeu et exécute le jeu (la boucle principale)
    ai = AlienInvasion() # Crée une instance de la classe AlienInvasion
    ai.run_game() # Démarre la boucle principale du jeu
