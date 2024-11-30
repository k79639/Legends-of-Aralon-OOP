'''This module handels the game logic'''
#import all the necessary modules for game
from hero import Hero 
from monster import Monster
from script import Script
from challenge import Challenge

class Game:
    def __init__(self):
        self._script = None
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
        self._challengeNum = -1
        self._gameEnd = False
        self._roundWinner = None
        self._alertAboutAiDeath = False
        self._alertAboutHeroDeath = False

    def getHero(self):
        return self._heroCharacter
    
    def getAi(self):
        return self._aiCharacter
    
    def getChallengeNum(self):
        return self._challengeNum
    
    def getChallenge1Monster(self):
        return self._round1Monster
    
    def getChallenge2Monster(self):
        return self._round2Monster
    
    def getChallenge3Monster(self):
        return self._round3Monster
    
    def getChallenge4Monster(self):
        return self._round4Monster
    
    def getChallenge5Monster(self):
        return self._round5Monster

    def getScript(self):
        return self._script
    
    def getRoundWinner(self):
        return self._roundWinner
    
    def setUserChoice(self, userChoice):
        self._userChoice = userChoice

    def setScript(self, scriptInstance):
        self._script = scriptInstance

    '''This method is the main game method which handel the logic and flow of the game'''
    def run(self):
        
        #Acknowledge the user choice and create all the characters of the game
        self.createCharacters()

        #Display the character assigned to their role
        self._script.displayRoles()

        #set challenge number to 1.
        self._challengeNum = 1

        #Loop battle until game ends
        while not self._gameEnd:
            self._roundWinner = False
            self._challenge.battlefield()

    '''This method creates all the charcaters of the game according to the user selection'''
    def createCharacters(self):
        #Create all the monsters in the game for each round
        self._round1Monster = Monster("Kragnar", 50, "Kragnar the Stoneborn!", "\033[35mKragnar")
        self._round2Monster = Monster("Azra", 50, "Azra the Mirror Fiend", "\033[35mAzar")
        self._round3Monster = Monster("Malakar", 60, "Malakar the Life Leech", "\033[35mMalakar")
        self._round4Monster = Monster("Ignarok", 60, "Ignarok the Blazing Drake", "\033[35mIgnarok")
        self._round5Monster = Monster("Zarok", 70, "Zarok the Deathbringer", "\033[35mZarok")

        #Set valerius as Hero and eldara as AI
        if self._userChoice == "Valerius":
            self._heroCharacter = Hero("Valerius", 50, "the Guardian Knight", "\033[92mValerius", 2, 2, -3)
            self._aiCharacter = Hero("Eldara", 50, "the Mystic Sage", "\033[94mEldara", -1, -2, 3)

        #Set eldara as Hero and valerius as AI
        elif self._userChoice == "Eldara":
            self._heroCharacter = Hero("Eldara", 50, "the Mystic Sage", "\033[94mEldara", -1, -2, 3)
            self._aiCharacter = Hero("Valerius", 50, "the Guardian Knight", "\033[92mValerius", 2, 2, -3)
        
    '''This method determines if someone wins a challenge'''
    def determineRoundWinner(self):
        if self._challenge.getMonster().characterIsAlive() and (self._heroCharacter.characterIsAlive() > 0 or self._aiCharacter.characterIsAlive()):
            self._roundWinner = False

        elif not self._challenge.getMonster().characterIsAlive() and (self._heroCharacter.characterIsAlive() > 0 or self._aiCharacter.characterIsAlive()):
            self._challengeNum += 1
            self._roundWinner = True           

    '''This method determines if someone wins the game'''
    def determineGameWinner(self):
        if not self._round5Monster.characterIsAlive() and (self._heroCharacter.characterIsAlive() > 0 or self._aiCharacter.characterIsAlive()):
            self._script.zarokFinalDialogues()
            self._script.orianaFinalDialogues()
            self._script.thankyouMessage()
            self._roundWinner = True
            self._gameEnd = True
        
        elif not self._aiCharacter.characterIsAlive() and not self._heroCharacter.characterIsAlive():
            self._script.typingEffect(f"\n{self._challenge.getMonster().getColorName()}\033[0m stands victorious! Both heroes have fallen in battle.\t\n\n\033[7mGAME OVER\033[0m\n") 
            self._roundWinner = True
            self._gameEnd = True 

    '''This method alearts the player if someone dies'''
    def alertPlayerAboutCharacterDeath(self):
        if not self._aiCharacter.characterIsAlive() and self._alertAboutAiDeath == False and self._alertAboutHeroDeath == False:
            self._script.typingEffect(f"\n{self._aiCharacter.getColorName()}\033[0m has fallen in battle! Only {self._heroCharacter.getColorName()}\033[0m remains to carry the kingdom's hope.")
            self._alertAboutAiDeath = True
        
        elif not self._heroCharacter.characterIsAlive() and self._alertAboutHeroDeath == False and self._alertAboutAiDeath == False:
            self._script.typingEffect(f"\n{self._heroCharacter.getColorName()}\033[0m has fallen in battle! Only {self._aiCharacter.getColorName()}\033[0m remains to carry the kingdom's hope.")
            self._alertAboutHeroDeath = True

            

