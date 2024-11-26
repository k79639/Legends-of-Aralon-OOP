'''This module handels the game logic'''
#import all the necessary modules for game
from hero import Hero 
from monster import Monster
from script import Script
from challenge import Challenge

class Game:
    def __init__(self):
        #Create script for game and pass game instance to script
        self._script = Script(self)
        #Create challenges for game and pass game instance to challenge
        self._challenge = Challenge(self)

    def run(self):
        #print a “welcome” message and provide a short overview of the game
        self._script.displayWelcome()

        