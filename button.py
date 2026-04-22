import pygame.font

class Button:
    """Classe pour créer des boutons pour le jeu"""

    def __init__(self, ai_game, msg):
        """Initialiser les attributs du bouton"""
        self.screen = ai_game.screen # Récupère l'écran du jeu
        self.screen_rect = self.screen.get_rect() # Récupère le rectangle de l'écran du jeu

        # Définir les dimensions et les propriétés du bouton
        self.width, self.height = 200, 50 # Largeur et hauteur du bouton
        self.button_color = (0, 135, 0) # Couleur du bouton (vert)
        self.text_color = (255, 255, 255) # Couleur du texte (blanc)
        self.font = pygame.font.SysFont(None, 48) # Police de caractères pour le texte du bouton

        # Construire le rectangle du bouton et le centrer
        self.rect = pygame.Rect(0, 0, self.width, self.height) # Créer un rectangle pour le bouton
        self.rect.center = self.screen_rect.center # Centrer le rectangle du bouton sur l'écran

        # Préparer le message du bouton une seule fois
        self._prep_msg(msg) # Préparer le message à afficher sur le bouton

    def _prep_msg(self, msg):
        """Convertir msg en une image et la centrer sur le bouton"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color) # Convertir le message en une image
        self.msg_image_rect = self.msg_image.get_rect() # Obtenir le rectangle de l'image du message
        self.msg_image_rect.center = self.rect.center # Centrer l'image du message sur le rectangle du bouton