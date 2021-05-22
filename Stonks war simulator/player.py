"Fichier pour le joueur"

class Player():
    """ Définit le joueur """
    def __init__(self, game, name, character, side):
        self.game = game
        self.name = name
        self.character = character
        self.side = side
        self.avatar = None
        self.health = 1000
        self.max_health = 1000
        self.sentence = []
        self.sentence_display = ""
        self.ready = False
        self.weakness = None

    def change_name(self, name):
        "Change le nom du joueur"
        self.name = name

    def change_character(self, character):
        "Change le personnage du joueur"
        self.character = character
        if self.character == "BITCOIN":
            self.weakness = "a scheme of Elon Musk"
        elif self.character == "DOGECOIN":
            self.weakness = "a bad meme"
        elif self.character == "SHIBA INU":
            self.weakness = "a big dog"
        elif self.character == "UNISWAP":
            self.weakness = "a fake horse"
        elif self.character == "PANCAKESWAP":
            self.weakness = "an expired pancake"
        elif self.character == "SUSHISWAP":
            self.weakness = "an outdated fish"
        elif self.character == "PANCAKEBUNNY":
            self.weakness = "a smelly bunny"
        elif self.character == "DRAGONCHAIN":
            self.weakness = "a stingy trash"

    def lose_hp(self, damage):
        "Permet d'influencer sur les points de vie du joueur"
        self.health -= damage
        if self.health > self.max_health:
            self.health = self.max_health
        if self.health < 0:
            self.health = 0

    def clear_sentence(self):
        self.sentence = []
        self.sentence_display = ""
        self.ready = False

    def check_error(self):
        "Vérifie la phrase fonctionne mot à mot"

        if len(self.sentence) == 1:
            if self.sentence[0] not in self.game.words.connector[0] and self.sentence[0] not in self.game.words.verb[0] and self.sentence[0] != "!":
                return True

            else:
                return False

        if len(self.sentence) > 1:
            if self.sentence[-2] in self.game.words.final[0] and self.sentence[-1]:
                return False

        if len(self.sentence) == 2:
            if self.sentence[0] in self.game.words.subject[0] or self.sentence[0] in self.game.words.supplement[0]:
                if self.sentence[1] in self.game.words.verb[0]:
                    return True

                elif self.sentence[1] in self.game.words.connector[0]:
                    return True

                else:
                    return False
            
            else:
                return False

        elif len(self.sentence) == 3:
            if self.sentence[1] in self.game.words.verb[0]:
                if self.sentence[2] in self.game.words.subject[0] or self.sentence[2] in self.game.words.supplement[0]:
                    return True

                else:
                    return False

            elif self.sentence[1] in self.game.words.connector[0]:
                if self.sentence[2] in self.game.words.subject[0] or self.sentence[2] in self.game.words.supplement[0]:
                    return True

                else: 
                    return False

        elif len(self.sentence) == 4:
            if self.sentence[1] in self.game.words.verb[0]:
                if self.sentence[2] in self.game.words.subject[0] or self.sentence[2] in self.game.words.supplement[0]:
                    if self.sentence[3] in self.game.words.connector[0]:
                        return True

                    if self.sentence[3] == "!":
                      self.ready = True
                      return True

                    else: 
                        return False

            elif self.sentence[1] in self.game.words.connector[0]:
                if self.sentence[2] in self.game.words.subject[0] or self.sentence[2] in self.game.words.supplement[0]:
                    if self.sentence[3] in self.game.words.verb[0]:
                        return True

                    else:
                        return False
        
        elif len(self.sentence) == 5:
            if self.sentence[3] in self.game.words.connector[0]:
                if self.sentence[4] in self.game.words.final[0]:
                    self.ready = True
                    return True
                
                else:
                    return False
            
            elif self.sentence[3] in self.game.words.verb[0]:
                if self.sentence[4] in self.game.words.subject[0] or self.sentence[4] in self.game.words.supplement[0]:
                    return True

                else:
                    return False
        
        elif len(self.sentence) == 6:
            if self.sentence[4] in self.game.words.subject[0] or self.sentence[4] in self.game.words.supplement[0]:
                if self.sentence[5] in self.game.words.connector[0]:
                    return True

                elif self.sentence[5] == "!":
                    self.ready = True
                    return True
                
                else:
                    return False

        elif len(self.sentence) == 7:
            if self.sentence[6] in self.game.words.final[0]:
                self.ready = True
                return True

            elif self.sentence[6] in self.game.words.subject[0] or self.sentence[6] in self.game.words.supplement[0]:
                return True

            else:
                return False
            
        elif len(self.sentence) == 8:
            if self.sentence[7] == "!":
                self.ready = True
                return True

            else:
                return False
