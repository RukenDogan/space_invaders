# Fichier avec le code qui utilise pygame pour charger, afficher, transformer des éléments graphiques et gérer les événements

import sys # Sert à accéder à des fonctions et objets système fournis par le module sys
import pygame # Importe la bibliothèque Pygame pour créer des jeux vidéo
import time # Importe le module time pour gérer le temps dans le jeu

from settings import Settings # Importe la classe Settings depuis le fichier settings.py
from ship import Ship # Importe la classe Ship depuis le fichier ship.py
from alien import Alien # Importe la classe Alien depuis le fichier alien.py
from home_screen import HomeScreen # Importe la classe HomeScreen depuis le fichier home_screen.py
from bullet import Bullet # Importe la classe Bullet depuis le fichier bullet.py

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
        self.bullets = pygame.sprite.Group() # Crée un groupe de sprites pour gérer les balles tirées par le vaisseau
        self.aliens = pygame.sprite.Group() # Crée un groupe de sprites pour gérer les aliens
        self._create_fleet() # Crée une flotte d'aliens
        self.home_screen = HomeScreen(self) # Crée une instance de la classe HomeScreen pour gérer l'écran d'accueil
        
        self.show_home_screen = True # Indique si l'écran d'accueil doit être affiché
        self.start_time = time.time() # Enregistre le temps de début pour gérer l'affichage de l'écran d'accueil

        self.home_bg = pygame.image.load('images/home_bg.jpg') # Charge l'image de fond de l'écran d'accueil
        self.home_bg = pygame.transform.scale(self.home_bg, (self.settings.screen_width, self.settings.screen_height)) # Ajuste la taille pour remplir l'écran

        self.controls_bg = pygame.image.load('images/controls_screen.png') # Charge l'image de fond de l'écran de contrôle
        self.controls_bg = pygame.transform.scale(self.controls_bg, (self.settings.screen_width, self.settings.screen_height)) # Ajuste la taille pour remplir l'écran
        self.show_controls_screen = False # Indique si l'écran de contrôle doit être affiché

        self.controls_sound = pygame.mixer.Sound("sounds/life_on_line.wav") # Son de fond du jeu
        self.controls_sound.set_volume(0.5) # Définit le volume du son de fond
        self.controls_music_playing = False # Indique si la musique de fond est en cours de lecture

        self.background_sound = pygame.mixer.Sound("sounds/KAYTRANADA_SPACEINVADER.wav") # Son de fond du jeu
        self.background_sound.set_volume(0.5) # Définit le volume du son de fond
        self.background_music_playing = False # Indique si la musique de fond est en cours de lecture



    def run_game(self):
        """Démarrer la boucle principale du jeu"""
        while True:
            self.check_events() # Vérifier les événements de l'utilisateur

            if self.show_home_screen:
                # Affiche l’écran d’accueil pendant 3 sec max
                if time.time() - self.start_time > 3: # Si l'écran d'accueil est affiché depuis plus de 3 secondes
                    self.show_home_screen = False # Ne pas afficher l'écran d'accueil
                    self.show_controls_screen = True # Affiche l'écran de contrôle après l'écran d'accueil
                self._update_home_screen() # Met à jour l'écran d'accueil pour afficher les éléments de l'écran d'accueil
                
            
            elif self.show_controls_screen: # Si l'écran de contrôle doit être affiché
                if not self.controls_music_playing: # Si la musique de contrôle n'est pas en cours de lecture
                    self.controls_sound.play(-1)  # Joue le son de contrôle en boucle infinie
                    self.controls_music_playing = True # Démarre la musique de contrôle
                self._update_controls_screen() # Met à jour l'écran de contrôle pour afficher les éléments de l'écran de contrôle
            
            else:
                if not self.background_music_playing: # Si la musique de fond n'est pas en cours de lecture 
                    self.controls_sound.stop() # arrête le son de contrôle
                    self.background_sound.fadeout(2000) # Arrête le son de fond avec un délai de 1 seconde
                    self.background_sound.play(-1, fade_ms=2000) # Joue le son de fond en boucle infinie avec un délai de 1 seconde
                    self.background_music_playing = True # Démarre la musique de fond
                self.ship.update() # Met à jour la position du vaisseau
                self._update_screen() # Met à jour l'écran pour afficher les éléments du jeu

            self._update_bullets() # Met à jour la position des tirs
            self.aliens.update() # Met à jour la position des aliens
            self.clock.tick(60) # Limite la boucle à 60 images par seconde

    def check_events(self):
            # Surveille les événements du clavier et de la souris
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.background_sound.stop() # Arrête le son de fond
                    sys.exit()

                elif event.type == pygame.KEYDOWN: # vérifie si une touche est enfoncée
                    if self.show_home_screen: # Si l'écran d'accueil est affiché
                        self.show_home_screen = False # Ne pas afficher l'écran d'accueil
                        self.show_controls_screen = True # Affiche l'écran de contrôle après l'écran d'accueil

                    elif self.show_controls_screen: # Si l'écran de contrôle est affiché
                        self.show_controls_screen = False # Ne pas afficher l'écran de contrôle

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
                    elif event.key == pygame.K_UP: # Si la touche flèche haut est enfoncée
                         self.ship.moving_up = True # Déplace le vaisseau vers le haut
                    elif event.key == pygame.K_DOWN: # Si la touche flèche bas est enfoncée
                        self.ship.moving_down = True # Déplace le vaisseau vers le bas

                    elif event.key == pygame.K_ESCAPE: # Si la touche Q est enfoncée
                        self.background_sound.stop() # Arrête le son de fond
                        pygame.quit() # Quitte Pygame
                        sys.exit() # Quitte le jeu
                        
                    elif event.key == pygame.K_SPACE: # Si la touche espace est enfoncée
                        self._fire_bullet() # Tire une balle depuis le vaisseau

    def _check_keyup_events(self, event):
                    """Réagit aux touches relâchées"""          
                    if event.key == pygame.K_RIGHT: # Si la touche flèche droite est relâchée
                         self.ship.moving_right = False # Déplace le vaisseau vers la droite
                    elif event.key == pygame.K_LEFT: # Si la touche flèche gauche est relâchée
                        self.ship.moving_left = False # Déplace le vaisseau vers la gauche
                    elif event.key == pygame.K_UP: # Si la touche flèche haut est relâchée
                        self.ship.moving_up = False # Déplace le vaisseau vers le haut
                    elif event.key == pygame.K_DOWN: # Si la touche flèche bas est relâchée
                        self.ship.moving_down = False # Déplace le vaisseau vers le bas
                    elif event.key == pygame.K_ESCAPE: # Si la touche Échap est enfoncée
                        sys.exit() # Quitte le jeu

    
    def _update_bullets(self):
        """Met à jour la position des tirs"""
        self.bullets.update() # Met à jour la position des tirs

        for bullet in self.bullets.copy(): # Parcourt les balles tirées par le vaisseau
            if bullet.rect.bottom <= 0: # Si la balle est en dehors de l'écran
                self.bullets.remove(bullet) # Supprime la balle
                # print(len(self.bullets)) # Affiche le nombre de balles restantes


    def _update_screen(self):
            """Met à jour l'écran et affiche les éléments du jeu"""        
            self.screen.blit(self.bg_image, (0, 0))  # Affiche l'image de fond en (0,0)
            for bullet in self.bullets.sprites(): # Dessine les bullets
                bullet.draw_bullet() # Dessine le bullet
            self.ship.blitme() # Dessine le vaisseau
            self.aliens.draw(self.screen) # Dessine les aliens à leur position actuelle
            pygame.display.flip() # Met à jour l'écran

    def _update_home_screen(self):
            """Met à jour l'écran d'accueil et affiche les éléments de l'écran d'accueil"""
            self.screen.blit(self.home_bg, (0, 0))  # Affiche l'image de fond en (0,0)
            self.home_screen.blitme() # Dessine l'écran d'accueil
            pygame.display.flip() # Met à jour l'écran pour afficher les éléments de l'écran d'accueil

    def _update_controls_screen(self):
            """Met à jour l'écran de contrôle et affiche les éléments de l'écran de contrôle"""
            self.screen.blit(self.controls_bg, (0, 0))  # Affiche l'image de fond en (0,0)
            pygame.display.flip() # Met à jour l'écran pour afficher les éléments de l'écran de contrôle
            
    def _fire_bullet(self):
        """Créer un nouveau tir et l'ajouter au groupe bullets"""
        if len(self.bullets) < self.settings.bullets_allowed: # Si le nombre de tirs est inférieur au nombre maximum autorisé
            new_bullet = Bullet(self)  # Crée un nouveau tir
            self.bullets.add(new_bullet)  # Ajoute le tir au groupe bullets

    def _create_fleet(self):
        """Créer une flotte d'aliens"""
        alien_width, alien_height = self.settings.alien_width, self.settings.alien_height # Récupère la largeur et la hauteur de l'alien à partir des paramètres du jeu (settings.py)

        current_x, current_y = alien_width, alien_height # Définir la position de départ de l'alien
        while current_y < (self.settings.screen_height - 3 * alien_height):
        # Tant que la position verticale (current_y) des aliens est inférieure à la hauteur totale de l'écran
        # moins trois fois la hauteur d'un alien, on peut encore placer une nouvelle rangée d'aliens.
        # => Cela empêche les aliens d'être générés trop bas (près du vaisseau du joueur).
            
            while current_x < (self.settings.screen_width - 2 * alien_width):
            # Tant que la position horizontale (current_x) est inférieure à la largeur de l'écran
            # moins deux fois la largeur d'un alien, on peut encore ajouter un nouvel alien sur la ligne courante.
            # => Cela évite que les aliens soient créés en dehors des bords droits de l'écran.    
                self._create_alien(current_x, current_y) # Crée un nouvel alien à la position actuelle
                current_x += 2 * alien_width # Déplace l'alien vers la droite

            current_x = alien_width # Réinitialise la position horizontale de l'alien
            current_y += 2 * alien_height # Déplace l'alien vers le bas

    def _create_alien(self, x_position, y_position):
        """Créer un nouvel alien à la position x_position, y_position"""
        new_alien = Alien(self) # Crée une nouvelle instance de la classe Alien
            
        new_alien.x = x_position # Défini la position de l'alien
        new_alien.y = y_position # Défini la position de l'alien
        new_alien.rect.x = x_position # Défini la position de l'alien
        new_alien.rect.y = y_position # Défini la position de l'alien
        self.aliens.add(new_alien) # Ajoute l'alien au groupe aliens



if __name__ == '__main__':
    # Crée une instance de jeu et exécute le jeu (la boucle principale)
    ai = AlienInvasion() # Crée une instance de la classe AlienInvasion
    ai.run_game() # Démarre la boucle principale du jeu
