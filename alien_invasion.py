# Fichier avec le code qui utilise pygame pour charger, afficher, transformer des éléments graphiques et gérer les événements

import sys  # Sert à accéder à des fonctions et objets système fournis par le module sys
import pygame  # Importe la bibliothèque Pygame pour créer des jeux vidéo
import time  # Importe le module time pour gérer le temps dans le jeu

# Importe la classe Settings depuis le fichier settings.py
from settings import Settings
from ship import Ship  # Importe la classe Ship depuis le fichier ship.py
from alien import Alien  # Importe la classe Alien depuis le fichier alien.py
# Importe la classe HomeScreen depuis le fichier home_screen.py
from home_screen import HomeScreen
from bullet import Bullet  # Importe la classe Bullet depuis le fichier bullet.py
# Importe la fonction sleep depuis le module time pour faire des pauses dans le jeu
from time import sleep
# Importe la classe GameStats depuis le fichier game_stats.py
from game_stats import GameStats
from button import Button  # Importe la classe Button depuis le fichier button.py


class AlienInvasion:
    """Classe principale pour gérer les ressources et le comportement du jeu"""

    def __init__(self):
        """Initialiser le jeu et créer des ressources de jeu"""
        pygame.init()  # Initialise tous les modules Pygame nécessaires

        # Crée un objet pour contrôler la fréquence d'images du jeu
        self.clock = pygame.time.Clock()
        self.settings = Settings()  # Crée un objet pour gérer les paramètres du jeu

        self.screen = pygame.display.set_mode(
            (0, 0), pygame.FULLSCREEN)  # Définit la taille de l'écran
        # Récupère la largeur de l'écran
        self.settings.screen_width = self.screen.get_width()
        # Récupère la hauteur de l'écran
        self.settings.screen_height = self.screen.get_height()

        # Définit le titre de la fenêtre du jeu
        pygame.display.set_caption("Alien Invasion")

        self.bg_image = pygame.image.load(
            'images/bg.png')  # Charge l'image du background
        # Ajuste la taille pour remplir l'écran
        self.bg_image = pygame.transform.scale(
            self.bg_image, (self.settings.screen_width, self.settings.screen_height))

        # Crée une instance de la classe GameStats pour gérer les statistiques du jeu
        self.stats = GameStats(self)
        # Crée une instance de la classe Ship pour gérer le vaisseau spatial
        self.ship = Ship(self)
        # Crée un groupe de sprites pour gérer les balles tirées par le vaisseau
        self.bullets = pygame.sprite.Group()
        # Crée un groupe de sprites pour gérer les aliens
        self.aliens = pygame.sprite.Group()
        self._create_fleet()  # Crée une flotte d'aliens
        # Crée une instance de la classe HomeScreen pour gérer l'écran d'accueil
        self.home_screen = HomeScreen(self)
        self.show_home_screen = True  # Indique si l'écran d'accueil doit être affiché
        # Enregistre le temps de début pour gérer l'affichage de l'écran d'accueil
        self.start_time = time.time()

        # Charge l'image de fond de l'écran d'accueil
        self.home_bg = pygame.image.load('images/home_bg.jpg')
        # Ajuste la taille pour remplir l'écran
        self.home_bg = pygame.transform.scale(
            self.home_bg, (self.settings.screen_width, self.settings.screen_height))

        # Charge l'image de fond de l'écran de contrôle
        self.controls_bg = pygame.image.load('images/controls_screen.png')
        self.controls_bg = pygame.transform.scale(
            # Ajuste la taille pour remplir l'écran
            self.controls_bg, (self.settings.screen_width, self.settings.screen_height))
        # Indique si l'écran de contrôle doit être affiché
        self.show_controls_screen = False

        self.controls_sound = pygame.mixer.Sound(
            "sounds/life_on_line.wav")  # Son de fond du jeu
        self.controls_sound.set_volume(0.5)  # Définit le volume du son de fond
        # Indique si la musique de fond est en cours de lecture
        self.controls_music_playing = False

        self.background_sound = pygame.mixer.Sound(
            "sounds/KAYTRANADA_SPACEINVADER.wav")  # Son de fond du jeu
        # Définit le volume du son de fond
        self.background_sound.set_volume(0.5)
        # Indique si la musique de fond est en cours de lecture
        self.background_music_playing = False

        self.bulletshoot_sound = pygame.mixer.Sound(
            "sounds/shoot.wav")  # Son de tir du jeu
        # Définit le volume du son de tir
        self.bulletshoot_sound.set_volume(0.5)
        # Indique si la musique de tir est en cours de lecture
        self.bulletshoot_music_playing = False

        # Indique si le jeu est actif (en cours de jeu) ou non (écran d'accueil ou écran de contrôle)
        self.game_active = False

        # Crée un bouton de démarrage pour le jeu
        self.play_button = Button(self, "Play")

    def run_game(self):
        """Démarrer la boucle principale du jeu"""
        while True:
            self.check_events()  # Vérifier les événements de l'utilisateur

            if self.show_home_screen:
                # Affiche l’écran d’accueil pendant 3 sec max
                if time.time() - self.start_time > 3:  # Si l'écran d'accueil est affiché depuis plus de 3 secondes
                    self.show_home_screen = False  # Ne pas afficher l'écran d'accueil
                    # Affiche l'écran de contrôle après l'écran d'accueil
                    self.show_controls_screen = True
                # Met à jour l'écran d'accueil pour afficher les éléments de l'écran d'accueil
                self._update_home_screen()

            elif self.show_controls_screen:  # Si l'écran de contrôle doit être affiché
                if not self.controls_music_playing:  # Si la musique de contrôle n'est pas en cours de lecture
                    # Joue le son de contrôle en boucle infinie
                    self.controls_sound.play(-1)
                    self.controls_music_playing = True  # Démarre la musique de contrôle
                # Met à jour l'écran de contrôle pour afficher les éléments de l'écran de contrôle
                self._update_controls_screen()

            else:
                if not self.background_music_playing:  # Si la musique de fond n'est pas en cours de lecture
                    self.controls_sound.stop()  # arrête le son de contrôle
                    # Arrête le son de fond avec un délai de 1 seconde
                    self.background_sound.fadeout(2000)
                    # Joue le son de fond en boucle infinie avec un délai de 1 seconde
                    self.background_sound.play(-1, fade_ms=2000)
                    self.background_music_playing = True  # Démarre la musique de fond

                if self.game_active:
                    self.ship.update()  # Met à jour la position du vaisseau
                    self._update_bullets()  # Met à jour la position des tirs
                    self._update_aliens()  # Met à jour la position des aliens

                self._update_screen()  # Met à jour l'écran pour afficher les éléments du jeu

            self.clock.tick(60)  # Limite la boucle à 60 images par seconde

    def check_events(self):
        # Surveille les événements du clavier et de la souris
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.background_sound.stop()  # Arrête le son de fond
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:  # Vérifie si un bouton de la souris est enfoncé
                mouse_pos = pygame.mouse.get_pos()  # Récupère la position de la souris
                # Vérifie si le bouton de démarrage a été cliqué
                self._check_play_button(mouse_pos)

            elif event.type == pygame.KEYDOWN:  # vérifie si une touche est enfoncée
                if self.show_home_screen:  # Si l'écran d'accueil est affiché
                    self.show_home_screen = False  # Ne pas afficher l'écran d'accueil
                    # Affiche l'écran de contrôle après l'écran d'accueil
                    self.show_controls_screen = True

                elif self.show_controls_screen:  # Si l'écran de contrôle est affiché
                    self.show_controls_screen = False  # Ne pas afficher l'écran de contrôle

                else:
                    # Vérifie les événements clavier
                    self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:  # vérifie si une touche est relâchée
                # Vérifie les événements clavier
                self._check_keyup_events(event)

    def _check_play_button(self, mouse_pos):
        """Commence un nouveau jeu lorsque le joueur clique sur Play"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)  # Vérifie si le bouton de démarrage a été cliqué
        if button_clicked and not self.game_active:  # Si le bouton de démarrage a été cliqué et que le jeu n'est pas actif
            self.stats.reset_stats() # Réinitialise les statistiques du jeu
            self.bullets.empty()  # Supprime toutes les balles
            self._create_fleet() # crée une nouvelle flotte d'aliens
            self.ship.center_ship() # centre le vaisseau
            self.game_active = True  # Démarre le jeu

    def _check_keydown_events(self, event):
        """Réagit aux touches enfoncées"""
        if event.key == pygame.K_RIGHT:  # Si la touche flèche droite est enfoncée
            self.ship.moving_right = True  # Déplace le vaisseau vers la droite
        elif event.key == pygame.K_LEFT:  # Si la touche flèche gauche est enfoncée
            self.ship.moving_left = True  # Déplace le vaisseau vers la gauche
        elif event.key == pygame.K_UP:  # Si la touche flèche haut est enfoncée
            self.ship.moving_up = True  # Déplace le vaisseau vers le haut
        elif event.key == pygame.K_DOWN:  # Si la touche flèche bas est enfoncée
            self.ship.moving_down = True  # Déplace le vaisseau vers le bas

        elif event.key == pygame.K_ESCAPE:  # Si la touche Échap est enfoncée
            self.background_sound.stop()  # Arrête le son de fond
            pygame.quit()  # Quitte Pygame
            sys.exit()  # Quitte le jeu

        elif event.key == pygame.K_SPACE:  # Si la touche espace est enfoncée
            self._fire_bullet()  # Tire une balle depuis le vaisseau
            self.bulletshoot_sound.play()  # Joue le son de tir

    def _check_keyup_events(self, event):
        """Réagit aux touches relâchées"""
        if event.key == pygame.K_RIGHT:  # Si la touche flèche droite est relâchée
            self.ship.moving_right = False  # Déplace le vaisseau vers la droite
        elif event.key == pygame.K_LEFT:  # Si la touche flèche gauche est relâchée
            self.ship.moving_left = False  # Déplace le vaisseau vers la gauche
        elif event.key == pygame.K_UP:  # Si la touche flèche haut est relâchée
            self.ship.moving_up = False  # Déplace le vaisseau vers le haut
        elif event.key == pygame.K_DOWN:  # Si la touche flèche bas est relâchée
            self.ship.moving_down = False  # Déplace le vaisseau vers le bas
        elif event.key == pygame.K_ESCAPE:  # Si la touche Échap est enfoncée
            sys.exit()  # Quitte le jeu

    def _update_bullets(self):
        """Met à jour la position des tirs"""
        self.bullets.update()  # Met à jour la position des tirs

        for bullet in self.bullets.copy():  # Parcourt les balles tirées par le vaisseau
            if bullet.rect.bottom <= 0:  # Si la balle est en dehors de l'écran
                self.bullets.remove(bullet)  # Supprime la balle
                # print(len(self.bullets)) # Affiche le nombre de balles restantes
        # Vérifie les collisions entre les balles et les aliens
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)

    def _update_aliens(self):
        """Met à jour la position des aliens"""
        self._check_fleet_edges()  # Vérifie si des aliens ont atteint un bord
        self.aliens.update()  # Met à jour la position des aliens

        # Vérifie les collisions entre le vaisseau et les aliens
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            # Affiche un message si le vaisseau a été touché
            print("Le vaisseau a été touché !")
            self._ship_hit()  # Gère le vaisseau touché

        self._check_aliens_bottom()  # Vérifie si des aliens ont atteint le bas de l'écran

    def _ship_hit(self):
        """Vérifie si le vaisseau a été touché"""
        if self.stats.ships_left > 0:  # Si le nombre de vaisseaux restants est supérieur à 0
            self.stats.ships_left -= 1  # Décrémente le nombre de vaisseaux restants

            self.bullets.empty()  # Vide la liste des bullets
            self.aliens.empty()  # Vide la liste des aliens

            self._create_fleet()  # Crée une nouvelle flotte d'aliens
            self.ship.center_ship()  # Centre le vaisseau
            sleep(0.5)  # Pause de 0.5 seconde
        else:
            self.game_active = False  # Le jeu est terminé

    def _update_screen(self):
        """Met à jour l'écran et affiche les éléments du jeu"""
        self.screen.blit(self.bg_image, (0, 0)
                         )  # Affiche l'image de fond en (0,0)
        for bullet in self.bullets.sprites():  # Dessine les bullets
            bullet.draw_bullet()  # Dessine le bullet
        self.ship.blitme()  # Dessine le vaisseau
        # Dessine les aliens à leur position actuelle
        self.aliens.draw(self.screen)

        # Si le jeu n'est pas actif (écran d'accueil ou écran de contrôle)
        if not self.game_active:
            self.play_button.draw_button()  # Dessine le bouton de démarrage sur l'écran

        pygame.display.flip()  # Met à jour l'écran

    def _update_home_screen(self):
        """Met à jour l'écran d'accueil et affiche les éléments de l'écran d'accueil"""
        self.screen.blit(self.home_bg, (0, 0)
                         )  # Affiche l'image de fond en (0,0)
        self.home_screen.blitme()  # Dessine l'écran d'accueil
        # Met à jour l'écran pour afficher les éléments de l'écran d'accueil
        pygame.display.flip()

    def _update_controls_screen(self):
        """Met à jour l'écran de contrôle et affiche les éléments de l'écran de contrôle"""
        self.screen.blit(self.controls_bg, (0, 0)
                         )  # Affiche l'image de fond en (0,0)
        # Met à jour l'écran pour afficher les éléments de l'écran de contrôle
        pygame.display.flip()

    def _fire_bullet(self):
        """Créer un nouveau tir et l'ajouter au groupe bullets"""
        if len(self.bullets) < self.settings.bullets_allowed:  # Si le nombre de tirs est inférieur au nombre maximum autorisé
            new_bullet = Bullet(self)  # Crée un nouveau tir
            self.bullets.add(new_bullet)  # Ajoute le tir au groupe bullets

    def _create_fleet(self):
        """Créer une flotte d'aliens"""
        alien_width, alien_height = self.settings.alien_width, self.settings.alien_height  # Récupère la largeur et la hauteur de l'alien à partir des paramètres du jeu (settings.py)

        # Définir la position de départ de l'alien
        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 5 * alien_height):
            # Tant que la position verticale (current_y) des aliens est inférieure à la hauteur totale de l'écran
            # moins trois fois la hauteur d'un alien, on peut encore placer une nouvelle rangée d'aliens.
            # => Cela empêche les aliens d'être générés trop bas (près du vaisseau du joueur).

            while current_x < (self.settings.screen_width - 2 * alien_width):
                # Tant que la position horizontale (current_x) est inférieure à la largeur de l'écran
                # moins deux fois la largeur d'un alien, on peut encore ajouter un nouvel alien sur la ligne courante.
                # => Cela évite que les aliens soient créés en dehors des bords droits de l'écran.
                # Crée un nouvel alien à la position actuelle
                self._create_alien(current_x, current_y)
                current_x += 1.5 * alien_width  # Déplace l'alien vers la droite

            current_x = alien_width  # Réinitialise la position horizontale de l'alien
            current_y += 1.5 * alien_height  # Déplace l'alien vers le bas

    def _create_alien(self, x_position, y_position):
        """Créer un nouvel alien à la position x_position, y_position"""
        new_alien = Alien(
            self)  # Crée une nouvelle instance de la classe Alien

        new_alien.x = x_position  # Défini la position de l'alien
        new_alien.y = y_position  # Défini la position de l'alien
        new_alien.rect.x = x_position  # Défini la position de l'alien
        new_alien.rect.y = y_position  # Défini la position de l'alien
        self.aliens.add(new_alien)  # Ajoute l'alien au groupe aliens

    def _check_fleet_edges(self):
        """Réagit en fonction si des aliens ont atteint un bord"""
        for alien in self.aliens.sprites():  # Parcourt les aliens
            if alien.check_edges():  # Vérifie si l'alien est en dehors des bords de l'écran
                self._change_fleet_direction()  # Change la direction de la flotte d'aliens
                break  # Sort de la boucle pour ne pas continuer à parcourir les aliens

    def _change_fleet_direction(self):
        """Change la direction de la flotte d'aliens"""
        for alien in self.aliens.sprites():  # Parcourt les aliens
            # Déplace chaque alien vers le bas de la flotte
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1  # Inverse la direction de la flotte d'aliens

    def _check_aliens_bottom(self):
        """Vérifie si des aliens ont atteint le bas de l'écran"""
        for alien in self.aliens.sprites():  # Parcourt les aliens
            if alien.rect.bottom >= self.settings.screen_height:  # Si l'alien est en dehors du bas de l'écran
                self._ship_hit()  # Gère le vaisseau touché
                break  # Sort de la boucle pour ne pas continuer à parcourir les aliens


if __name__ == '__main__':
    # Crée une instance de jeu et exécute le jeu (la boucle principale)
    ai = AlienInvasion()  # Crée une instance de la classe AlienInvasion
    ai.run_game()  # Démarre la boucle principale du jeu
