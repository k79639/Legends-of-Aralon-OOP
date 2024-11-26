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
        self._userChoice = None
        self._heroCharacter = None
        self._aiCharacter = None
        self._round1Monster = None
        self._round2Monster = None
        self._round3Monster = None
        self._round4Monster = None
        self._round5Monster = None

    def getHero(self):
        return self._heroCharacter
    
    def getAi(self):
        return self._aiCharacter

    

    '''This method is the main game method which handel the logic and flow of the game'''
    def run(self):
        #Print a “welcome” message and provide a short overview of the game
        self._script.displayWelcome()

        #Prints the characters options to choose from
        self._script.displayOptions()

        #Allow the user to choose one of the two roles implemented in the game
        self._userChoice = self.selectCharacter()
        
        #Acknowledge the user choice and create all the characters of the game
        self.createCharacters()

        #Display the character assigned to their role
        self._script.displayRoles()

        #Present the challenges implemented in the game, one at a time.
        self._script.orianaAndChallenge1Intro()



    '''This method allow user to select one of the two characters implemented in the game'''
    def selectCharacter(self):
        validChoice = False
        while not validChoice: #Loop until user gives valid choice
            global selectedHero
            #strip the space from front and back of the user input (if added) and convert it into lowercase
            selectedHero = input("\nYour choice (\033[92mValerius\033[0m/\033[94mEldara\033[0m): ").strip().lower() 
            if selectedHero == "valerius":
                validChoice = True
                return "Valerius"

            elif selectedHero == "eldara":
                validChoice = True
                return "Eldara"

            else:
                print("\n\033[91mInvalid choice.\033[0m Please type \033[92m'Valerius'\033[0m or \033[94m'Eldara'\033[0m.")

    '''This method creates all the charcaters of the game according to the user selection'''
    def createCharacters(self):
        #Create all the monsters in the game for each round
        self._round1Monster = Monster("Kragnar", 25, "Kragnar the Stoneborn!", "\033[35mKragnar")
        self._round2Monster = Monster("Azra", 25, "Azra the Mirror Fiend", "\033[35mAzar")
        self._round3Monster = Monster("Malakar", 30, "Malakar the Life Leech", "\033[35mMalakar")
        self._round4Monster = Monster("Ignarok", 30, "Ignarok the Blazing Drake", "\033[35mIgnarok")
        self._round5Monster = Monster("Zarok", 35, "Zarok the Deathbringer", "\033[35mZarok")

        #Set valerius as Hero and eldara as AI
        if self._userChoice == "Valerius":
            self._heroCharacter = Hero("Valerius", 50, "the Guardian Knight", "\033[92mValerius", 2, 2, -3)
            self._aiCharacter = Hero("Eldara", 50, "the Mystic Sage", "\033[94mEldara", -1, -2, 3)

        #Set eldara as Hero and valerius as AI
        elif self._userChoice == "Eldara":
            self._heroCharacter = Hero("Eldara", 50, "the Mystic Sage", "\033[94mEldara", -1, -2, 3)
            self._aiCharacter = Hero("Valerius", 50, "the Guardian Knight", "\033[92mValerius", 2, 2, -3)
        


        