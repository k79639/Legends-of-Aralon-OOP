'''This module handels the hero's of the game and their logic and inherits from character base class'''
from character import Character

class Monster(Character):
    def __init__(self, name, health, title, coloredName):
        Character.__init__(self, name, health, title, coloredName)