"Fichier pour le jeu"
import pygame
from display import Display
from player import Player
from words import Words

# Crée une classe qui représente le jeu
class Game():
    """ Définit les informations du jeu """
    def __init__(self, screen):
        # Le jeu est lancé
        self.is_playing = False

        # Stock les touches pressés
        self.pressed = {}

        # Charge l'affichage
        self.display = Display(self, screen)

        # Charge les mots
        self.words = Words()

        # Définit l'état initial de l'écran de sélection
        self.choice = None
        self.picking_phase = 1
        self.active_J1 = False
        self.active_J2 = False
        self.turn = 1
        self.Player1 = Player(self, "Player 1", None, "right")
        self.Player2 = Player(self, "Player 2", None, "left")
        self.damage_player_1 = 0
        self.damage_player_2 = 0

    def update(self):
        "Met à jour le jeu"
        # On est dans le menu de départ
        if not self.is_playing and self.choice:

            # Le joueur 1 choisit son personnage
            if self.picking_phase == 1:
                self.Player1.change_character(self.choice)
                self.picking_phase = 2

            # Le joueur 2 choisit son personnage
            elif self.picking_phase == 2:
                self.Player2.change_character(self.choice)
                self.picking_phase = 3

            self.choice = None

        # Le duel a commencé
        if self.is_playing:

            # Quand les deux joueurs ont leur phrase prêtes calcule les dégats et régénère un nouveau round
            if self.Player1.ready and self.Player2.ready:
                self.damage_player_1 = len(self.Player1.sentence_display) * 5
                if self.Player2.weakness in self.Player1.sentence:
                    self.damage_player_1 += 100

                self.damage_player_2 = len(self.Player2.sentence_display) * 5
                if self.Player1.weakness in self.Player2.sentence:
                    self.damage_player_2 += 100
                self.Player1.lose_hp(self.damage_player_2)
                self.Player2.lose_hp(self.damage_player_1)

                # Passe au prochain round
                self.words.generate()
                self.words.reset_words()
                self.Player1.clear_sentence()
                self.Player2.clear_sentence()
                self.turn = 1

            # Régénère des mots lorsque tout a été utilisé
            elif (not self.words.word_1 and not self.words.word_2 and not self.words.word_3 and not self.words.word_4 and not self.words.word_5 
            and not self.words.word_6 and not self.words.word_7 and not self.words.word_8):
                self.words.generate()
                self.words.reset_words()

            # Tant qu'aucun des joueurs passe à 0 point de vie, le duel continue
            if self.Player1.health == 0 or self.Player2.health == 0:
                pygame.time.delay(3000)
                self.is_playing = False
                self.display.endscreen()

            if self.choice:

                # C'est le tour du Joueur 1
                if self.turn % 2 == 1:
                    # Ajoute le mot choisit
                    self.Player1.sentence.append(self.choice)

                    # Vérifie si il y a une erreur dans la phrase
                    if self.Player1.check_error():

                        # Finit la phrase
                        if self.Player1.sentence == "!":
                            self.Player1.ready = True

                        # Rajoute le mot à la phrase du joueur
                        if self.Player1.sentence_display:
                            self.Player1.sentence_display += " " + self.choice

                        else:
                            self.Player1.sentence_display += self.choice
                        
                        # Enlève l'espace si il est au début de ligne
                        if len(self.Player1.sentence_display) > 34:
                            if self.Player1.sentence_display[34] == " ":
                                    self.Player1.sentence_display = self.Player1.sentence_display[:34] + self.Player1.sentence_display[35:]

                        if len(self.Player1.sentence_display) > 68:
                            if self.Player1.sentence_display[68] == " ":
                                self.Player1.sentence_display = self.Player1.sentence_display[:68] + self.Player1.sentence_display[69:]
                
                    else:
                        # Lors d'une erreur, perd des pv et enlève l'erreur
                        self.Player1.sentence.remove(self.choice)
                        self.Player1.lose_hp(100)

                # C'est le tour du Joueur 2
                else:
                    # Ajoute le mot choisit
                    self.Player2.sentence.append(self.choice)

                    # Vérifie si il y a une erreur dans la phrase
                    if self.Player2.check_error():

                        # Finit la phrase
                        if self.Player2.sentence[-1] == "!":
                            self.Player2.ready = True
                        
                        # Rajoute le mot à la phrase du joueur
                        if self.Player2.sentence_display:
                            self.Player2.sentence_display += " " + self.choice

                        else:
                            self.Player2.sentence_display += self.choice

                    # Enlève l'espace si il est au début de ligne
                        if len(self.Player2.sentence_display) > 34:
                            if self.Player2.sentence_display[34] == " ":
                                    self.Player2.sentence_display = self.Player2.sentence_display[:34] + self.Player2.sentence_display[35:]

                        if len(self.Player2.sentence_display) > 68:
                            if self.Player2.sentence_display[68] == " ":
                                self.Player2.sentence_display = self.Player2.sentence_display[:68] + self.Player2.sentence_display[69:]

                    else:
                         # Lors d'une erreur, perd des pv et enlève l'erreur
                        self.Player2.sentence.remove(self.choice)
                        self.Player2.lose_hp(100)

                self.choice = None
                self.turn += 1

            # Si un joueur a finit sa phrase, laisse l'autre joueur finir la sienne
            elif self.Player1.ready and self.turn % 2 == 1:
                self.turn += 1
            
            elif self.Player2.ready and self.turn %2 == 0:
                self.turn += 1

    def reset(self):
        "Remet à zéro les données du jeu"
        if self.Player1 and self.Player2:
            del self.Player1
            del self.Player2
        self.choice = None
        self.picking_phase = 1
        self.active_J1 = False
        self.active_J2 = False
        self.turn = 1
        self.Player1 = Player(self, "Player 1", None, "right")
        self.Player2 = Player(self, "Player 2", None, "left")
        self.damage_player_1 = 0
        self.damage_player_2 = 0