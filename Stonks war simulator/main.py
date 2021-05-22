"Fichier principale du jeu"
import pygame
from pygame.constants import MOUSEMOTION
from game import Game

# Initialisation
pygame.init()

# Fenêtre d'affichage
pygame.display.set_caption("Stonks industry")
screen = pygame.display.set_mode((1280, 720))
icon = pygame.image.load("assets/logo.png")
pygame.display.set_icon(icon)

# Charge le jeu
game = Game(screen)

# Définit que l'on est pas dans un champ de texte
game.active_J1 = False
game.active_J2 = False

# Permet de commencer à hover
start_hover = False

# Menu de départ
choice = "home"

# Boucle du principale du jeu
running = True
while running:

    # Raffraichie la fenêtre
    pygame.display.flip()

    # Raffraichie le jeu
    game.update()

    # Affiche le menu du jeu
    if choice == "home":
        game.display.menu()
        game.reset()

        # Définit les rectangles des boutons
        local_duel_button_rect = game.display.load_image_rect("assets/menu/home/button.png", 300, 40, 100, 466)
        about_us_button_rect = game.display.load_image_rect("assets/menu/home/button.png", 300, 40, 100, 516)
        exit_button_rect = game.display.load_image_rect("assets/menu/home/button.png", 300, 40, 100, 566)

    # Affiche la sélection des personnages
    if choice == "select":
        game.display.select()

        # Définit les rectangles des boutons
        return_button_rect = game.display.load_image_rect("assets/menu/select/return.png", 100, 50, 0, 0)
        avatar_1_button_rect = game.display.load_image_rect("assets/avatar/bitcoin/bitcoin.png", 310, 190, 20, 56)
        avatar_2_button_rect = game.display.load_image_rect("assets/avatar/dogecoin/dogecoin.png", 310, 190, 330, 56)
        avatar_3_button_rect = game.display.load_image_rect("assets/avatar/sushiswap/sushiswap.png", 310, 190, 640, 56)
        avatar_4_button_rect = game.display.load_image_rect("assets/avatar/dragonchain/dragonchain.png", 310, 190, 950, 56)
        avatar_5_button_rect = game.display.load_image_rect("assets/avatar/pancakebunny/pancakebunny.png", 310, 190, 20, 251)
        avatar_6_button_rect = game.display.load_image_rect("assets/avatar/pancakeswap/pancakeswap.png", 310, 190, 330, 251)
        avatar_7_button_rect = game.display.load_image_rect("assets/avatar/shiba inu/shiba inu.png", 310, 190, 640, 251)
        avatar_8_button_rect = game.display.load_image_rect("assets/avatar/uniswap/uniswap.png", 310, 190, 950, 251)
        name_J1_button_rect = game.display.load_image_rect("assets/menu/select/name_J1.png", 241, 42, 342, 619)
        name_J2_button_rect = game.display.load_image_rect("assets/menu/select/name_J2.png", 241, 42, 970, 619)
        start_duel_button_rect = game.display.load_image_rect("assets/menu/home/button.png", 379, 57, 450, 412)
        start_hover = True
    
    # Affiche le duel
    elif game.is_playing:
        game.display.duel()

        # Définit les rectangles des boutons
        word_1_button_rect = game.display.load_image_rect("assets/menu/home/button.png", 250, 40, 515, 150)
        word_2_button_rect = game.display.load_image_rect("assets/menu/home/button.png", 250, 40, 515, 210)
        word_3_button_rect = game.display.load_image_rect("assets/menu/home/button.png", 250, 40, 515, 270)
        word_4_button_rect = game.display.load_image_rect("assets/menu/home/button.png", 250, 40, 515, 330)
        word_5_button_rect = game.display.load_image_rect("assets/menu/home/button.png", 250, 40, 515, 390)
        word_6_button_rect = game.display.load_image_rect("assets/menu/home/button.png", 250, 40, 515, 450)
        word_7_button_rect = game.display.load_image_rect("assets/menu/home/button.png", 250, 40, 515, 510)
        word_8_button_rect = game.display.load_image_rect("assets/menu/home/button.png", 250, 40, 515, 570)
        bonus_word_1_button_rect = game.display.load_image_rect("assets/menu/home/button.png", 350, 40, 0, 650)
        bonus_word_2_button_rect = game.display.load_image_rect("assets/menu/home/button.png", 250, 40, 350, 650)
        bonus_word_3_button_rect = game.display.load_image_rect("assets/menu/home/button.png", 250, 40, 680, 650)
        bonus_word_4_button_rect = game.display.load_image_rect("assets/menu/home/button.png", 350, 40, 930, 650)
        finish_1_button_rect = game.display.load_image_rect("assets/menu/home/button.png", 75, 75, 0, 550)
        finish_2_button_rect = game.display.load_image_rect("assets/menu/home/button.png", 75, 75, 1205, 550)

    # Récupère les évènements
    for event in pygame.event.get():

        # Ferme la fenêtre lorsque l'on appuie sur la croix rouge
        if event.type == pygame.QUIT:
            running = False

        # Si une touche est appuyée, la met avec la valeur True dans un dictionnaire
        if event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            if choice == "select":

                # Permet de changer le pseudo du joueur 1
                if game.active_J1:
                    if event.key == pygame.K_RETURN:
                        game.active_J1 = False
                    elif game.pressed.get(pygame.K_BACKSPACE) and len(game.Player1.name) > 0:
                        game.Player1.name = game.Player1.name[:-1]
                    elif len(game.Player1.name) < 12:
                        game.Player1.name += event.unicode

                # Permet de change le pseudo du joueur 2
                if game.active_J2:
                    if event.key == pygame.K_RETURN:
                        game.active_J2 = False
                    elif game.pressed.get(pygame.K_BACKSPACE) and len(game.Player1.name) > 0:
                        game.Player2.name = game.Player2.name[:-1]
                    elif len(game.Player2.name) < 12:
                        game.Player2.name += event.unicode

            # Vérifie si la touche ECHAP est appuyé
            if game.pressed.get(pygame.K_ESCAPE):

                game.is_playing = False
                choice = "home"
                game.Player1.character = game.display.load_image_rect
                game.Player2.character = game.display.load_image_rect
                game.picking_phase = 1

        # Si une touche est relachée, la met avec la valeur False dans un dictionnaire
        if event.type == pygame.KEYUP:
            game.pressed[event.key] = False
        
        # Détecte le mouvement du curseur
        if event.type == pygame.MOUSEMOTION:

            # Vérifie si on est sur le menu de départ
            if choice == "home":

                # Vérifie si le curseur hover le bouton de duel local
                if local_duel_button_rect.collidepoint(event.pos):
                    game.display.menu_hover = 1

                # Vérifie si le curseur hover le bouton en savoir plus
                elif about_us_button_rect.collidepoint(event.pos):
                    game.display.menu_hover = 2

                # Vérifie si le curseur hover le bouton quitter
                elif exit_button_rect.collidepoint(event.pos):
                    game.display.menu_hover = 3

            # Vérifie si on est sur le menu de sélection des personnages
            elif choice == "select" and start_hover:

                # Vérifie si le curseur hover le personnage 1
                if avatar_1_button_rect.collidepoint(event.pos):
                    game.display.select_hover = 1

                # Vérifie si le curseur hover le personnage 2
                elif avatar_2_button_rect.collidepoint(event.pos):
                    game.display.select_hover = 2
                
                # Vérifie si le curseur hover le personnage 3
                elif avatar_3_button_rect.collidepoint(event.pos):
                    game.display.select_hover = 3
                
                # Vérifie si le curseur hover le personnage 4
                elif avatar_4_button_rect.collidepoint(event.pos):
                    game.display.select_hover = 4
                
                # Vérifie si le curseur hover le personnage 5
                elif avatar_5_button_rect.collidepoint(event.pos):
                    game.display.select_hover = 5
                
                # Vérifie si le curseur hover le personnage 6
                elif avatar_6_button_rect.collidepoint(event.pos):
                    game.display.select_hover = 6
                
                # Vérifie si le curseur hover le personnage 7
                elif avatar_7_button_rect.collidepoint(event.pos):
                    game.display.select_hover = 7
                
                # Vérifie si le curseur hover le personnage 8
                elif avatar_8_button_rect.collidepoint(event.pos):
                    game.display.select_hover = 8

        # Si le bouton entrer est appuyé
        if event.type == pygame.MOUSEBUTTONDOWN:

            # Vérifie si on est sur le menu de départ
            if choice == "home":

                # Vérifie si le bouton duel est cliqué
                if local_duel_button_rect.collidepoint(event.pos):
                    choice = "select"

                # Vérifie si le bouton en savoir plus est cliqué
                elif about_us_button_rect.collidepoint(event.pos):
                    choice = "about_us"
                    game.display.about_us()

                # Vérifie si le bouton quitter est cliqué
                elif exit_button_rect.collidepoint(event.pos):
                    running = False

            # Vérifie si on est sur en savoir plus
            elif choice == "about_us":
                choice = "home"

            # Vérifie si on est sur le menu de selection des personnages
            elif choice == "select":
  
                if not game.active_J1:

                    # Vérifie si le bouton du nom du joueur 1 est cliqué
                    if name_J1_button_rect.collidepoint(event.pos):
                        game.active_J1 = True

                else:
                    game.active_J1 = False

                if not game.active_J2:

                    # Vérifie si le bouton du nom du joueur 2 est cliqué
                    if name_J2_button_rect.collidepoint(event.pos):
                        game.active_J2 = True

                else:
                    game.active_J2 = False

                # Vérifie si le bouton de retour est cliqué
                if return_button_rect.collidepoint(event.pos):
                    if game.picking_phase == 1:
                        choice = "home"
                    
                    elif game.picking_phase == 2:
                        game.picking_phase = 1
                        game.Player1.change_character(None)

                elif game.picking_phase != 3:

                    # Vérifie si le bouton du personnage 1 est cliqué
                    if avatar_1_button_rect.collidepoint(event.pos):
                        game.choice = "BITCOIN"

                    # Vérifie si le bouton du personnage 2 est cliqué
                    elif avatar_2_button_rect.collidepoint(event.pos):
                        game.choice = "DOGECOIN"
                    
                    # Vérifie si le bouton du personnage 3 est cliqué
                    elif avatar_3_button_rect.collidepoint(event.pos):
                        game.choice = "SUSHISWAP"
                    
                    # Vérifie si le bouton du personnage 4 est cliqué
                    elif avatar_4_button_rect.collidepoint(event.pos):
                        game.choice = "DRAGONCHAIN"
                    
                    # Vérifie si le bouton du personnage 5 est cliqué
                    elif avatar_5_button_rect.collidepoint(event.pos):
                        game.choice = "PANCAKEBUNNY"
                    
                    # Vérifie si le bouton du personnage 6 est cliqué
                    elif avatar_6_button_rect.collidepoint(event.pos):
                        game.choice = "PANCAKESWAP"
                    
                    # Vérifie si le bouton du personnage 7 est cliqué
                    elif avatar_7_button_rect.collidepoint(event.pos):
                        game.choice = "SHIBA INU"
                    
                    # Vérifie si le bouton du personnage 8 est cliqué
                    elif avatar_8_button_rect.collidepoint(event.pos):
                        game.choice = "UNISWAP"

                else:
                    # Vérifie si le bouton de début du duel est cliqué
                    if start_duel_button_rect.collidepoint(event.pos):
                        choice = None
                        game.is_playing = True
                        game.words.generate()
                        game.words.reset_words()

                    else:
                        if not game.active_J1 and not game.active_J2:
                            game.picking_phase = 2
                            game.Player2.change_character(None)
        
            elif game.is_playing:
                # Vérifie si le bouton du mot numéro 1 est cliqué
                if word_1_button_rect.collidepoint(event.pos):
                    game.choice = game.words.word_1
                    game.words.word_1 = None

                # Vérifie si le bouton du mot numéro 2 est cliqué
                elif word_2_button_rect.collidepoint(event.pos):
                    game.choice = game.words.word_2
                    game.words.word_2 = None

                # Vérifie si le bouton du mot numéro 3 est cliqué
                elif word_3_button_rect.collidepoint(event.pos):
                    game.choice = game.words.word_3
                    game.words.word_3 = None

                # Vérifie si le bouton du mot numéro 4 est cliqué
                elif word_4_button_rect.collidepoint(event.pos):
                    game.choice = game.words.word_4
                    game.words.word_4 = None

                # Vérifie si le bouton du mot numéro 5 est cliqué
                elif word_5_button_rect.collidepoint(event.pos):
                    game.choice = game.words.word_5
                    game.words.word_5 = None

                # Vérifie si le bouton du mot numéro 6 est cliqué
                elif word_6_button_rect.collidepoint(event.pos):
                    game.choice = game.words.word_6
                    game.words.word_6 = None

                # Vérifie si le bouton du mot numéro 7 est cliqué
                elif word_7_button_rect.collidepoint(event.pos):
                    game.choice = game.words.word_7
                    game.words.word_7 = None

                # Vérifie si le bouton du mot numéro 8 est cliqué
                elif word_8_button_rect.collidepoint(event.pos):
                    game.choice = game.words.word_8
                    game.words.word_8 = None
                
                # Vérifie si le bouton du mot bonus numéro 1 est cliqué
                elif bonus_word_1_button_rect.collidepoint(event.pos):
                    game.choice = game.words.bonus_word_1
                    game.words.bonus_word_1 = None
                
                # Vérifie si le bouton du mot bonus numéro 2 est cliqué
                elif bonus_word_2_button_rect.collidepoint(event.pos):
                    game.choice = game.words.bonus_word_2
                    game.words.bonus_word_2 = None
                
                # Vérifie si le bouton du mot bonus numéro 3 est cliqué
                elif bonus_word_3_button_rect.collidepoint(event.pos):
                    game.choice = game.words.bonus_word_3
                    game.words.bonus_word_3 = None
                
                # Vérifie si le bouton du mot bonus numéro 4 est cliqué
                elif bonus_word_4_button_rect.collidepoint(event.pos):
                    game.choice = game.words.bonus_word_4
                    game.words.bonus_word_4 = None

                # Vérifie si le bouton de fin de phrase du joueur 1 est cliqué
                elif finish_1_button_rect.collidepoint(event.pos):
                    game.choice = "!"
                
                # Vérifie si le bouton de fin de phrase du joueur 2 est cliqué
                elif finish_2_button_rect.collidepoint(event.pos):
                    game.choice = "!"