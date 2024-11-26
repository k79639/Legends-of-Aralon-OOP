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
        self._selectedCharacter = None
    

    '''This method is the main game method handel the logic and flow of the game'''
    def run(self):
        #Print a “welcome” message and provide a short overview of the game
        self._script.displayWelcome()

        #Allow the user to choose one of the two roles implemented in the game
        self.selectCharacter()



    '''This method allow user to select one of the two characters implemented in the game'''
    def selectCharacter(self):
        validChoice = False
        while not validChoice: #Loop until user gives valid choice
            global selectedHero
            selectedHero = input("\nYour choice (\033[92mValerius\033[0m/\033[94mEldara\033[0m): ").strip().lower()

            if selectedHero == "valerius":
                return "Valerius"

            elif selectedHero == "eldara":
                return "Eldara"

            else:
                print("\n\033[91mInvalid choice.\033[0m Please type \033[92m'Valerius'\033[0m or \033[94m'Eldara'\033[0m.", 0.03)


        