'''This module creates the characters of the game and handel their logic and decisions'''
class Character:

    def __init__(self, name, health, title, coloredName):
        self._name = name
        self._health = health
        self._title = title
        self._coloredName = coloredName
        self._characterRoll = -999
        