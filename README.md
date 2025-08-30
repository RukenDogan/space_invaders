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
- Ajout d'un son de fond pour l'écran de jeu (KAYTRANADA_SPACEINVADER.wav) (/!\ a changer pour des raisons de copyright)
- Ajout d'un son pour l'écran de contrôle (life_on_line, produit par Gari Pi)
- Apparition d'une flotte d'aliens
- Détection des collisions entre balles et aliens

## À faire :
- Affichage du score
- Ajout d’un système de vies
- Sons (tir, explosion, musique)


## Inspiration et ressources :
- Python Crash Course - Eric Matthes
- https://www.pygame.org/docs/
- les images : https://opengameart.org/ et https://pixabay.com/
- les sons : https://www.freesound.org/ et https://opengameart.org
- le son de l'écran de contrôle : produit par Gari Pi https://spiceprogrammers.bandcamp.com/
- le son de fond : à venir



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