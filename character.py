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

    def getColorName(self):
        return self._coloredName
    
    def getTitle(self):
        return self._title
    
    def getHealth(self):
        return self._health
    
    def getRoll(self):
        return self._characterRoll
    
    def getName(self):
        return self._name
    
    def getCharacterDecision(self):
        return self._characterDecision

    '''This method rolls 2 six-sided dice for characters and store their outcome'''
    def rollDice(self):
        self._characterRoll = random.randint(0, 12)

    '''This method gives characters ability to make decision mainly for monsters and "AI" '''
    def characterDecision(self):
        # 50% chance for character to give it's decision as True
        if random.randint(0, 1) > 0.5:
            self._characterDecision = True
        else:
            self._characterDecision = False

    '''This method return true or false based on if character is alive or not and sets the not alive character roll to 0'''
    def characterIsAlive(self):
        if self._health > 0:
            return True
        elif self._health <= 0:
            #If a character is not alive set its roll to 0 so it does not affect the logic and calculation in the battle mainly for if hero or ai dies.
            self._characterRoll = 0
            return False
        else: 
            return None
        
    '''This method updates the health of the characters after the damage and ensure it never goes into negative'''
    def updateHealth(self, damage):
        if self._health - damage < 0:
            self._health = 0
        else:
            self._health = self._health - damage
        