'''This module creates the characters of the game and handel their logic and decisions'''
import random

class Character:

    def __init__(self, name, health, title, coloredName):
        self._name = name
        self._health = health
        self._title = title
        self._coloredName = coloredName
        self._characterRoll = -999
        self._characterDecision = None

    '''This module rolls 2 six-sided dice for characters and store their outcome'''
    def rollDice(self):
        self._characterRoll = random.randint(0, 12)

    '''This method gives characters ability to make decision mainly for monsters and "AI" '''
    def characterDecision(self):
        # 50% chance for character to give it's decision as True
        if random.randint(0, 1) > 0.5:
            self._characterDecision = True

        else:
            self._characterDecision = False
        