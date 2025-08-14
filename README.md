# Alien Invasion – WIP 🚧
['hwip' - Stewie](https://www.youtube.com/watch?v=4F5FvUchhxQ&list=LL&index=1)

## Fonctionnalités terminées :
- Création d’un environnement virtuel
- Importation des modules nécessaires (`pygame`, `time`, `sprite`, `sys`)
- Création de la fenêtre de jeu
- Fermeture du jeu avec la touche Échap
- Affichage d’un alien au centre de l’écran (collisions non implémentées)
- Mouvements du vaisseau avec les touches fléchées (KEYDOWN / KEYUP pour un déplacement fluide)
- Limitation du vaisseau aux bords de l’écran
- Architecture modulaire (classes séparées dans plusieurs fichiers : `settings.py`, `ship.py`, `alien.py`, `home_screen.py`, `bullet.py`)
- Affichage d’un écran d’accueil pendant 3 secondes avant le démarrage
- Redimensionnement automatique de l’image de fond
- Système de tir (touche Espace) avec gestion de plusieurs balles via pygame.sprite.Group (plusieurs balles, suppression automatique)
- Affichage d'un écran de contrôle après l'écran d'accueil
- Son de fond (KAYTRANADA_SPACEINVADER.wav) (/!\ a changer pour des raisons de copyright)

## À faire :
- Détection des collisions entre balles et aliens
- Affichage du score
- Ajout d’un système de vies
- Apparition de plusieurs aliens
- Sons (tir, explosion, musique)


# Avant de lancer le jeu, active l'environnement virtuel :

Windows :
```
.\venv\Scripts\activate
```

Linux/macOS :
```
source venv/bin/activate
```

# Pour lancer le jeu :
```
python alien_invasion.py
```

# Installer un module :
```
pip install nom_du_module
```

# Installer Pygame :
```
pip install pygame
```

# Pour installer les dépendances nécessaires :

```
pip install -r requirements.txt
```