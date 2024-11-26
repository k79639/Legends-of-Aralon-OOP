'''This module prints and handel the script, game messages and storyteller'''
import sys
import time

class Script:
    def __init__(self, gameInstance):
        self._game = gameInstance
        self._oriana = "\033[93mOriana:\033[0m " #creates storyteller

    