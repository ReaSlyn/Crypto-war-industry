"Fichier pour les fonctions d'affichage"
import pygame

class Display():
    """ Définit l'affichage des textures """
    def __init__(self, game, screen):
        self.game = game
        self.screen = screen

        # Définit les couleurs
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.red = (255, 0, 0)
        self.blue = (0, 0, 255)
        self.green = (111, 210, 100)

        self.menu_hover = 0
        self.select_hover = 0

    def text_objects(self, text, font, color):
        """ Renvoie un texte sur une surface et ses coordonnées """
        text_surface = font.render(text, True, color)
        return text_surface, text_surface.get_rect()

    def message_display(self, text, size, x, y, color, style="regular"):
        """ Affiche le message 'text' en 'x' et 'y' """
        myriad = pygame.font.Font(f"assets/font/myriad_{style}.ttf", size)
        text_surf, text_rect = self.text_objects(text, myriad, color)
        text_rect.x, text_rect.y = (x,y)
        self.screen.blit(text_surf, text_rect)

    def message_display_right(self, text, size, x, y, color, style="regular"):
        """ Affiche le message 'text' avec pour droite 'x' et 'y' """
        myriad = pygame.font.Font(f"assets/font/myriad_{style}.ttf", size)
        text_surf, text_rect = self.text_objects(text, myriad, color)
        text_rect.topright = (x, y)
        self.screen.blit(text_surf, text_rect)

    def message_display_center(self, text, size, x, y, color, y_offset = 0, style="regular"):
        """ Affiche le message 'text' avec pour centre 'x' et 'y' """
        myriad = pygame.font.Font(f"assets/font/myriad_{style}.ttf", size)
        text_surf, text_rect = self.text_objects(text, myriad, color)
        text_rect.center = (x,y + y_offset)
        self.screen.blit(text_surf, text_rect)

    def load_image(self, image_path, dim_x, dim_y):
        """ Affiche une image provenant de 'image_path' aux dimensions 'dim_x', 'dim_y' """
        image = pygame.image.load(image_path)
        image = pygame.transform.scale(image, (dim_x, dim_y))
        return image

    def load_image_position(self, image_path, dim_x, dim_y, x, y):
        """ Affiche une image provenant de 'image_path' aux dimensions 'dim_x', 'dim_y' en 'x','y' """
        image = self.load_image(image_path, dim_x, dim_y)
        self.screen.blit(image, (x, y))

    def load_image_rect(self, image_path, dim_x, dim_y, x, y):
        """ Permet d'avoir le rectangle de l'image provenant de 'image_path' aux dimensions 'dim_x', 'dim_y' en 'x','y' """
        image = self.load_image(image_path, dim_x, dim_y)
        image = pygame.transform.scale(image, (dim_x, dim_y))
        image_rect = image.get_rect()
        image_rect.x = x
        image_rect.y = y
        return image_rect

    def menu(self):
        """ Affiche le menu """
        self.load_image_position("assets/menu/home/fill.jpeg", 1280, 720, 0, 0)
        self.message_display("Stonks War Simulator", 48, 700, 100, self.white, "bold")
        if self.menu_hover == 1:
            self.message_display("LOCAL DUEL", 24, 120, 478, self.white, "bold")
        else:
            self.message_display("LOCAL DUEL", 24, 120, 478, self.black, "bold")
        if self.menu_hover == 2:
            self.message_display("ABOUT US", 24, 120, 528, self.white, "bold")
        else:
            self.message_display("ABOUT US", 24, 120, 528, self.black, "bold")
        if self.menu_hover == 3:
            self.message_display("QUIT", 24, 120, 578, self.white, "bold")
        else:
            self.message_display("QUIT", 24, 120, 578, self.black, "bold")
        self.message_display("Stonks War Simulator", 48, 700, 100, self.black, "bold")

    def about_us(self):
        """ Affiche les informations du jeu """
        self.load_image_position("assets/menu/home/background_menu.png", 427, 540, 426, 100)
        self.message_display_center("Stonks War Simulator", 30, 640, 150, self.white, 0,"bold")
        self.message_display("Thanh-Long Pham / Romain Monfret", 24, 450, 210, self.white)
        self.message_display("This game is the result of the project", 24, 440, 275, self.white)
        self.message_display("given by Mr. Loïc Janin in H1 in our", 24, 440, 305, self.white)
        self.message_display("course of programming. We have been", 24, 440, 335, self.white)
        self.message_display("asked to make a game in the style of", 24, 440, 365, self.white)
        self.message_display("'Oh ... sir, The Insult Simulator'.", 24, 440, 395, self.white)
        self.message_display("So we decided to push this project", 24, 440, 425, self.white)
        self.message_display("to the maximum using the pygame", 24, 440, 455, self.white)
        self.message_display("module with python.", 24, 440, 485, self.white)

    def select(self):
        """ Affiche l'écran de sélection des personnages """
        pygame.draw.rect(self.screen, self.black, (0, 0, 1280, 450))
        pygame.draw.rect(self.screen, self.white, (20, 55, 1240, 386))
        self.load_image_position("assets/menu/select/background.png", 1280, 330, 0, 450)

        if self.game.picking_phase == 1:
            color = self.red
        elif self.game.picking_phase == 2:
            color = self.blue
        else:
            color = self.white

        if self.select_hover == 1:
            pygame.draw.rect(self.screen, color, (20, 55, 310, 191))
        elif self.select_hover == 2:
            pygame.draw.rect(self.screen, color, (330, 55, 310, 191))
        elif self.select_hover == 3:
            pygame.draw.rect(self.screen, color, (640, 55, 310, 191))
        elif self.select_hover == 4:
            pygame.draw.rect(self.screen, color, (950, 55, 310, 191))
        elif self.select_hover == 5:
            pygame.draw.rect(self.screen, color, (20, 251, 310, 190))
        elif self.select_hover == 6:
            pygame.draw.rect(self.screen, color, (330, 251, 310, 190))
        elif self.select_hover == 7:
            pygame.draw.rect(self.screen, color, (640, 251, 310, 190))
        elif self.select_hover == 8:
            pygame.draw.rect(self.screen, color, (950, 251, 310, 190))

        self.load_image_position("assets/menu/select/return.png", 100, 50, 0, 0)
        self.load_image_position("assets/menu/select/player.png", 602, 259, 29, 462)
        if self.game.Player1.character:
            self.load_image_position(f"assets/avatar/{self.game.Player1.character}/{self.game.Player1.character}.png", 310, 190, 31, 529)
        self.load_image_position("assets/menu/select/J1.png", 359, 250, 269, 470)
        if self.game.Player1.character:
            self.message_display_right(self.game.Player1.character, 30, 602, 578, self.black, "bold")
        self.load_image_position("assets/menu/select/name_J1.png", 241, 42, 342, 619)
        self.message_display_center(self.game.Player1.name, 30, 464, 640, self.black, 3.25, "bold")
        if self.game.active_J1:
            self.load_image_position("assets/menu/select/cursor.png", 40, 30, 456 + len(self.game.Player1.name) * 7.5, 670)
        self.load_image_position("assets/menu/select/player.png", 602, 259, 653, 462)
        if self.game.Player2.character:
            self.load_image_position(f"assets/avatar/{self.game.Player2.character}/{self.game.Player2.character}.png", 310, 190, 655, 529)
        self.load_image_position("assets/menu/select/J2.png", 359, 250, 894, 470)
        if self.game.Player2.character:
            self.message_display_right(self.game.Player2.character, 30, 1230, 578, self.black, "bold")
        self.load_image_position("assets/menu/select/name_J2.png", 241, 42, 970, 619)
        self.message_display_center(self.game.Player2.name, 30, 1090, 640, self.black, 3.25, "bold")
        if self.game.active_J2:
            self.load_image_position("assets/menu/select/cursor.png", 40, 30, 1080 + len(self.game.Player2.name) * 7.5, 670)
        self.load_image_position("assets/avatar/bitcoin/bitcoin.png", 310, 190, 20, 56)
        self.message_display_center("BITCOIN", 24, 175, 218, self.black, 3, "bold")
        self.load_image_position("assets/avatar/dogecoin/dogecoin.png", 310, 190, 330, 56)
        self.message_display_center("DOGECOIN", 24, 485, 218, self.black, 3, "bold")
        self.load_image_position("assets/avatar/sushiswap/sushiswap.png", 310, 190, 640, 56)
        self.message_display_center("SUSHISWAP", 24, 795, 218, self.black, 3, "bold")
        self.load_image_position("assets/avatar/dragonchain/dragonchain.png", 310, 190, 950, 56)
        self.message_display_center("DRAGONCHAIN", 24, 1105, 218, self.black, 3, "bold")
        self.load_image_position("assets/avatar/pancakebunny/pancakebunny.png", 310, 190, 20, 251)
        self.message_display_center("PANCAKEBUNNY", 24, 175, 410, self.black, 3, "bold")
        self.load_image_position("assets/avatar/pancakeswap/pancakeswap.png", 310, 190, 330, 251)
        self.message_display_center("PANCAKESWAP", 24, 485, 410, self.black, 3, "bold")
        self.load_image_position("assets/avatar/shiba inu/shiba inu.png", 310, 190, 640, 251)
        self.message_display_center("SHIBA INU", 24, 795, 410, self.black, 3, "bold")
        self.load_image_position("assets/avatar/uniswap/uniswap.png", 310, 190, 950, 251)
        self.message_display_center("UNISWAP", 24, 1105, 410, self.black, 3, "bold")
        pygame.draw.line(self.screen, self.black, (0, 248), (1280, 248), 5)
        pygame.draw.line(self.screen, self.black, (330, 0), (330, 448), 5)
        pygame.draw.line(self.screen, self.black, (640, 0), (640, 448), 5)
        pygame.draw.line(self.screen, self.black, (950, 0), (950, 448), 5)
        self.message_display_center("DUEL LOCAL", 30, 640, 10, self.white, 20, "bold")
        if self.game.picking_phase == 3:
            self.load_image_position("assets/menu/home/button.png", 379, 57, 450, 412)
            self.message_display_center("LANCER LE DUEL", 30, 640, 440, self.black, 3.25, "bold")

    def duel(self):
        "Affiche l'écran de combat"
        self.load_image_position("assets/dual/background.jpg", 1280, 720, 0, 0)
        pygame.draw.rect(self.screen, self.black, (140, 20, 400, 50), 5)
        pygame.draw.rect(self.screen, self.black, (740, 20, 400, 50), 5)
        pygame.draw.rect(self.screen, self.green, (143, 23, self.game.Player1.health * 0.394, 44))
        pygame.draw.rect(self.screen, self.green, (743, 23, self.game.Player2.health * 0.394, 44))
        self.message_display(f"{self.game.Player1.name} - ({self.game.Player1.character})", 24, 140, 80, self.black)
        self.message_display_right(f"{self.game.Player2.name} - ({self.game.Player2.character})", 24, 1140, 80, self.black)
        self.load_image_position(f"assets/avatar/{self.game.Player1.character}/{self.game.Player1.character}_icon.png", 100, 100, 20, 20)
        self.load_image_position(f"assets/avatar/{self.game.Player2.character}/{self.game.Player2.character}_icon.png", 100, 100, 1160, 20)
        self.load_image_position(f"assets/avatar/{self.game.Player1.character}/{self.game.Player1.character}_{self.game.Player1.side}.png", 180, 300, 140, 300)
        self.load_image_position(f"assets/avatar/{self.game.Player2.character}/{self.game.Player2.character}_{self.game.Player2.side}.png", 180, 300, 960, 300)

        self.load_image_position("assets/dual/sentence_right.png", 440, 90, 0, 200)
        if len(self.game.Player1.sentence_display) <= 33:
            self.message_display(self.game.Player1.sentence_display, 24, 55, 205, self.black)

        elif len(self.game.Player1.sentence_display) <= 67:
            self.message_display(self.game.Player1.sentence_display[0:34], 24, 55, 205, self.black)
            self.message_display(self.game.Player1.sentence_display[34:], 24, 55, 230, self.black)
        else:
            self.message_display(self.game.Player1.sentence_display[0:34], 24, 55, 205, self.black)
            self.message_display(self.game.Player1.sentence_display[34:68], 24, 55, 230, self.black)
            self.message_display(self.game.Player1.sentence_display[68:], 24, 55, 255, self.black)

        self.load_image_position("assets/dual/sentence_left.png", 440, 90, 840, 200)
        if len(self.game.Player2.sentence_display) <= 33:
            self.message_display(self.game.Player2.sentence_display, 24, 860, 205, self.black)

        elif len(self.game.Player2.sentence_display) <= 67:
            self.message_display(self.game.Player2.sentence_display[0:34], 24, 860, 205, self.black)
            self.message_display(self.game.Player2.sentence_display[34:], 24, 860, 230, self.black)
        else:
            self.message_display(self.game.Player2.sentence_display[0:34], 24, 860, 205, self.black)
            self.message_display(self.game.Player2.sentence_display[34:68], 24, 860, 230, self.black)

            self.message_display(self.game.Player2.sentence_display[68:], 24, 860, 255, self.black)

        self.message_display_center(f"{self.game.Player1.health} / {self.game.Player1.max_health}$", 24, 340, 45, self.black)
        self.message_display_center(f"{self.game.Player2.health} / {self.game.Player2.max_health}$", 24, 940, 45, self.black)
        self.load_image_position("assets/menu/home/background_menu.png", 300, 500, 490, 130)
        if self.game.words.word_1:
            self.load_image_position("assets/menu/home/button.png", 250, 40, 515, 150)
            self.message_display_center(self.game.words.word_1, 24, 635, 170, self.black, 3)
        if self.game.words.word_2:
            self.load_image_position("assets/menu/home/button.png", 250, 40, 515, 210)
            self.message_display_center(self.game.words.word_2, 24, 635, 230, self.black, 3)
        if self.game.words.word_3:
            self.load_image_position("assets/menu/home/button.png", 250, 40, 515, 270)
            self.message_display_center(self.game.words.word_3, 24, 635, 290, self.black, 3)
        if self.game.words.word_4:
            self.load_image_position("assets/menu/home/button.png", 250, 40, 515, 330)
            self.message_display_center(self.game.words.word_4, 24, 635, 350, self.black, 3)
        if self.game.words.word_5:
            self.load_image_position("assets/menu/home/button.png", 250, 40, 515, 390)
            self.message_display_center(self.game.words.word_5, 24, 635, 410, self.black, 3)
        if self.game.words.word_6:
            self.load_image_position("assets/menu/home/button.png", 250, 40, 515, 450)
            self.message_display_center(self.game.words.word_6, 24, 635, 470, self.black, 3)
        if self.game.words.word_7:
            self.load_image_position("assets/menu/home/button.png", 250, 40, 515, 510)
            self.message_display_center(self.game.words.word_7, 24, 635, 530, self.black, 3)
        if self.game.words.word_8:
            self.load_image_position("assets/menu/home/button.png", 250, 40, 515, 570)
            self.message_display_center(self.game.words.word_8, 24, 635, 590, self.black, 3)

        if self.game.turn % 2 == 1:
            if not self.game.Player1.ready:
                if self.game.words.bonus_word_1:
                    self.load_image_position("assets/menu/home/button.png", 350, 40, 0, 650)
                    self.message_display_center(self.game.words.bonus_word_1, 24, 175, 670, self.black, 3)
                if self.game.words.bonus_word_2:
                    self.load_image_position("assets/menu/home/button.png", 250, 40, 350, 650)
                    self.message_display_center(self.game.words.bonus_word_2, 24, 475, 670, self.black, 3)
                pygame.draw.rect(self.screen, self.white, (0, 550, 75, 75))
                pygame.draw.rect(self.screen, self.black, (0, 550, 75, 75), 5)
                self.message_display_center("... !", 48, 37.5, 582.5, self.red, 6)

        else:
            if not self.game.Player2.ready:
                if self.game.words.bonus_word_3:
                    self.load_image_position("assets/menu/home/button.png", 250, 40, 680, 650)
                    self.message_display_center(self.game.words.bonus_word_3, 24, 805, 670, self.black, 3)
                if self.game.words.bonus_word_4:
                    self.load_image_position("assets/menu/home/button.png", 350, 40, 930, 650)
                    self.message_display_center(self.game.words.bonus_word_4, 24, 1105, 670, self.black, 3) 
                pygame.draw.rect(self.screen, self.white, (1205, 550, 75, 75))
                pygame.draw.rect(self.screen, self.black, (1205, 550, 75, 75), 5)
                self.message_display_center("... !", 48, 1242.5, 582.5, self.red, 6)

        if self.game.damage_player_1 and self.game.damage_player_2 and self.game.turn == 1:
            self.message_display_center(f"- {self.game.damage_player_2}", 60, 300, 200, self.red, 8, "bold")
            self.message_display_center(f"- {self.game.damage_player_1}", 60, 980, 200, self.red, 8, "bold")

    def endscreen(self):
        self.load_image_position("assets/dual/background.jpg", 1280, 720, 0, 0)
        if self.game.Player1.health == 0:
            self.message_display_center(f"{self.game.Player2.name} HAS WON AS {self.game.Player2.character}", 60, 640, 260, self.black, 8, "bold")
            self.message_display_center("press esc to go to the menu", 60, 640, 500, self.black, 8, "bold")
        elif self.game.Player2.health == 0:
            self.message_display_center(f"{self.game.Player1.name} HAS WON AS {self.game.Player1.character}", 60, 640, 260, self.black, 8, "bold")
            self.message_display_center("press esc to go to the menu", 60, 640, 500, self.black, 8, "bold")
        else:
            self.message_display_center(f"NOBODY WON, IT WAS A DOUBLE SUICIDE", 60, 640, 260, self.black, 8, "bold")
            self.message_display_center("press esc to go to the menu", 60, 640, 500, self.black, 8, "bold")
