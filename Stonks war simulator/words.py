"Fichier pour les mots"
import pygame
import random

class Words():
    """ Définit les mots """
    def __init__(self):
        self.subject = [["you", "your name", "your crypto", "your icon"], ["subject"]]
        self.verb = [["smell like", "is", "seems like", "appears to be"],["verb"]]
        self.supplement = [["a ponzi pyramid", "a scam", "a hateful trap", "a bad meme", "a fake horse", "a stingy trash", "an expired pancake", "a big dog", "a scheme of Elon Musk", "an outdated fish", "a smelly bunny"], ["supplement"]]
        self.connector = [["and", "and"], ["connector"]]
        self.final = [["you are already part of the past !", "it is time to give up !", "you should not have been born !", "Elon Musk would give up on you !"], ["final"]]

        self.word_1 = None
        self.word_2 = None
        self.word_3 = None
        self.word_4 = None
        self.word_5 = None
        self.word_6 = None
        self.word_7 = None
        self.word_8 = None
        self.bonus_word_1 = None
        self.bonus_word_2 = None
        self.bonus_word_3 = None
        self.bonus_word_4 = None
        self.word_database = None

    def reset_words(self):
        "Remet à l'état d'origine les mots sélectionnables aléatoirement"
        self.subject = [["you", "your name", "your crypto", "your icon"], ["subject"]]
        self.verb = [["smell like", "is", "seems like", "appears to be"],["verb"]]
        self.supplement = [["a ponzi pyramid", "a scam", "a hateful trap", "a bad meme", "a fake horse", "a stingy trash", "an expired pancake", "a big dog", "a scheme of Elon Musk", "an outdated fish", "a smelly bunny"], ["supplement"]]
        self.connector = [["and", "and"], ["connector"]]
        self.final = [["you are already part of the past !", "it is time to give up !", "you should not have been born !", "Elon Musk would give up on you !"], ["final"]]

    def generate(self):
        "Choisit aléatoirement les 8 mots permettant de composer une phrase ainsi que 2 mots bonus personnels pour chaque joueurs"
        self.word_database = [self.subject, self.verb, self.supplement, self.connector]
        random.shuffle(self.word_database)
        place = [1,2,3,4,5,6,7,8]
        random.shuffle(place)
        for x in range(0, 4):
            for y in range(0, 2):

                if self.word_database[x][1] != "connector":
                    index = random.randint(0, len(self.word_database[x][0])-1)

                else:
                    index = 0

                word = self.word_database[x][0][index]
                del self.word_database[x][0][index]
                message_assignment = f"self.word_{place[0]}"
                del place[0]
                exec(message_assignment + f" = '{word}' ")

            if x in [0, 3]:
                random_index = random.randint(0, len(self.final[0])-1)
                word = self.final[0][random_index]
                del self.final[0][random_index]

            else:
                for loop in range(0, 4):
                    if self.word_database[loop][1][0] == "supplement":
                        random_index = random.randint(0, len(self.word_database[loop][0])-1)
                        word = self.word_database[loop][0][random_index]
                        del self.word_database[loop][0][random_index]

            message_assignment = f"self.bonus_word_{x+1}"
            exec(message_assignment + f" = '{word}'")