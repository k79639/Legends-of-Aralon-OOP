'''This module handels the hero's of the game and their logic and inherits from character base class'''
from character import Character

class Hero(Character):
    def __init__(self, name, health, title, coloredName, stamina, strength, intelligence):
        Character.__init__(self, name, health, title, coloredName)
        self._stamina = stamina
        self._strength = strength
        self._intelligence = intelligence

    def getStrength(self):
        return self._strength
    
    def getIntelligence(self):
        return self._strength
    
    def getStamina(self):
        return self._stamina
    
