'''This module handels the hero's of the game and their logic and inherits from character base class'''
from character import Character

class Party(Character):
    def __init__(self, name, health, title, coloredName, stamina, strength, intelligence):
        Character.__init__(self, name, health, title, coloredName)
        self._stamina = stamina
        self._strength = strength
        self._intelligence = intelligence
        self._shieldBreaksLeft = 3

    def getStrength(self):
        return self._strength
    
    def getIntelligence(self):
        return self._strength
    
    def getStamina(self):
        return self._stamina
    
    def getTotalShieldsLeft(self):
        return self._shieldBreaksLeft
    
    '''This method gives selected hero ability to destroy monster shield'''
    def destroyShield(self):
        try:
            if self._shieldBreaksLeft > 0:
                validChoice = False
                while not validChoice:
                    userSelection = input(f"\n\033[4mDo you want to use {self.getColorName()}\033[0m\033[4m ability to break monster's shield?\033[0m (yes/no): ").strip().lower()
                    if userSelection == "yes" or userSelection == "y":
                        self._shieldBreaksLeft -= 1
                        print(f"\n{self.getColorName()}\033[0m shatters monster's shield")
                        validChoice = True
                        return True
                    elif userSelection == "no" or userSelection == "n":
                        print(f"\n{self.getColorName()}\033[0m decides to save their ability for now.")
                        validChoice = True
                    else:
                        print("\n\033[91mInvalid choice.\033[0m Please type 'Yes' or 'No'.")
            elif self._shieldBreaksLeft <= 0:
                print(f"\n{self.getColorName()}\033[0m shield-breaking ability is exhausted! Monster's shield absorbs your attack!")
        except KeyboardInterrupt:
            raise
            

